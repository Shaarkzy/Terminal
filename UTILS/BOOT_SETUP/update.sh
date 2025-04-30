#!/bin/bash

# Define paths
TARGET_DIR="$HOME/Shell"
TEMP_DIR="$HOME/Shell_temp"
REPO_URL="https://github.com/Shaarkzy/Shell"


# Clone the repo to a temporary directory
git clone "$REPO_URL" "$TEMP_DIR"

# Check if the clone was successful
if [ $? -eq 0 ]; then

    # If the main Shell directory exists, remove it
    if [ -d "$TARGET_DIR" ]; then
        rm -rf "$TARGET_DIR"
    fi

    # Rename temp folder to Shell
    mv "$TEMP_DIR" "$TARGET_DIR"
    echo -e "[*] Update Successful"
    version="$HOME/Shell/__version__"
    data=$(cat "$version")
    echo -e "[!]SOFTWARE UPDATED: VERSION: $data\n[!]PLEASE REFRESH YOUR TERMINAL"

else
    echo "[!]Update Failed"
    # Optionally remove the temp folder if it was created
    rm -rf "$TEMP_DIR"
fi
