#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output="${1:-$root/dist/personal-voice.skill}"

mkdir -p "$(dirname "$output")"
rm -f "$output"

(
  cd "$root"
  zip -r "$output" SKILL.md references/
)

echo "Created $output"
