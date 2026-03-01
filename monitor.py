import os

print("--- SRE SMART MONITOR ACTIVE ---")

storage_data = os.popen("df -h $HOME").read()
print(f"Current Status\n{storage data}")

storage_data.split('\n'):
    if '/data/data/com.termux'
        colums = line.split()
        usage_pct = colums[4].replace('%', '')
        usage_int = int(usage_pct)

        print(f"\n[ANALYSIS]: Current Usage is at {usage_int}%")

        if usage_int >= 90:
            print("❌ CRITICAL: Storage is almost full! Immediate cleanup required.")
        elif usage_int >= 75:
            print("⚠️ WARNING: Storage usage is high. Monitor closely.")
        else:
            print("✅ HEALTHY: Storage levels are within normal limits.")
