# SRE System Monitor 🚀

A Python-based infrastructure health monitoring tool designed for real-time Linux system diagnostics and resource automation. 

## 🛠 Features
* **Storage Monitoring**: Provides detailed disk usage statistics using the df -h utility.
* **Automated Diagnostics**: Built-in logic to identify system paths and verify directory availability.
* **Resource Tracking**: Tracks total, used, and available disk space to prevent system downtime.
* **Linux Integration**: Seamlessly executes system-level commands via Python's os module.

## 📂 Project Structure
* SRE/: Core directory for Site Reliability Engineering scripts.
* monitor.py: The primary automation script for system health checks.

## 🚀 Getting Started
1. **Clone the repository**:
   git clone https://github.com/YOUR_USERNAME/sre-system-monitor.git
2. **Navigate to the directory**:
   cd sre-system-monitor/SRE
3. **Run the monitor**:
   python monitor.py

## 📊 Sample Output
Filesystem      Size  Used  Avail Use% Mounted on
/dev/block/dm-44 111G   87G    25G  78% /data/data/com.termux/files/home

## 🎯 Roadmap
- [ ] Implement automated alerting for high disk usage (>80%).
- [ ] Add memory (RAM) and CPU process tracking.
- [ ] Integrate logging to a history file for long-term diagnostics.
EOF

