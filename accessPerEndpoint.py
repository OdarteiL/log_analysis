from collections import defaultdict
import re

log_data = "./NodeJsApp.log"
with open(log_data, "r") as f:
    log_data = f.readlines()

endpoint_counts = defaultdict(int)

for line in log_data:
    match = re.search(r'"[A-Z]+ ([^ ]+)', line)
    if match:
        endpoint = match.group(1)
        endpoint_counts[endpoint] += 1

print("\nEndpoint access counts:")
for endpoint, count in endpoint_counts.items():
    print(f"{endpoint}: {count}")
