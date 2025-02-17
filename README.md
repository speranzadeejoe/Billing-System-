# Billing-System-
---

# Billing System

A simple billing system built with **Tkinter** for the graphical user interface and **MySQL Workbench** for database management. This project demonstrates how to add items to a bill, calculate totals, store the data in a MySQL database, and retrieve past records.

## Features

- **Add Items:** Input item name, quantity, and price.
- **Calculate Total:** Automatically computes the total bill.
- **Database Integration:** Stores and fetches bill data using MySQL.
- **Simple and Easy-to-Use:** Clean interface built using Tkinter.

## Prerequisites

- **Python 3.x**
- **MySQL Server** with MySQL Workbench (or any MySQL client)
- Python packages:
  - `mysql-connector-python`
  - `tkinter` (usually comes with Python standard library)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/billing-system.git
   cd billing-system
   ```

2. **Install Required Packages**

   ```bash
   pip install mysql-connector-python
   ```

## Database Setup

1. Open **MySQL Workbench** (or your preferred MySQL client).
2. Execute the following SQL script to create the database and table:

   ```sql
   CREATE DATABASE IF NOT EXISTS attendance_management;
   USE attendance_management;

   CREATE TABLE IF NOT EXISTS bills (
       id INT AUTO_INCREMENT PRIMARY KEY,
       item_name VARCHAR(100),
       quantity INT,
       price FLOAT,
       total FLOAT
   );
   ```

3. **Note:**  
   The database connection details are specified in `db.py`:
   - **Host:** localhost
   - **User:** root
   - **Password:** mini
   - **Database:** attendance_management
   - **Port:** 3306

   Adjust these values if necessary.

## Project Structure

```
billing-system/
│
├── main.py       # Tkinter UI implementation
├── db.py         # Database connection and operations
└── README.md     # Project documentation
```

## Running the Application

1. **Ensure MySQL Server is running** on your machine.
2. **Run the main application:**

   ```bash
   python main.py
   ```

3. The application window will open where you can add items, see your bill, and fetch records from the database.

## Troubleshooting

- **Database Connection Error:**  
  Ensure your MySQL server is running and the credentials in `db.py` are correct.

- **Invalid Input:**  
  Make sure to provide valid numbers for quantity and price.

- **Module Import Issues:**  
  Ensure that both `main.py` and `db.py` are in the same directory.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Built using **Tkinter** for the UI.
- **MySQL Connector/Python** for database operations.

---

Feel free to customize the README as needed for your project. Enjoy coding!
