#Error Handling/Exception Handling......
#Handling errors created by the users to avoid system from crashing
#We use try, except block
#try: houses a code that might generate an error from the user
#except/catch: where the error is handled before the system crashes

# while True:
#     try:
#         number = int(input("Enter a digit?: "))
#         print(f"You Have entered {number}")
#     except:
#         print("Please enter a valid input.....")    


while True:
    try:
        num1 = int(input("Enter first Number: "))
        num2 = int(input("Enter second Number: "))
        division = num1/num2
        print(division)
    except:
        print("You cannot have a zero division")    



#Types of exeptions in python (Research on this Brown!!!!!!1)   
# Object Oriented Programming .......
# Classes
# Properties
# Methods     
