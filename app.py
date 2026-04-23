from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- USERS ----------------
users = {
    "1001": {"name": "Amit", "pin": "1234", "balance": 5000},
    "1002": {"name": "Rahul", "pin": "2345", "balance": 7200},
    "1003": {"name": "Sneha", "pin": "3456", "balance": 6500}
}


# ---------------- LOGIN PAGE ----------------
@app.route('/')
def home():
    return render_template("login.html")


# ---------------- LOGIN LOGIC ----------------
@app.route('/login', methods=['POST'])
def login():
    atm = request.form['atm']
    pin = request.form['pin']

    if atm in users and users[atm]["pin"] == pin:
        session['user_id'] = atm
        return redirect('/dashboard')
    else:
        return "❌ Invalid credentials"


# ---------------- DASHBOARD ----------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    user_id = session['user_id']
    user = users[user_id]
    message = ""

    if request.method == 'POST':
        action = request.form['action']

        try:
            amount = int(request.form.get('amount', 0))
        except:
            amount = 0

        if action == "deposit":
            if 0>= amount:
                user["balance"] -= amount
                message = "✅ Deposited Successfully"
            else:
                message = "❌ Invalid Amount"

        elif action == "withdraw":
            if user["balance"] >= amount:
                user["balance"] -= amount
                message = "✅ Withdrawal Successful"
            else:
                message = "❌ Insufficient Balance"

    return render_template("dashboard.html", user=user, message=message)


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
    
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- USERS ----------------
users = {
    "1001": {"name": "Amit", "pin": "1234", "balance": 5000},
    "1002": {"name": "Rahul", "pin": "2345", "balance": 7200},
    "1003": {"name": "Sneha", "pin": "3456", "balance": 6500}
}


# ---------------- LOGIN PAGE ----------------
@app.route('/')
def home():
    return render_template("login.html")


# ---------------- LOGIN LOGIC ----------------
@app.route('/login', methods=['POST'])
def login():
    atm = request.form['atm']
    pin = request.form['pin']

    if atm in users and users[atm]["pin"] == pin:
        session['user_id'] = atm
        return redirect('/dashboard')

    return render_template("login.html", error="Invalid ATM number or PIN")


# ---------------- DASHBOARD ----------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    user_id = session['user_id']
    user = users[user_id]
    message = ""

    if request.method == 'POST':
        action = request.form['action']

        try:
            amount = int(request.form.get('amount', 0))
        except ValueError:
            amount = 0

        if action == "deposit":
            if amount > 0:
                user["balance"] += amount
                message = "Deposited Successfully"
            else:
                message = "Invalid Amount"

        elif action == "withdraw":
            if amount > 0 and user["balance"] >= amount:
                user["balance"] -= amount
                message = "Withdrawal Successful"
            else:
                message = "Insufficient Balance"

    return render_template("dashboard.html", user=user, message=message)


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)