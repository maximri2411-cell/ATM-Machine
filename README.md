🏦 Passover ATM Project
Welcome to our Passover ATM Simulation! This project was developed as a teamwork challenge during the holiday, combining logic, data management, and a sleek GUI.

👥 The Team
Alex (Alexdv25)
Maxim (maximri2411-cell)

🚀 Overview
This application simulates a real-life ATM experience. Users can manage their bank accounts, perform transactions, and view their history, while an administrative layer allows for system-wide account management.

📂 Project Structure
main.py – Entry Point: The heart of the app. Run this file to launch the application.
models.py – Business Logic: Defines the Bank and Accounts classes, including PIN hashing and transaction logic.
ui.py – User Interface: A full GUI built with tkinter, featuring custom themes and responsive layouts.
storage.py – Data Management: Handles persistent storage using JSON to ensure your data stays safe even after closing the app.
terminal_lab.py – Development labs used for testing new features and logic before integration.

✨ Key Features
Secure Login: PIN-based authentication with SHA-256 hashing.
Transactions: Withdraw, Deposit, and Transfer funds between accounts.
Live History: A detailed, scrollable transaction log for every account.
Admin Panel: Special access for managing users and system status.
Data Persistence: All actions are saved in real-time to a JSON database.

🛠 Installation & Running
Make sure you have Python 3.x installed.
Install dependencies: pip install -r requirements.txt
Run the app: python main.py
Tip: Feel free to explore the code, and if you have any feedback, don't be shy to contact us! Happy Passover!