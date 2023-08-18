#UPDATE : Moidify an already existing record
import pymysql



#Step1. Database Connection
connection = pymysql.connect(host='localhost', user='root', password='Kifaru12345', database='MpesaTestDB')
print("Database connected successfully")

#Cursor

cursor = connection.cursor()


#data 
salary = 800000
emp_id = 6

#sql
sql = "update employees set salary = %s where emp_id = %s"

#Execution 
data = (salary, emp_id)
cursor.execute(sql, data)
connection.commit()

#notify user
print(f"Employee ID {emp_id}  salary updated successfully with {salary}")


