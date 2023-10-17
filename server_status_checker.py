#!/usr/bin/env python3

import subprocess
import sys

def check_server_status(servers):
    for server in servers:
        response = subprocess.call(["ping", "-c", "1", server])
        if response == 0:
            print(f"{server} is up!")
        else:
            print(f"{server} is down!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 server_status_checker.py <server1> <server2> ...")
        sys.exit(1)

    servers = sys.argv[1:]
    check_server_status(servers)
