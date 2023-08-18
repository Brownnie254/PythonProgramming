# Intergrating MySQL database with Python
# Module: pymsql
import pymysql

# Create a database connection
# Use the function Connect with the parameters
# Connect(host='', user = '' ,password = ''(if access requires a password), database = '')

connection = pymysql.connect(host='localhost', user='root', password='Kifaru12345', database='MpesaTestDB')
print("Database connected successfully")


# 2. Inserting Data to the Tables


employee_name = "Mary D Mongo"
hire_date = '2023-07-04'
salary = 450000
dept_id = 7


# Cursors : A cursor is a propert(State) used to execute sql codes on python
# Prepared statements (%s):They indicate that values will be passed during sql execution

cursor = connection.cursor()


sql = "insert into employees (emp_name, hire_date, salary , dept_id) values (%s, %s, %s, %s)"


# 3. sql execution:
data = (employee_name, hire_date, salary, dept_id)
cursor.execute(sql, data)


# Commit

connection.commit()


print("Record  Saved Successfully")