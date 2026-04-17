# CF Scanner

> [English](./README.md) | [فارسی](./README_FA.md)

**cf-scanner** is a simple, human-friendly multi-threaded IP range scanner.
It quickly checks which hosts in a range are **alive** and whether their **HTTP (port 80)** and **HTTPS (port 443)** services are reachable, and shows everything in a clean, aligned terminal table.

---

## Features

- **ICMP ping to detect live hosts**
- **TCP port 80 (HTTP) and **TCP port 443** (HTTPS) checks**
- **Clean terminal table with proper row numbering (1, 2, 3, …)**
- **Saves live IPs to `actives.txt`**
- **Multi-threaded for faster scanning**
- **Includes a ready-made **`hosts.txt`** file with all Cloudflare IP ranges**
  → you can scan all Cloudflare IPs just by entering this file name

---

##  Author

>- **Author:** Matin
>- **Telegram-Channel:** [A Hunter](https://t.me/ahunter0)

---

## Project Structure (Overview)

```text
project/
├── scanner.py
├── hosts.txt          # Full Cloudflare IP ranges
└── modules/
    ├── __init__.py
    ├── banner.py
    ├── ip.py
    ├── ip_reader.py
    ├── ping_scanner.py
    ├── port_checker.py
    ├── domain_resolver.py
    ├── create_result.py
    ├── screen_display.py
    ├── scan_worker.py
    └── state_reporter.py
```

---

##  Requirements

- **Python 3.9+**
- **colorama** for colored terminal output:

```bash
pip install colorama
```

- OS: Tested on **Windows**, should work on any OS with Python and `ping`.

---

## Special: Scan All Cloudflare IPs

The project includes a **`hosts.txt`** file that contains **all Cloudflare IP ranges**.

To scan all Cloudflare IPs:

1. Make sure `hosts.txt` is in the same directory as `scanner.py`.
2. When the scanner asks for the range file name, simply type:

```text
hosts.txt
```

The scanner will go through all Cloudflare IPs from `hosts.txt` and:

- show the result in the table,
- save all live IPs into `actives.txt`.

---

## Insrtallaton: Using Git

This method is for when you host the code in a Git repository (GitHub, GitLab, etc.).

### 1. Clone the repository

```bash
git clone https://github.com/hu-matin/cf-scanner.git
cd cf-scanner
```

### 2. Install dependencies

If you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Prepare range files

**Option A – your own ranges**

Create a text file, e.g. `ranges.txt`, and put one range per line.
In this simple version, each line is assumed to be a `/24` block:

```text
3.25.205.0/24
10.0.0.0/24
```

**Option B – Cloudflare**

Just use the included **`hosts.txt`** file – no extra work needed.

### 4. Run the scanner

```bash
python scanner.py
```

Then:

- To scan your own ranges, enter: `ranges.txt`
- To scan Cloudflare IPs, enter: `hosts.txt`
- Choose thread count (e.g. 50, or press Enter for default)

Example output:

```text
[#]  IP address          PING   P80   P443  DOMAIN
────────────────────────────────────────────────────────
[ 1]  3.25.205.10        OK     OPEN  CLOSE example.com
[ 2]  3.25.205.11        FAIL   CLOSE CLOSE no-domain
...
```

All live hosts will also be saved in `actives.txt`.

---

## Method 2: Using ZIP (No Git Required)

If you received the project as a **ZIP file** (from Telegram, web, etc.):

### 1. Extract the ZIP

- Place the ZIP (e.g. `cf-scanner.zip`) somewhere (like Desktop)
- Right click → **Extract All...** (or use WinRAR / 7-Zip)
- Go into the extracted folder – you should see `cf-scanner.py`, `hosts.txt` and `modules/`.

### 2. Open CMD / PowerShell in that folder

On Windows:

- Click the path bar in Explorer, type `cmd`, press Enter
  or
- Shift + Right Click → **Open PowerShell window here**

### 3. Install dependencies

With `requirements.txt`:

```bash
pip install -r requirements.txt
```


### 4. Choose what to scan

- For your own IP ranges: create `ranges.txt` and add your ranges (one per line).
- For Cloudflare: simply use the provided `hosts.txt` as-is.

### 5. Run the scanner

```bash
python scanner.py
```

Then:

- For Cloudflare scan → enter: `hosts.txt`
- For your own ranges → enter: `ranges.txt` (or whatever filename you chose)
- Set thread count

You’ll see the live, ordered table in the terminal, and `actives.txt` will contain all responding hosts.

---

## Tips

- Want slower but more stable scans? **Use fewer threads** (e.g. 10).
- Need faster scans on a strong network? Increase the thread count, but watch your network load.
- You can reuse `actives.txt` as input for other tools or for further analysis.
- For a quick Cloudflare health check, just always use **`hosts.txt`** as the range file.

---

## 📬 Contact

For bugs, ideas, or contributions, feel free to reach out:

>- **Matin** – Telegram: [https://t.me/Hu_Matin](https://t.me/ahunter0)