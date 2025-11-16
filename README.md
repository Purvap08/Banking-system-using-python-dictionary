# Banking-system-using-python-dictionary
🏦 Banking System Using Python Dictionary

A simple and beginner-friendly Banking System implemented in Python, using a dictionary to store and manage account information.
This project demonstrates core Python concepts such as functions, file handling, conditional logic, and CRUD operations, making it ideal for students and new Python learners.

📌 Features

Create a new bank account

Deposit money

Withdraw money

Check account balance

View all account details

Data is stored using a Python dictionary

Supports saving & loading data through a text file (accinfo.txt)

🛠️ Technologies Used

Python 3

Dictionary Data Structure

JSON for serialization

Basic File Handling

📁 Project Structure
├── accinfo.txt      # Stores account data in JSON format
├── main.py          # Main program logic
└── README.md        # Project documentation

▶️ How It Works

Each account is stored as a key–value pair in a dictionary.

The account number is the key.

Account details (name, balance, etc.) are stored as the value.

Data is loaded from accinfo.txt when the program starts.

All updates are saved automatically.

📖 Example Dictionary Structure
bank = {
    "101": {"name": "Purva", "balance": 5000},
    "102": {"name": "Yash", "balance": 8000}
}

🚀 How to Run
python main.py


Make sure accinfo.txt exists in the same directory.
If not, the program will create it automatically.

🎯 Learning Outcomes

Understanding Python dictionaries

Using JSON to store structured data

File reading/writing

Building a menu-driven CLI application

Applying functions and modular programming

📌 Future Enhancements

Add password protection for each account

Implement transaction history

Create a GUI using Tkinter

Add CSV or database support
