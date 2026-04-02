
# Python Security Scripts

A growing collection of Python scripts built as part of my journey into Python in Cybersecurity. Each script focuses on a practical security concept while reinforcing core programming skills.

---

## Project Context

This is my **ongoing Python learning project**, developed to apply security concepts in code. It covers:

- **File I/O:** Reading and parsing structured data from text files and logs.
- **Data Structures:** Using sets and dictionaries for efficient lookups and counting.
- **Function Design:** Separating logic into focused, reusable functions.
- **GUI Development:** Building a desktop interface with Tkinter.
- **Security Logic:** Implementing real-world checks like blocklists, account lockouts, and log analysis.

---

## Scripts

### `mypass.py` — Password Strength Checker

A Tkinter desktop app that evaluates password strength in real-time.

**Features:**
- Validates complexity rules (length, uppercase, lowercase, numbers)
- Toggle between masked and plain text with a "Show Password" checkbox
- Color-coded feedback: **Green** for strong, **Red** for weak

**Run:**
```
python mypass.py
```

**Password criteria for a Strong rating:**
- At least 12 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number

---

### `ip_checker.py` — IP Blocklist Checker

Reads a list of IP addresses from `ips.txt` and checks each one against a hardcoded blocklist. Prints whether each IP is `BLOCKED` or `clean`.

**Run:**
```
python ip_checker.py
```

**Input file:** `ips.txt` — one IP address per line

---

### `ip_counter.py` — Access Log IP Frequency Counter

Parses a web server `access.log` file, counts how many times each IP address appears, and prints the top 3 most frequent IPs. Useful for spotting suspicious or high-volume sources.

**Run:**
```
python ip_counter.py
```

**Input file:** `access.log` — space-delimited log entries (timestamp, IP, method, path, status)

---

### `username_checker.py` — Locked Account Checker (v1)

Reads a list of usernames from `usernames_status.txt` and checks each one against `locked_accounts.txt`. Reports whether each account is locked or allowed.

**Run:**
```
python username_checker.py
```

---

### `username_checker_v2.py` — Locked Account Checker (v2)

A refactored version of `username_checker.py`. Breaks the logic into three focused functions:

- `load_locked_accounts(filepath)` — loads the locked account list into a set
- `check_username(username, locked_accounts)` — returns `True` if locked
- `report_result(username, result)` — prints the outcome

This version demonstrates how to separate concerns and make code easier to test and reuse.

**Run:**
```
python username_checker_v2.py
```

---

## Built With

- **Python 3.x**
- **Tkinter** — standard library GUI (used by `mypass.py` only)
- No external `pip` installations required

---

## Installation & Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Run any script directly:**
   ```
   python <script_name>.py
   ```

---

## Acknowledgments & Learning Process

- **AI Collaboration via Claude Code:** A key part of this project has been learning how to use **Claude Code** as a teaching tool rather than a shortcut. Instead of generating code for me, Claude Code guides me through problems — asking questions, explaining concepts, and letting me write the code myself. This approach has pushed me to think through logic independently, plan before I write, and understand *why* something works, not just *that* it works. The progression from `username_checker.py` to `username_checker_v2.py` is a direct result of that process: Claude Code challenged me to think about how to break the script into functions before touching the keyboard.
- **Lessons Learned:** Planning before writing code matters. Breaking a script into functions makes it easier to read, debug, and build on later. Learning to ask better questions of an AI tool is itself a skill — and one that translates directly into cybersecurity work.

*Developed as part of my journey into Python in Cybersecurity.*
