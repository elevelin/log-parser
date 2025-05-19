# 🔍 Log Parser & Alert System (Python)

A lightweight Python tool that scans log files for security-relevant patterns (e.g. failed SSH logins), summarizes results on the console, and exports JSON or CSV reports. Easily extendable to other log types (Apache, Nginx, systemd) and alert mechanisms.

---

## 🚀 Features

- **Failed SSH login detection** (default)  
- **Top offending IPs** by failure count  
- **Console summary** of total and per-IP counts  
- **JSON** report output (`reports/summary.json` by default)  
- **Extensible** — add your own regex patterns or log formats  
- **No secrets** included; uses only standard Python libraries  

---

## 🛠️ Requirements

- Python 3.6+  
- No external dependencies  

(Optional, for CSV export)  
```bash
pip3 install pandas
📦 Setup & Installation
Clone the repo

bash
Copy code
git clone https://github.com/elevelin/log-parser.git
cd log-parser
(Optional) Create a virtual environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies (only if adding CSV export)

bash
Copy code
pip3 install pandas
▶️ Usage
Parse a sample log
bash
Copy code
python3 log_parser.py --path sample.log
Parse a real log file
bash
Copy code
python3 log_parser.py --path /var/log/auth.log
Specify a custom output path
bash
Copy code
python3 log_parser.py --path sample.log --output reports/my_report.json
📁 Directory Structure
perl
Copy code
log-parser/
├── log_parser.py    # Main script
├── sample.log       # Example log for testing
├── reports/         # JSON report(s) saved here
├── logs/            # (Ignored) any raw logs you drop here
├── README.md
└── .gitignore       # Excludes logs/ and reports/
🔧 Extending the Tool
Add new patterns

Open log_parser.py

Add a new re.compile(...) and counter in parse_log()

Export to CSV

python
Copy code
import pandas as pd
df = pd.DataFrame.from_dict(results, orient="index", columns=["count"])
df.to_csv("reports/summary.csv")
Integrate alerts

Print warnings on threshold breaches

Hook into Slack/email using requests or yagmail

🎯 Purpose & Benefits
Security Awareness: Quickly spot brute-force or repeated errors

Scripting Skills: Demonstrates Python CLI scripting & regex

Portfolio-Ready: No secrets, easy to review, clear output


