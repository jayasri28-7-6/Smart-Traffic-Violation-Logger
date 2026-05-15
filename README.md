# 🚦 Smart Traffic Violation Logger

A Python-based web application that helps traffic authorities manage and monitor traffic violations efficiently. The system allows users to add violations, generate QR codes, track payment status, and manage records using Flask and SQLite.

---

# 📌 Features

- 🚗 Add traffic violation records
- 🔍 Search vehicle records
- 📊 Dashboard showing total, paid, and unpaid violations
- 💳 Mark fines as paid
- 🗑️ Delete violation records
- 📷 Automatic QR code generation for each violation
- 🌐 Simple and interactive web interface

---

# 🛠️ Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- QRCode Library

---

# 📂 Project Structure

```bash
traffic_logger/
│── app.py
│── database.db
│── static/
│   ├── style.css
│   └── qr/
│── templates/
│   ├── index.html
│   ├── add_violation.html
│   └── status.html
│── README.md
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/your-username/traffic_logger.git
cd traffic_logger
```

---

## Install required packages

```bash
pip install flask flask_sqlalchemy qrcode pillow
```

---

# ▶️ How to Run

```bash
python app.py
```

---

# 🌐 Output

- Opens automatically in your browser
- Displays all traffic violation records
- Generates QR codes for each violation
- Allows searching, updating payment status, and deleting records

---

# 📊 Example Features

- View all violation records
- Search using vehicle number
- Generate QR code for payment tracking
- Monitor paid and unpaid fines
- Dashboard statistics display

---

# 🗃️ Database

This project uses SQLite database:

```bash
database.db
```

Main Table:

```sql
Violation
```

Fields:
- Vehicle Number
- Vehicle Type
- Violation
- Location
- Date
- Fine Amount
- Payment Status

---

# 🚀 Future Improvements

- 📈 Add charts and analytics dashboard
- 📧 Email/SMS fine notifications
- 🔐 Admin login authentication
- 🌍 Deploy online
- 🤖 AI-based vehicle number detection

---
