import os

print("--- SRE SMART MONITOR ACTIVE ---")

storage_data = os.popen("df -h $HOME").read()
print(f"Current Status:\n{storage_data}")

for line in storage_data.split('\n'):
    if '/data/data/com.termux' in line:
        columns = line.split()
        usage_pct = columns[4].replace('%', '')
        usage_int = int(usage_pct)

        print(f"\n[ANALYSIS]: Current Usage is at {usage_int}%")

        if usage_int >= 90:
            print("❌ CRITICAL: Storage is almost full! Immediate cleanup required.")
        elif usage_int >= 75:
            print("⚠️ WARNING: Storage usage is high. Monitor closely.")
        else:
            print("✅ HEALTHY: Storage levels are within normal limits.")

