
import sys
from collections import Counter

def parse_log(file_path):
    ip_list = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) > 0:
                    ip_list.append(parts[0])  # IP is usually the first column
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        sys.exit(1)

    # Count top 5 IPs
    counter = Counter(ip_list)
    print("\nTop 5 IPs making requests:\n")
    for ip, count in counter.most_common(5):
        print(f"{ip} => {count} requests")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_apache_nginx_logs.py access.log")
        sys.exit(1)

    log_file = sys.argv[1]
    parse_log(log_file)
