#!/usr/bin/env bash
# Compatibility wrapper. The real build is scripts/build.py, which emits an
# artifact per provider under dist/. This keeps the old two-file output working
# and drops copies at the paths earlier docs and scripts expected.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "$root/scripts/build.py" "$@"

if [[ -f "$root/dist/release/personal-voice.skill" ]]; then
  cp "$root/dist/release/personal-voice.skill" "$root/dist/personal-voice.skill"
  cp "$root/dist/release/personal-voice.zip" "$root/dist/personal-voice.zip"
  echo
  echo "Also copied to dist/personal-voice.skill and dist/personal-voice.zip"
  echo "Run scripts/build.py --list to see every provider target."
fi
