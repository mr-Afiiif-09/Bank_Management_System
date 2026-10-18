import json, os
from datetime import datetime
from decimal import Decimal, InvalidOperation
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "local-demo-change-this-key")
DATA_FILE = "bank.json"
TXN_FILE = "transactions.json"

def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def accounts():
    return load(DATA_FILE)

def transactions():
    return load(TXN_FILE)

def find_account(number):
    return next((a for a in accounts() if str(a.get("Acc_no")) == str(number)), None)

def money(value):
    try:
        amount = Decimal(value)
        return amount if amount.is_finite() and amount >= 0 else None
    except (InvalidOperation, TypeError):
        return None

@app.route("/")
def index():
    all_accounts = accounts()
    txns = transactions()
    q = request.args.get("q", "").strip()
    shown = [a for a in all_accounts if q.lower() in str(a.get("Name", "")).lower() or q in str(a.get("Acc_no", ""))] if q else all_accounts
    total = sum(float(a.get("Balance", 0)) for a in all_accounts)
    deposits = sum(float(t["amount"]) for t in txns if t["type"] == "Deposit")
    withdrawals = sum(float(t["amount"]) for t in txns if t["type"] == "Withdrawal")
    return render_template("index.html", accounts=shown, all_accounts=all_accounts, transactions=txns[:6], total=total, deposits=deposits, withdrawals=withdrawals, q=q)

@app.route("/create", methods=["POST"])
def create():
    number = request.form.get("account_no", "").strip()
    name = request.form.get("name", "").strip()
    balance = money(request.form.get("balance", ""))
    if not number.isdigit():
        flash("Account number must contain digits only.", "error")
    elif not name:
        flash("Account holder name is required.", "error")
    elif balance is None:
        flash("Enter a valid non-negative opening balance.", "error")
    elif find_account(number):
        flash("That account number already exists.", "error")
    else:
        data = accounts()
        data.append({"Acc_no": int(number), "Name": name, "Balance": float(balance)})
        save(DATA_FILE, data)
        flash("Account created successfully.", "success")
    return redirect(url_for("index"))

@app.route("/transaction/<kind>", methods=["POST"])
def transaction(kind):
    if kind not in ("deposit", "withdraw"):
        flash("Invalid transaction type.", "error")
        return redirect(url_for("index"))
    number = request.form.get("account_no", "").strip()
    amount = money(request.form.get("amount", ""))
    data = accounts()
    account = next((a for a in data if str(a.get("Acc_no")) == number), None)
    if not account:
        flash("Account not found.", "error")
    elif amount is None or amount <= 0:
        flash("Enter an amount greater than zero.", "error")
    else:
        balance = Decimal(str(account.get("Balance", 0)))
        if kind == "withdraw" and balance < amount:
            flash("Insufficient balance. Withdrawal was not made.", "error")
        else:
            balance = balance + amount if kind == "deposit" else balance - amount
            account["Balance"] = float(balance)
            save(DATA_FILE, data)
            txns = transactions()
            txns.insert(0, {"account_no": number, "name": account["Name"], "type": "Deposit" if kind == "deposit" else "Withdrawal", "amount": float(amount), "created_at": datetime.now().strftime("%d %b %Y, %I:%M %p")})
            save(TXN_FILE, txns[:100])
            flash("Transaction completed successfully.", "success")
    return redirect(url_for("index"))

@app.route("/delete/<number>", methods=["POST"])
def delete(number):
    data = accounts()
    updated = [a for a in data if str(a.get("Acc_no")) != str(number)]
    if len(updated) == len(data):
        flash("Account not found.", "error")
    else:
        save(DATA_FILE, updated)
        flash("Account deleted.", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    if not os.path.exists(DATA_FILE): save(DATA_FILE, [])
    if not os.path.exists(TXN_FILE): save(TXN_FILE, [])
    app.run(debug=True)
