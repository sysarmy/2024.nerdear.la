#!/bin/bash

# Get the directory of the script
SCRIPT_DIR=$(dirname "$0")

# Change to the parent directory
cd "$SCRIPT_DIR/.."


pybabel compile -d app/translations
