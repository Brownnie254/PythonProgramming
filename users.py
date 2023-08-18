# Intergrating MySQL database with Python
# Module: pymsql
import pymysql

# Create a database connection
# Use the function Connect with the parameters
# Connect(host='', user = '' ,password = ''(if access requires a password), database = '')

connection = pymysql.connect(host='localhost', user='root', password='Kifaru12345', database='MpesaTestDB')
print("Database connected successfully")


# 2. Inserting Data to the Tables

username = "Brownnie254"
password = '123456'
phone = '0702480881'


# Cursors : A cursor is a propert(State) used to execute sql codes on python
# Prepared statements (%s):They indicate that values will be passed during sql execution

cursor = connection.cursor()


sql = "insert into user (username, password, phone) values (%s, %s, %s)"


# 3. sql execution:
data = (username, password, phone)
cursor.execute(sql, data)


# Commit



username = "Toma Tech"
password = '000000'
phone = '0732584589'

cursor = connection.cursor()
sql = "insert into user (username, password, phone) values (%s, %s, %s)"
data = (username, password, phone)
cursor.execute(sql, data)


connection.commit()

username = "Andrew Tate"
password = 'qwerty123'
phone = '0774859632'

cursor = connection.cursor()
sql = "insert into user (username, password, phone) values (%s, %s, %s)"
data = (username, password, phone)
cursor.execute(sql, data)


connection.commit()


username = "Edh Malik"
password = '789456123'
phone = '0775489623'

cursor = connection.cursor()
sql = "insert into user (username, password, phone) values (%s, %s, %s)"
data = (username, password, phone)
cursor.execute(sql, data)


connection.commit()


print("Record  Saved Successfully")



#SELECTS : Log In, Ecommerce.......
#UPDATE
#DELETE

#FLASK : python framework to run web application