# 💳 ATM Flask App

A simple web-based ATM simulation built using **Python** and **Flask**.
This project demonstrates basic banking operations like login, deposit, and withdrawal in a clean web interface.
https://atm-flask-project.onrender.com/
---

## 🚀 Features

* 🔐 Login using ATM number and PIN
* 💰 Deposit money
* 💸 Withdraw money with balance validation
* 🔄 Session-based authentication (login/logout)

---

## ⚠️ Limitations

* 📊 Transaction history (mini statement) is **not yet implemented**
* 💾 Data is stored in memory (resets when server restarts)
* 🔒 No password encryption (for learning/demo purposes only)

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Templating Engine:** Jinja2

---

## 📁 Project Structure

```
atm-flask-app/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    ├── login.html
    └── dashboard.html
```

---

## ▶️ How to Run Locally

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/atm-flask-app.git
cd atm-flask-app
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Application

```
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔑 Demo Login Credentials

| ATM Number | PIN  |
| ---------- | ---- |
| 1001       | 1234 |
| 1002       | 2345 |
| 1003       | 3456 |

---

## 🎯 Purpose of the Project

This project is designed for **learning and practice**.
It helps beginners understand:

* Flask routing and request handling
* Form submission (GET/POST)
* Session management
* Basic backend logic for financial operations

---

## 🔮 Future Improvements

* 📊 Add transaction history (mini statement)
* 🗄️ Integrate SQLite/MySQL database
* 🔐 Implement password hashing (security)
* 🎨 Improve UI using Bootstrap or Tailwind
* 🌐 Deploy on cloud platforms (Render / Vercel / Railway)

---

## ⚠️ Disclaimer

This is a **simulation project only** and not intended for real financial use.
Do not use real banking data or credentials.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
