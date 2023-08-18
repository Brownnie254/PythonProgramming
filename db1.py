#READ OPERATION (SELECT): Petrieving from The Database
import pymysql

#Step1. Database Connection
connection = pymysql.connect(host='localhost', user='root', password='Kifaru12345', database='MpesaTestDB')
print("Database connected successfully")

#Step2. Create a connection cursor
cursor = connection.cursor()

#Step3. Sql to read data 
sql = "select * from employees"


#Execute
cursor.execute(sql)

#Step4. Check whether  its empty(rowcount)
count = cursor.rowcount
print(count)

if count == 0:
    print("No Records Found")
else:
    data = cursor.fetchall()
    print(data)    

