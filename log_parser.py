import argparse
import re
import json
from collections import defaultdict

def parse_log(file_path):
    failed_logins = defaultdict(int)
    pattern = re.compile(r"Failed password for .* from ([\d\.]+)")

    with open(file_path, 'r', errors='ignore') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                failed_logins[ip] += 1

    return failed_logins

def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Log Parser for Failed SSH Logins")
    parser.add_argument('--path', required=True, help='Path to the log file')
    parser.add_argument('--output', default='reports/summary.json', help='Output file (JSON)')

    args = parser.parse_args()
    results = parse_log(args.path)
    
    print(f"\n🔍 Found {sum(results.values())} failed login attempts.")
    for ip, count in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(f"IP {ip}: {count} attempts")
    
    save_json(results, args.output)
    print(f"\n✅ Report saved to {args.output}")

if __name__ == "__main__":
    main()

