import shutil
import psutil
import os

def check_system_health():
    total, used, free = shutil.disk_usage("/")
    disk_percent = (used / total) * 100
    ram_percent = psutil.virtual_memory().percent
    
    print(f"--- SYSTEM REPORT ---")
    print(f"Disk Usage: {disk_percent:.2f}%")
    print(f"RAM Usage: {ram_percent:.2f}%")
    
    if disk_percent > 90 or ram_percent > 90:
        print("ALERT: CRITICAL STATUS!")
        os.system('termux-notification --title "SRE ALERT" --content "Critical Resource Usage! Disk: {:.2f}% RAM: {:.2f}%" --priority high'.format(disk_percent, ram_percent))
    else:
        print("Status: HEALTHY ✅")

if __name__ == "__main__":
    check_system_health()

