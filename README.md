## ATM Simulation System

This repository contains a modular Python-based **ATM Simulation System**. The project demonstrates fundamental programming concepts such as module organization, list manipulation, and user input validation within a financial application context.

---

### ## Key Features

* **Secure Access**: Users must provide a unique identity and a matching PIN to perform any actions.
* **Balance Inquiry**: Real-time checking of current account balances.
* **Deposit Functionality**: Users can add funds to their account, which updates their balance and transaction history.
* **Withdrawal System**: Secure cash withdrawal with built-in checks for insufficient funds.
* **Bank Statements**: A detailed log of all deposits and withdrawals made during the session.

---

### ## Project Structure

The system is broken down into several modules to ensure clean, maintainable code:

| File | Description |
| :--- | :--- |
| **`main.py`** | The entry point of the application containing the main menu loop. |
| **`accounts.py`** | Acts as the database, storing usernames, IDs, PINs, balances, and transaction logs. |
| **`balance.py`** | Contains the logic for viewing the current account balance. |
| **`deposit.py`** | Handles the logic for depositing money into a user's account. |
| **`withdraw.py`** | Manages the withdrawal process and balance verification. |
| **`transaction.py`** | Generates and displays the user's transaction history. |

---

### ## Getting Started

#### ### Prerequisites
* Python 3.x installed on your machine.

#### ### Execution
1.  Clone the repository or download the source files.
2.  Ensure all `.py` files are in the same directory.
3.  Run the application by executing the main file:
    ```bash
    python main.py
    ```

---

### ## How It Works

1.  **Identity Verification**: Upon selecting an option, the system prompts for a **Unique Identity**.
2.  **Authentication**: If the ID is valid, the system asks for a **PIN**.
3.  **Operations**: Once authenticated, you can withdraw, deposit, or view your statement.
4.  **Session Persistence**: Transactions and balance changes are tracked throughout the duration of the program execution.

---

### ## Future Improvements
* Implement data persistence using a real database or CSV files.
* Add a GUI (Graphical User Interface) using Tkinter or PyQt.
* Enhance security with encrypted PIN storage.
