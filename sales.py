import mysql.connector
from datetime import datetime

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sales"
)

cursor = db.cursor()

# Function to add a new sales record
def add_sales_record(product_name, quantity, price_per_unit, sale_date):
    sql = "INSERT INTO SalesRecords (product_name, quantity, price_per_unit, sale_date) VALUES (%s, %s, %s, %s)"
    val = (product_name, quantity, price_per_unit, sale_date)
    cursor.execute(sql, val)
    db.commit()
    print(f"Sales record for {product_name} added successfully.")

# Function to view all sales records
def view_sales_records():
    cursor.execute("SELECT * FROM SalesRecords")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to update a sales record
def update_sales_record(id, product_name=None, quantity=None, price_per_unit=None, sale_date=None):
    sql = "UPDATE SalesRecords SET"
    params = []
    if product_name:
        sql += " product_name = %s,"
        params.append(product_name)
    if quantity:
        sql += " quantity = %s,"
        params.append(quantity)
    if price_per_unit:
        sql += " price_per_unit = %s,"
        params.append(price_per_unit)
    if sale_date:
        sql += " sale_date = %s,"
        params.append(sale_date)
    
    sql = sql.rstrip(",") + " WHERE id = %s"
    params.append(id)
    
    cursor.execute(sql, params)
    db.commit()
    print(f"Sales record ID {id} updated successfully.")

# Function to delete a sales record
def delete_sales_record(id):
    sql = "DELETE FROM SalesRecords WHERE id = %s"
    cursor.execute(sql, (id,))
    db.commit()
    print(f"Sales record ID {id} deleted successfully.")

# Main menu
def main():
    while True:
        print("\nSales Management System")
        print("1. Add Sales Record")
        print("2. View Sales Records")
        print("3. Update Sales Record")
        print("4. Delete Sales Record")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity sold: "))
            price_per_unit = float(input("Enter price per unit: "))
            sale_date = input("Enter sale date (YYYY-MM-DD): ")
            add_sales_record(product_name, quantity, price_per_unit, sale_date)
        
        elif choice == '2':
            view_sales_records()
        
        elif choice == '3':
            id = int(input("Enter sales record ID to update: "))
            print("Enter new details (leave blank to keep current):")
            product_name = input("New product name: ")
            quantity = input("New quantity: ")
            price_per_unit = input("New price per unit: ")
            sale_date = input("New sale date (YYYY-MM-DD): ")
            update_sales_record(id, product_name or None, quantity or None, price_per_unit or None, sale_date or None)
        
        elif choice == '4':
            id = int(input("Enter sales record ID to delete: "))
            delete_sales_record(id)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
1