#!/bin/bash

# Define the subdomain variable
subdomain="2024.nerdear.la"

# Get the directory of the script
SCRIPT_DIR=$(dirname "$0")

# Change to the parent directory
cd "$SCRIPT_DIR/.."

# Replace href="/ with href="/$subdomain/, and the same with src for images
find app/build/ -type f -name "*.html" -exec sed -i "s#href=\"/#href=\"/$subdomain/#g" {} +
find app/build/ -type f -name "*.html" -exec sed -i "s#src=\"/#src=\"/$subdomain/#g" {} +
