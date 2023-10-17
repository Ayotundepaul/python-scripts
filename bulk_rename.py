#!/usr/bin/env python3

import os
import sys
import re

def bulk_rename(directory, pattern, replacement):
    for filename in os.listdir(directory):
        new_filename = re.sub(pattern, replacement, filename)
        if filename != new_filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 bulk_rename.py <directory> <pattern> <replacement>")
        sys.exit(1)

    directory = sys.argv[1]
    pattern = sys.argv[2]
    replacement = sys.argv[3]

    bulk_rename(directory, pattern, replacement)
