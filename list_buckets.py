#!/usr/bin/env python3

import json
import subprocess

result = subprocess.run(["aws", "s3api", "list-buckets", "--query", "Buckets[].Name"], capture_output=True, text=True)
buckets = json.loads(result.stdout)
print(json.dumps({"buckets": buckets}))
