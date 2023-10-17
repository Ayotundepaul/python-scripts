#!/usr/bin/env python3

from collections import Counter
import sys

def analyze_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    error_counts = Counter(line for line in lines if 'ERROR' in line)
    
    for error, count in error_counts.most_common():
        print(f"{error.strip()}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer.py <log_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_log(file_path)
