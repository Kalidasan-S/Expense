# Expense Tracker

A comprehensive web application built with Django that allows users to manage their personal finances by tracking expenses and income (salary).

## Features

- **User Authentication:** Secure login and registration system.
- **Dashboard:** Interactive overview of your financial data with charts.
- **Expense Management:** Add, edit, and keep a detailed list of your expenses.
- **Income Tracking:** Add salary and alternate income to maintain an accurate balance.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kalidasan-S/Expense.git
   ```

2. **Activate your Virtual Environment:**
   ```bash
   # If you use the 'expense' folder as your python environment:
   expense\Scripts\activate
   ```

3. **Run Migrations:**
   *(Navigate to the folder containing `manage.py`)*
   ```bash
   cd expense/expense_tracker
   python manage.py migrate
   ```

4. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://localhost:8000/` in your browser to start tracking your expenses!

## Built With
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite3
