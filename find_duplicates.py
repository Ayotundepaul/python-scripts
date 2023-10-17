#!/usr/bin/env python3

import os
import hashlib
import sys

def find_duplicates(directory):
    seen = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'rb') as f:
                filehash = hashlib.md5(f.read()).hexdigest()
                if filehash in seen:
                    duplicates.append((filepath, seen[filehash]))
                else:
                    seen[filehash] = filepath

    return duplicates

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 find_duplicates.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    duplicates = find_duplicates(directory)

    if duplicates:
        for dup, orig in duplicates:
            print(f"Duplicate: {dup} (Original: {orig})")
    else:
        print("No duplicates found.")
