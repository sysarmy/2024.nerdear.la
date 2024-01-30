#!/bin/bash

# Get the directory of the script
SCRIPT_DIR=$(dirname "$0")

# Change to the parent directory
cd "$SCRIPT_DIR/.."

# Check if the language parameter is provided
if [ $# -eq 1 ]; then
  language="$1"
else
  echo "Please provide a language parameter."
  exit 1
fi

# Generate the message.po in app/translations
pybabel init --no-wrap -i app/translations/messages.pot -d app/translations -l "$language"
