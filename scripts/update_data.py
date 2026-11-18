#!/usr/bin/env python3
"""
UFC ADVERSARIAL JUDGE - ONE-COMMAND DATA REFRESH
================================================
    python3 scripts/update_data.py            # download + rebuild data + refit model
    python3 scripts/update_data.py --full     # ...also rerun walk-forward eval and the backtest report
    python3 scripts/update_data.py --check    # just say how fresh the local data is

Where the data comes from
-------------------------
UFCStats.com is the official stats provider, but it now puts a JavaScript
"checking your browser" wall in front of scripts, so the old scraper.py gets an
empty page. Instead this pulls the public mirror at
github.com/Greco1899/scrape_ufc_stats, which re-scrapes UFCStats every day and
publishes every event, fight, round-by-round stat line and fighter profile as CSV.
It is the same numbers, in a stable format, without hitting UFCStats ourselves.

Safety checks before anything is replaced
-----------------------------------------
  1. All six files download and contain the expected columns.
  2. No file shrinks by more than 1% compared with the copy we already have
     (a broken upstream scrape usually shows up as missing rows).
  3. The newest event date is not older than the one we already have.
Only then is the new copy swapped in. The previous copy is kept in
data/raw/ufcstats/_previous/ so a bad refresh can be rolled back by hand.
"""

import argparse
import hashlib
import io
import json
import os
import shutil
import sys
from datetime import datetime, timezone

import pandas as pd
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(ROOT, 'data', 'raw', 'ufcstats')
MANIFEST = os.path.join(RAW_DIR, 'manifest.json')
REPO = 'Greco1899/scrape_ufc_stats'
BRANCH = 'main'
USER_AGENT = 'ufc-adversarial-judge-data-refresh'

FILES = {
    'ufc_event_details': ['EVENT', 'URL', 'DATE', 'LOCATION'],
    'ufc_fight_results': ['EVENT', 'BOUT', 'OUTCOME', 'WEIGHTCLASS', 'METHOD', 'ROUND', 'TIME',
                          'TIME FORMAT', 'REFEREE', 'DETAILS', 'URL'],
    'ufc_fight_stats': ['EVENT', 'BOUT', 'ROUND', 'FIGHTER', 'KD', 'SIG.STR.', 'TOTAL STR.', 'TD',
                        'SUB.ATT', 'REV.', 'CTRL', 'HEAD', 'BODY', 'LEG', 'DISTANCE', 'CLINCH', 'GROUND'],
    'ufc_fighter_details': ['FIRST', 'LAST', 'NICKNAME', 'URL'],
    'ufc_fighter_tott': ['FIGHTER', 'HEIGHT', 'WEIGHT', 'REACH', 'STANCE', 'DOB', 'URL'],
}
STALE_AFTER_DAYS = 7


def _get(url, timeout=60):
    resp = requests.get(url, headers={'User-Agent': USER_AGENT}, timeout=timeout)
    resp.raise_for_status()
    return resp.content


def upstream_commit():
    """Latest commit on the mirror (so we know exactly which snapshot we have)."""
    try:
        data = json.loads(_get(f'https://api.github.com/repos/{REPO}/commits/{BRANCH}', timeout=20))
        return {'sha': data['sha'], 'date': data['commit']['author']['date'],
                'message': data['commit']['message']}
    except Exception as exc:  # the API is rate limited; this is informational only
        return {'sha': None, 'error': str(exc)}


def read_manifest():
    if os.path.exists(MANIFEST):
        with open(MANIFEST) as fh:
            return json.load(fh)
    return None


def latest_event_date(event_csv_bytes):
    ev = pd.read_csv(io.BytesIO(event_csv_bytes))
    return pd.to_datetime(ev['DATE'].str.strip(), format='%B %d, %Y', errors='coerce').max()


def download_and_validate(commit_sha=None):
    """Download every file into memory and check it. Raises on any problem."""
    ref = commit_sha or BRANCH
    previous = read_manifest() or {}
    prev_files = previous.get('files', {})
    blobs, info = {}, {}
    for name, required in FILES.items():
        url = f'https://raw.githubusercontent.com/{REPO}/{ref}/{name}.csv'
        blob = _get(url)
        df = pd.read_csv(io.BytesIO(blob), low_memory=False)
        missing = [c for c in required if c not in df.columns]
        if missing:
            raise ValueError(f'{name}.csv is missing columns {missing}; upstream format changed.')
        prev_rows = prev_files.get(name, {}).get('rows')
        if prev_rows and len(df) < prev_rows * 0.99:
            raise ValueError(f'{name}.csv shrank from {prev_rows:,} to {len(df):,} rows; refusing to update.')
        blobs[name] = blob
        info[name] = {'rows': len(df), 'sha256': hashlib.sha256(blob).hexdigest()}

    newest = latest_event_date(blobs['ufc_event_details'])
    prev_newest = previous.get('latest_event')
    if prev_newest and newest < pd.Timestamp(prev_newest):
        raise ValueError(f'Newest event {newest:%Y-%m-%d} is older than what we have ({prev_newest}).')
    return blobs, info, newest


def install(blobs, info, newest, commit):
    """Swap the validated files in, keeping the previous copy for rollback."""
    os.makedirs(RAW_DIR, exist_ok=True)
    prev_dir = os.path.join(RAW_DIR, '_previous')
    if any(os.path.exists(os.path.join(RAW_DIR, f'{n}.csv')) for n in FILES):
        shutil.rmtree(prev_dir, ignore_errors=True)
        os.makedirs(prev_dir)
        for n in list(FILES) + ['manifest']:
            ext = 'json' if n == 'manifest' else 'csv'
            src = os.path.join(RAW_DIR, f'{n}.{ext}')
            if os.path.exists(src):
                shutil.copy2(src, prev_dir)
    for name, blob in blobs.items():
        tmp = os.path.join(RAW_DIR, f'.{name}.csv.tmp')
        with open(tmp, 'wb') as fh:
            fh.write(blob)
        os.replace(tmp, os.path.join(RAW_DIR, f'{name}.csv'))
    manifest = {
        'source': f'https://github.com/{REPO}', 'commit': commit,
        'downloaded_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'latest_event': f'{newest:%Y-%m-%d}', 'files': info,
    }
    with open(MANIFEST, 'w') as fh:
        json.dump(manifest, fh, indent=2)
    return manifest


def data_age_days():
    """Days since the last successful download, or None if never downloaded."""
    m = read_manifest()
    if not m:
        return None
    then = datetime.fromisoformat(m['downloaded_at'])
    return (datetime.now(timezone.utc) - then).total_seconds() / 86400


def check():
    m = read_manifest()
    if not m:
        print('No UFCStats data downloaded yet. Run: python3 scripts/update_data.py')
        return 1
    age = data_age_days()
    print(f"Last refresh   : {m['downloaded_at']} ({age:.1f} days ago)")
    print(f"Newest event   : {m['latest_event']}")
    print(f"Mirror commit  : {(m.get('commit') or {}).get('sha')}")
    print('Status         : ' + ('STALE - run update_data.py' if age > STALE_AFTER_DAYS else 'fresh'))
    return 0


def refresh(full=False, skip_download=False):
    print('=' * 70)
    print('UFC ADVERSARIAL JUDGE - DATA REFRESH')
    print('=' * 70)
    if not skip_download:
        before = read_manifest()
        commit = upstream_commit()
        print(f"[1/4] Downloading UFCStats mirror (commit {str(commit.get('sha'))[:10]})...")
        blobs, info, newest = download_and_validate(commit.get('sha'))
        manifest = install(blobs, info, newest, commit)
        old_latest = (before or {}).get('latest_event', 'none')
        print(f"      OK. Newest event {manifest['latest_event']} (previously {old_latest}).")
        for n, i in info.items():
            print(f"      {n:<22} {i['rows']:>7,} rows")
    else:
        print('[1/4] Skipping download, using files already on disk.')

    import build_dataset
    import features
    print('[2/4] Building clean fight and fighter tables...')
    build_dataset.build()
    print('[3/4] Rebuilding point-in-time features and current fighter snapshot...')
    features.build_features()

    import train_model
    print('[4/4] Refitting the prediction model on all fights...')
    train_model.main(evaluate=full)

    if full:
        import backtest
        print('[+] Running the historical backtest report...')
        backtest.main()
    print('Done.')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--full', action='store_true', help='also rerun walk-forward evaluation and backtest')
    ap.add_argument('--check', action='store_true', help='only report how fresh the data is')
    ap.add_argument('--skip-download', action='store_true', help='rebuild from files already downloaded')
    args = ap.parse_args()
    if args.check:
        sys.exit(check())
    refresh(full=args.full, skip_download=args.skip_download)
