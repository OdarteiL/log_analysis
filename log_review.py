from datetime import datetime, timedelta
from collections import defaultdict, Counter
import re

# Log data (read from file)
with open("NodeJsApp.log", "r") as f:
    log_data = f.read()

# Regex pattern
pattern = re.compile(r'^(.*?) (\d+\.\d+\.\d+\.\d+).+?"\w+ (/[^ ]*)[^"]*" \d+ - .*?"([^"]+)"$')

# Data containers
ip_requests = defaultdict(list)
user_agents = Counter()
endpoints = Counter()

# Parse logs
for line in log_data.strip().split("\n"):
    match = pattern.match(line)
    if match:
        timestamp_str, ip, endpoint, user_agent = match.groups()
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        ip_requests[ip].append(timestamp)
        user_agents[user_agent] += 1
        endpoints[endpoint] += 1

# Question 1: Count how many requests were made within 10 seconds after the first request by each IP
requests_within_10s = {}
for ip, times in ip_requests.items():
    times.sort()
    first_time = times[0]
    count = sum(1 for t in times if first_time < t <= first_time + timedelta(seconds=10))
    requests_within_10s[ip] = count

# Final output
print("1. Requests made within 10 seconds after the first request by each IP:")
for ip, count in requests_within_10s.items():
    print(f"   {ip}: {count} requests")

print("\n2. Count of requests by User-Agent:")
for agent, count in user_agents.items():
    print(f"   {agent}: {count} requests")

print("\n3. Count of each endpoint accessed:")
for endpoint, count in endpoints.items():
    print(f"   {endpoint}: {count} requests")
