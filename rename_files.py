#!/usr/bin/env python3

import os
import sys

def rename_files(directory, prefix):
    for filename in os.listdir(directory):
        os.rename(os.path.join(directory, filename), os.path.join(directory, prefix + filename))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 rename_files.py <directory> <prefix>")
        sys.exit(1)

    directory = sys.argv[1]
    prefix = sys.argv[2]

    rename_files(directory, prefix)
