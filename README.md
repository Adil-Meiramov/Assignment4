# Telegram Bot – Financial Planner

A simple Telegram bot for managing personal finances, built with `python-telegram-bot`.  
It allows users to set budgets, log expenses and income, and view a real-time financial summary — all within Telegram.

---

## Setup Instructions

1. **Clone the project** or download the source files.

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the environment**:
   - On Windows PowerShell:
     ```bash
     Set-ExecutionPolicy RemoteSigned -Scope Process -Force
     .\venv\Scripts\Activate.ps1
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set your Telegram bot token**:
   Open `main.py` and replace the placeholder with your token:
   ```python
   TOKEN = "YOUR_BOT_TOKEN_HERE"
   ```

6. **Run the bot**:
   ```bash
   python main.py
   ```

---

## Features

-  `/start` — Welcomes the user and shows basic usage
-  `/help` — Displays all available commands
-  `/config <category> <budget>` — Set a monthly budget per category
-  `/log <category> <+/-amount>` — Record an expense (negative) or income (positive)
-  `/summary` — View total balance and budget breakdown
-  `/notifyon` & `/notifyoff` — Enable or disable future notifications (placeholder)
-   Saves data persistently to `budget_data.json`

---

## File Structure

```
financial_planner_bot/
│
├── main.py              # Entry point for bot setup and command registration
├── handlers.py          # Logic for handling all commands
├── budget_data.json     # Stores user budget and logs (automatically created)
├── requirements.txt     # Project dependencies
├── .gitignore           # Excludes venv, pycache, and data files from Git
├── README.md            # Project documentation (this file)
└── screenshots/         # Folder with screenshots of bot in action
```

---

## Screenshots
![start](screenshots/image-1.png)
![budget](screenshots/image-2.png)
---

## Author

Created by a student for university Assignment 4.1 – Telegram Bot – Financial Planner  
Powered by Python + Telegram API