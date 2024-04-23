#!/bin/bash

# Define source and destination
SOURCE="/Volumes/fd/machine-learning"
DESTINATION="/Users/kaus/coding/"

# Use rsync to synchronize the directories
rsync -av --delete "$SOURCE" "$DESTINATION"
echo "Sync has completed. ꒰ ꒡◡꒡꒱"