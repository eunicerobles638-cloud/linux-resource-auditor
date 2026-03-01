import os
print("DevOps Monitoring Initialized...")
storage = os.popen("df -h /data/data/com.termux/files/home").read()
print(f"Current Status:\n{storage}")

