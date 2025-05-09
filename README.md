# ☕ Coffee Machine Simulator

A simple text-based coffee machine built with Python. It lets users choose between espresso, latte, or cappuccino — handling payments, resource tracking, and change calculation.

## 🔧 Features

- Select from 3 drinks: **Espresso**, **Latte**, **Cappuccino**
- Handles coin input and calculates change
- Checks if ingredients are enough before making a drink
- Gives feedback when resources are low or payment is insufficient
- Tracks current water, milk, coffee, and total money earned
- `report` and `off` commands to check status or shut down the machine

## 🛠 How It Works

- User is prompted to choose a drink
- The machine checks if there are enough ingredients
- If so, it asks the user to insert coins
- If the payment is enough, it dispenses the drink and updates resources
- Otherwise, it refunds the money and cancels the transaction

## 📋 Commands

- `espresso`, `latte`, `cappuccino`: Order a drink
- `report`: Print the remaining water, milk, coffee, and total money
- `off`: Shut down the machine

💡 You can manually edit the starting amounts of water, milk, and coffee by changing the `resources` dictionary at the top of the `main.py` file.

## 📁 Files

- `main.py`: Main Python script with all logic
  ↳ Edit the `resources` dictionary in this file to set initial amounts.
- `README.md`: This file

## 🧠 Learning Focus

This project helps practice:
- Conditional statements
- Loops
- Functions and parameters
- Dictionaries and data structures
- User input handling

---

## 📌 To Do / Future Improvements

- Add more drink options
- Save resource/money data between runs
- Add GUI or web version
- Handle invalid inputs

## 🧑‍💻 Author

Anton Valdez  
Software Developer 🚀  
[GitHub](https://github.com/antonvaldez) | [LinkedIn](https://www.linkedin.com/in/antonvaldez/)

---

> This is a learning project. Feel free to fork or suggest improvements!
