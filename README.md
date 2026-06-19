# Dapper Finanças - Python CLI System

**Dapper Finanças** is a command-line financial management application built in Python. This project was developed to practice core programming concepts, including data persistence, user authentication, and transaction logic.

## 🚀 Main Features

- **User Authentication:** A secure login system that validates users against a database, featuring a 3-attempt security lockout.
- **Account Registration:** Allows new users to create accounts with custom credit limits.
- **Transaction Engine:** 
  - **Outflow (Purchases):** Register purchases by category and automatically update the current invoice.
  - **Inflow (Income):** Track and add deposits to the user's total income.
- **Credit Logic:** Real-time validation of available credit; the system automatically denies transactions that exceed the user's limit.
- **Financial Reporting:** A summary view of total Inflows, Outflows, and the current net Balance.
- **Persistent Storage:** All data is saved in a `dados_usuarios.csv` file, ensuring information is kept after the program is closed.

## 🛠️ Technical Overview

- **Language:** Python 3.x
- **Data Format:** CSV (using `;` as a delimiter for easy spreadsheet integration).
- **Safety Features:** 
  - Uses the `with` statement for reliable file handling.
  - Implements `try-except` blocks to handle invalid numeric inputs.
  - Prevents duplicate usernames during registration.

## 💻 How to Use

1. Clone this repository.
2. Ensure you have Python installed on your machine.
3. Run the main file:
   ```bash
   python main.py
