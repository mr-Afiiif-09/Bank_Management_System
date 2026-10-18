# 🏦 Bank Management System

A lightweight, web-based Bank Management System developed using **Python, Flask, HTML, CSS, and JSON-based file storage**. The application provides a simple interface for managing bank accounts, performing basic financial transactions, and monitoring account activity through a centralized dashboard.

Designed as a beginner-friendly Python project, it demonstrates core programming concepts, web application development, data persistence, and transaction validation.

## ✨ Features

- **Account Management** — Create and manage accounts with unique account numbers.
- **Account Overview** — View account details and search for specific accounts.
- **Deposit Funds** — Add money to an account with transaction validation.
- **Withdraw Funds** — Withdraw money while preventing negative amounts and insufficient-balance transactions.
- **Account Deletion** — Remove existing accounts from the system.
- **Dashboard Analytics** — View account statistics and total balances.
- **Transaction History** — Track recent deposits and withdrawals.
- **Persistent Storage** — Store account information and transaction records in JSON files.
- **Responsive User Interface** — Navigate account management features through a structured web dashboard.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Backend web framework |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive layout |
| JSON | File-based data storage |

## 📁 Project Structure

```text
Bank-Management-System/
│
├── app.py                 # Flask application and backend logic
├── bank.json              # Account data storage
├── transactions.json      # Transaction history
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
├── static/                # CSS and other static assets
└── README.md              # Project documentation
```

*Note: The structure above is illustrative. Adjust the filenames and folders to match your actual repository.*

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- pip package manager
- Git (optional)

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Bank-Management-System
```

Alternatively, download the repository as a ZIP file and extract it.

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Start the application

```powershell
python app.py
```

### 6. Open the application

Visit the following URL in your browser:

**http://127.0.0.1:5000**

The application should now be available locally.

## 💾 Data Storage

The application uses JSON files for basic data persistence:

- `bank.json` — Stores account information and balances.
- `transactions.json` — Stores recent transaction records, with a limit of up to 100 entries.

This storage approach keeps the project simple and suitable for learning. For multi-user applications or concurrent transactions, a database-backed design is recommended.

## 🔒 Security and Limitations

This project is intended for **educational and demonstration purposes only**. It is not suitable for real banking operations or production deployment.

The current implementation does not provide production-grade authentication, authorization, transaction integrity, or financial data protection.

Before deploying a real-world application, consider implementing:

- Secure authentication and role-based authorization.
- A relational database with atomic transactions.
- CSRF protection and input validation.
- Secure session management and secret-key configuration.
- Audit logging, backups, and appropriate data protection controls.
- A production-ready WSGI server and secure deployment configuration.

**Do not use real financial information or actual money with this application.**

## 🚀 Future Enhancements

- User authentication and account-specific dashboards.
- SQLite or PostgreSQL database integration.
- Downloadable transaction statements.
- Date-based transaction filtering.
- Improved error handling and automated testing.
- Charts and visualizations for account activity.

## 🎯 Learning Objectives

This project demonstrates practical applications of:

- Python functions, data structures, and exception handling.
- Flask routes and request handling.
- HTML forms and CSS-based interface design.
- JSON serialization and file handling.
- Input validation and transaction-related business rules.
- Organizing a small full-stack application.

## 👨‍💻 Author

Developed as a Python and Flask learning project to explore backend development, data management, and web application design.

---

⭐ If you find this project useful, consider starring the repository on GitHub.