#!/usr/bin/env bash
# Installs a weekly macOS background job that refreshes the UFC data, rebuilds the
# features and refits the model every Monday at 09:00 (after Saturday's UFC event
# has been picked up by the UFCStats mirror on Sunday). If the Mac is asleep at
# that time, macOS runs the job when it wakes up.
#
#   bash scheduling/install_launchd.sh            # install / update the job
#   bash scheduling/install_launchd.sh --remove   # uninstall it
#
# Logs: logs/refresh.log in the project folder.
set -euo pipefail

LABEL="com.ufc-adversarial-judge.refresh"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON="$(command -v python3)"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl bootout "gui/$(id -u)" "$PLIST" 2>/dev/null || true
  rm -f "$PLIST"
  echo "Removed $LABEL"
  exit 0
fi

mkdir -p "$REPO/logs" "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>$PYTHON</string>
    <string>$REPO/scripts/update_data.py</string>
    <string>--full</string>
  </array>
  <key>WorkingDirectory</key><string>$REPO</string>
  <key>StartCalendarInterval</key>
  <dict><key>Weekday</key><integer>1</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer></dict>
  <key>StandardOutPath</key><string>$REPO/logs/refresh.log</string>
  <key>StandardErrorPath</key><string>$REPO/logs/refresh.log</string>
</dict>
</plist>
PLIST

launchctl bootout "gui/$(id -u)" "$PLIST" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "Installed $LABEL -> runs Mondays 09:00 using $PYTHON"
echo "Run it now with:  launchctl kickstart gui/$(id -u)/$LABEL"
