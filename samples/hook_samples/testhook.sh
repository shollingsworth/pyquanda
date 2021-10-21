#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

filename="${1?"filename"}"
cat "${filename}" >> /tmp/testlog.log
echo >> /tmp/testlog.log
