import tkinter as tk
from tkinter import ttk, messagebox
import db  # Import our database functions

# Initialize main window
root = tk.Tk()
root.title("Billing System")
root.geometry("600x400")

# List to keep track of items for the current session
items = []

def add_item():
    """
    Add an item to the bill, update the list view and store it in the database.
    """
    item_name = item_entry.get().strip()
    if not item_name:
        messagebox.showerror("Input Error", "Item name cannot be empty!")
        return

    try:
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for quantity and price.")
        return

    total_price = quantity * price
    items.append((item_name, quantity, price, total_price))
    bill_list.insert("", "end", values=(item_name, quantity, price, total_price))

    try:
        db.insert_bill(item_name, quantity, price, total_price)
    except Exception as e:
        messagebox.showerror("Database Error", f"Error inserting data: {e}")

    calculate_total()

def calculate_total():
    """
    Calculate and display the total amount for the current session.
    """
    total_amount = sum(item[3] for item in items)
    total_label.config(text=f"Total: ₹{total_amount:.2f}")

def fetch_bills():
    """
    Retrieve all bills from the database and display them in the list.
    """
    bill_list.delete(*bill_list.get_children())
    try:
        records = db.fetch_all_bills()
        for row in records:
            bill_list.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Database Error", f"Error fetching data: {e}")

# UI Components
tk.Label(root, text="Item Name").grid(row=0, column=0, padx=10, pady=10, sticky="w")
item_entry = tk.Entry(root)
item_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Quantity").grid(row=1, column=0, padx=10, pady=10, sticky="w")
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Price").grid(row=2, column=0, padx=10, pady=10, sticky="w")
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Add Item", command=add_item).grid(row=3, column=0, columnspan=2, pady=10)

# Table to display bill items
columns = ("Item", "Quantity", "Price", "Total")
bill_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    bill_list.heading(col, text=col)
bill_list.grid(row=4, column=0, columnspan=2, pady=10)

# Label to show total bill amount
total_label = tk.Label(root, text="Total: ₹0.00", font=("Arial", 14, "bold"))
total_label.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(root, text="Fetch Bills", command=fetch_bills).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
