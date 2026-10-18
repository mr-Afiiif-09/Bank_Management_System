# Bank Management System

A beginner-friendly web app built with Python, Flask, HTML, CSS, and JSON file storage.

## Features
- Create accounts with unique account numbers
- View and search accounts
- Deposit and withdraw money
- Prevent negative transactions and withdrawals above the available balance
- Delete accounts
- Dashboard totals and recent transaction history

## Run on Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Data files
`bank.json` stores account data. `transactions.json` stores up to 100 recent transactions.

## Important
This is an educational local demo, not a real banking system. It has no login, authorization, or production-grade transaction security. Do not use real customer information or real money. Before deployment, use secure authentication, a database with transactions, CSRF protection, and production server settings.
