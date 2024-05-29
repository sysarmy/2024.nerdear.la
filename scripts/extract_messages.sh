#!/bin/bash

# Get the directory of the script
SCRIPT_DIR=$(dirname "$0")

# Change to the parent directory
cd "$SCRIPT_DIR/.."

# Run pybabel extract
pybabel extract --no-wrap -F scripts/babel.cfg -k _l -o app/translations/messages.pot .
