import mysql.connector

def get_connection():
    """
    Establish and return a connection to the MySQL database.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mini",
            database="attendance_management",
            port=3306
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insert_bill(item_name, quantity, price, total):
    """
    Insert a new bill record into the bills table.
    """
    conn = get_connection()
    if conn is None:
        raise Exception("Database connection failed.")
    cursor = conn.cursor()
    query = "INSERT INTO bills (item_name, quantity, price, total) VALUES (%s, %s, %s, %s)"
    values = (item_name, quantity, price, total)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_all_bills():
    """
    Retrieve all bill records from the bills table.
    """
    conn = get_connection()
    if conn is None:
        raise Exception("Database connection failed.")
    cursor = conn.cursor()
    query = "SELECT item_name, quantity, price, total FROM bills"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records
