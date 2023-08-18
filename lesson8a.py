#Functions :  a  block of code that performs a specific task on the system tha only executes when it is called (refferenced)
#Mpesa USSD applications e,g Send Money, Deposit, Withdraw , Check Balance , Change Pin,
#Types of functions:
#Inbuilt Fuctions: Already existing on the project , e,g Print(), Input(), Range(),
#User-specific(Defined): Created by a developer, then call them when needed. e,g Send_Sms(), encrypt(),Mpesa()

#Defining a function:
#def function_name():
#      code block



def greet():
    print("Hello, Welcome to Functions")

#Calling a function
# function_name() : Exit the function and call


greet()     

def add():
    number1 = int(input("Enter First Number: "))
    number2 = int(input("Enter Second Number: "))
    sum = number1 + number2
    print(sum)
# add()  
print("==================================")



#add
#create a function to perfom simple interest
def Simple_interest():
    Principal = int(input("Enter the Amount Deposited?: "))
    Rate = int(input("Enter the Rate?: "))
    Time = int(input("Enter the Time: "))

    Interest = (Principal * Rate * Time)/100
    print(f"Your interest is Kshs. {Interest}")
Simple_interest()
