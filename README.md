# Linux Resource Auditor 📊
A simple monitoring tool I built to check how my system is doing. It tracks CPU load, RAM, and Disk space in one go.

I created this to automate the boring stuff like manual typing of `free -h` or `df -h` every time I want to check my server's health.

### What it checks:
* **CPU Load:** Shows the average load for the last 1, 5, and 15 minutes.
* **Memory (RAM):** Displays how much RAM is being used versus the total available.
* **Disk Status:** Monitors the main partition and shows available space.

### How to use:
1. **Clone the repo:**
   `git clone https://github.com/YOUR_USERNAME/linux-resource-auditor.git`
2. **Go to the folder:**
   `cd linux-resource-auditor`
3. **Run the script:**
   `python monitor.py`

### Sample Output:
```text
==========================================
      LINUX RESOURCE AUDITOR v2.0
      Infrastructure Health Check
==========================================
[+] CPU LOAD (1, 5, 15 min): ['0.12', '0.08', '0.05']

[+] MEMORY USAGE: Used: 1.2G / Total: 8.0G

[+] SYSTEM STORAGE: Available: 45G (Usage: 12%)
==========================================

