#Read all data from users table
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='Kifaru12345', database='MpesaTestDB')
print("Database connected successfully")


cursor = connection.cursor()

sql = "select * from user"

cursor.execute(sql)


count = cursor.rowcount
print(count)

if count == 0:
    print("No Records Found")
else:
    data = cursor.fetchall()
    print(data)  