from datetime import datetime, timedelta
from collections import defaultdict

# Replace with your actual log data as a multiline string
log_file_path = "./NodeJsApp.log"
with open(log_file_path, "r") as f:
    log_data = f.readlines()

ip_requests = defaultdict(list)

for line in log_data:
    parts = line.split()
    timestamp = datetime.fromisoformat(parts[0].replace("Z", "+00:00"))
    ip = parts[1]
    ip_requests[ip].append(timestamp)

print("Requests within 10s window after first request:")
for ip, times in ip_requests.items():
    times.sort()
    window_end = times[0] + timedelta(seconds=10)
    count = sum(1 for t in times if times[0] < t <= window_end)
    print(f"{ip}: {count} requests")
