#BOOLEANS


isApproved = False
print(type(isApproved))

isAbsent = True


#Booleans with comparison Operators
#We have the following : >, <, ==,>= ,<= ,!
#comparison operators : used to compare one variable and another

print(10>6)
# passwordSaved ='12345678'
# passwordRequested = input("Enter Your Password: ")

# print(passwordSaved == passwordRequested )

#Logical Operators : Compare relationship btn one condition and another
#and : returns True when BOTH conditions are true
#or: ATLEAST ONE condition is true


username = 'admin'
password = '12345678'

usernameRequested = input("Enter Username: ")
passwordRequested = input("Enter Your Password: ")

print(username == usernameRequested and password == passwordRequested)