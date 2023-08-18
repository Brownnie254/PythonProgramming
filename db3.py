# DELETE
import pymysql


# Step1. Database Connection
connection = pymysql.connect(
    host='localhost', user='root', password='Kifaru12345', database='MpesaTestDB')
print("Database connected successfully")

# Cursor

cursor = connection.cursor()

# data
emp_id = 5


sql = "delete from employees where emp_id = %s"

cursor.execute(sql, emp_id)
connection.commit()
print(f"Record {emp_id} deleted successfully.")
