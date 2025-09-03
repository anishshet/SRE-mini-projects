# 📊 Log Analysis Tool

A Python script that analyzes Apache/Nginx access logs to identify the top IP addresses making requests to your server.

## 🚀 What This Tool Does

This script reads web server log files and:
- ✅ Extracts IP addresses from each log entry
- ✅ Counts how many requests each IP made
- ✅ Shows you the **top 5 most active IPs**
- ✅ Handles errors gracefully (missing files, etc.)

---

## 📖 Code Breakdown & Explanation

### 🔧 **Imports Section**
```python
import sys
from collections import Counter
```

**→ `sys`** → lets you handle command-line arguments (`sys.argv`) and exit the script if something goes wrong.

**→ `Counter`** → a special class from Python's collections module. It counts how many times each item appears in a list (like a frequency counter).

---

### 🎯 **Main Function Definition**
```python
def parse_log(file_path):
    ip_list = []
```

**→ Defines a function `parse_log`** that takes a file path (`file_path`) as input.

**→ We create an empty list `ip_list`** to store all IP addresses we find in the log.

---

### 📂 **File Reading & IP Extraction**
```python
try:
    with open(file_path, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) > 0:
                ip_list.append(parts[0])  # IP is usually the first column
```

**→ `with open(file_path, "r") as f:`** → Opens the log file in read mode. `with` makes sure the file closes automatically.

**→ `for line in f:`** → Loops through each line in the file.

**→ `parts = line.split()`** → Splits the line into words (by spaces). In logs, the first column is usually the IP.

**→ `if len(parts) > 0:`** → Just a safety check in case the line is empty.

**→ `ip_list.append(parts[0])`** → Adds the first item (the IP) into `ip_list`.

---

### ⚠️ **Error Handling**
```python
except FileNotFoundError:
    print(f"Error: File {file_path} not found")
    sys.exit(1)
```

👉 **If the file doesn't exist**, it prints an error and exits with code 1 (non-zero means "error").

---

### 📈 **Counting & Display Logic**
```python
# Count top 5 IPs
counter = Counter(ip_list)
print("\nTop 5 IPs making requests:\n")
for ip, count in counter.most_common(5):
    print(f"{ip} => {count} requests")
```

**→ `counter = Counter(ip_list)`** → counts how many times each IP appeared.

**→ `counter.most_common(5)`** → gets the top 5 most frequent IPs.

**→ Loops through them and prints:**
```
192.168.1.10 => 320 requests
10.0.0.15 => 280 requests
203.0.113.45 => 156 requests
```

---

### 🎬 **Script Entry Point**
```python
if __name__ == "__main__":
```

👉 **Standard Python check:**
- Means "only run the below code if this file is executed directly, not imported as a module."

---

### 🔍 **Command-Line Argument Validation**
```python
if len(sys.argv) != 2:
    print("Usage: python parse_apache_nginx_logs.py access.log")
    sys.exit(1)
```

**→ `sys.argv`** → list of command-line arguments.

**Example:**
```bash
python parse_apache_nginx_logs.py access.log
```
- `sys.argv[0]` = `parse_apache_nginx_logs.py`
- `sys.argv[1]` = `access.log`

👉 **If no log file is passed**, it shows usage instructions and exits.

---

### 🏃 **Script Execution**
```python
log_file = sys.argv[1]
parse_log(log_file)
```

👉 **Takes the second argument** (log file path) and passes it into `parse_log`.

---

## 🛠️ Usage

### **Basic Usage:**
```bash
python parse_apache_nginx_logs.py access.log
```

### **Example Output:**
```
Top 5 IPs making requests:

192.168.1.10 => 1,247 requests
203.0.113.45 => 892 requests
10.0.0.25 => 634 requests
172.16.0.100 => 521 requests
198.51.100.30 => 445 requests
```

---

## 📋 Requirements

- **Python 3.x** (uses built-in modules only)
- **Log file** in standard Apache/Nginx format

---

## 📝 Supported Log Formats

This script works with standard web server logs where **IP address is the first field**:

### **Apache Common Log Format:**
```
127.0.0.1 - - [25/Dec/2023:10:00:00 +0000] "GET / HTTP/1.1" 200 1024
```

### **Nginx Access Log:**
```
192.168.1.100 - - [25/Dec/2023:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 2048
```

---

## 🚨 Error Handling

The script handles common errors:

- **File not found** → Shows clear error message and exits
- **Empty lines** → Safely skips them
- **Malformed entries** → Ignores lines without proper format

---

## 🎯 Use Cases

- **Security Analysis** → Identify potential attackers or bots
- **Traffic Monitoring** → See which IPs generate the most traffic  
- **Performance Debugging** → Find heavy users affecting server performance
- **Access Auditing** → Monitor who's accessing your server

---

## 🔧 Customization Ideas

Want to extend this script? Here are some ideas:

- Change the **top N** count (currently 5)
- Extract **additional fields** (user agents, status codes, etc.)
- Add **date filtering** for specific time ranges
- Export results to **CSV/JSON** format
- Add **IP geolocation** lookup

---

## 📊 Example Real-World Scenario

```bash
# Analyze yesterday's Apache logs
python parse_apache_nginx_logs.py /var/log/apache2/access.log

# Check Nginx logs for suspicious activity  
python parse_apache_nginx_logs.py /var/log/nginx/access.log
```

**Perfect for SRE tasks like:**
- Incident response and forensics
- Capacity planning and traffic analysis  
- Security monitoring and threat detection
- Performance optimization insights
