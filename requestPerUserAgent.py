from collections import defaultdict
import re

log_data = "./NodeJsApp.log"
with open(log_data, "r") as f:
    log_data = f.readlines()

user_agent_counts = defaultdict(int)

for line in log_data:
    match = re.search(r'"([^"]*)"$', line)
    if match:
        user_agent = match.group(1)
        user_agent_counts[user_agent] += 1

print("\nUser-Agent request counts:")
for agent, count in user_agent_counts.items():
    print(f"{agent}: {count}")
