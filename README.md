
#  Local Network Device Scanner (Python TCP/IP)

A simple Python tool to scan a local IP range and identify devices that are alive by attempting TCP connections (default: port 80). Designed with OOP principles, socket programming, and unit testing support. Includes a Flask-based web dashboard for live monitoring.

---

##  Features

-  **TCP/IP Socket Scanning** using `socket.create_connection()`
-  **Object-Oriented Design** (`Scanner`, `ScanResult`)
-  **Unit Testing** with `unittest`
-  **Real-time Flask Dashboard**
-  Easily extendable for port scanning, CSV export, authentication

---

##  Project Structure

```bash
network_scanner/
├── scanner.py          # Core scanning logic using sockets
├── run.py              # CLI script to launch scan
├── utils.py            # IP utilities and logging
├── test_scanner.py     # Unit tests
├── dashboard/
│   ├── app.py          # Flask web app
│   └── templates/
│       └── index.html  # Dashboard UI
└── README.md           # You're reading it!
````

---

##  Requirements

* Python 3.6+
* Flask (`pip install flask`)

---

##  Usage

###  Clone the Repository

```bash
git clone https://github.com/kartik-mone/Local-Network-Device-Scanner-Python-TCP-IP-.git
cd Local-Network-Device-Scanner-Python-TCP-IP-
```

---

###  Edit IP Range (Optional)

In `run.py` or `dashboard/app.py`:

```python
BASE_IP = '192.168.1.'
START = 1
END = 10
```

---

###  Run the CLI Scanner

```bash
python run.py
```

**Sample Output:**

```
Scanning 192.168.1.1 to 192.168.1.10 on port 80...

[✔] 192.168.1.1 is alive (15.2 ms)
[✖] 192.168.1.2 is unreachable
...
```

---

###  Run the Flask Dashboard

```bash
python dashboard/app.py
```

Open your browser and go to: [http://localhost:5000](http://localhost:5000)

The dashboard shows:

* Live IPs in the subnet
* Port scanned
* Response time
* Auto-refresh every 10 seconds

---

###  Run Unit Tests

```bash
python test_scanner.py
```

---

##  Concepts Demonstrated

*  Python Sockets & TCP/IP fundamentals
*  Object-Oriented Programming (OOP)
*  Flask app integration
*  Frontend dashboard (HTML + CSS + JS)
*  Auto-refreshing status
*  Modular structure & clean code
*  Unit testing best practices

---

##  Preview

<img width="1919" height="959" alt="image" src="https://github.com/user-attachments/assets/30f7278b-51ef-4b2d-b64f-ab777e052e07" />

---

##  Author

**Kartik Mone**
*Python Developer*

[LinkedIn](https://www.linkedin.com/in/kartik-mone) • [GitHub](https://github.com/kartik-mone)

