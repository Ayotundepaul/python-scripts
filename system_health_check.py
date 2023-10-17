#!/usr/bin/env python3

import psutil

def get_system_health():
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
    print("Disk Usage:", psutil.disk_usage('/').percent, "%")
    
if __name__ == "__main__":
    get_system_health()
