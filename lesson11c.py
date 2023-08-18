#Banking System
#Account
#Parent Class
class Bank:
    def __init__(self, usd_exchange_rate):
        self.usd_exchange_rate = usd_exchange_rate = usd_exchange_rate

    def usd_exchange_rate(self, currency,rate):
        rate = rate / currency
        print (f"Your New Rate is {rate}")

        

class Account(Bank) :
    def __init__(self, name, pin, balance , accno , branch , status):
        super().__init__(140)
        if balance <= 0 :
            print("Account Balance cannot be zero!")
        elif len(name) == 0:
            print("Please Enter Account Name!")
        elif len(accno) != 6:
            print("Invalid Account Number")

        else:
            self.name  = name
            self.pin = pin
            self.balance = balance
            self.accno = accno
            self.branch = branch
            self.status = status


    def withdraw (self):
        print("=====WELCOME TO WITHDRAW======= \n")
        pin = int(input("Please Enter PIN:  "))  
        if self.pin == self.pin:
            print("==ACCESS GRANTED==")
            amount = int(input("Enter The Amount:  "))
            if amount <= self.balance:
                print("Success!")
                print(f"You have withdrawn Kshs. {amount}")
                newBalance = self.balance - amount
                print(f"Your new Balance is Kshs. {newBalance}")

            else:
                print("Insufficient Account balance!!")
        else:
            print("Wrong PIN!!")
            print("Try Again!!")




    def check_balance(self):
        print("==WELCOME TO CHECK BALANCE==")
        pin = int(input("Please Enter PIN:  "))  
        if self.pin == self.pin:
            print("==ACCESS GRANTED==")
            balance = self.balance
            print(f"Your  Balance is Kshs. {balance}")
        else:
            print("Wrong PIN!!")
            print("Try Again!!")







account1 = Account("Modcom Institute",1234,15000,"123456","Westlands","Active")  
# account1.check_balance()   
account1.usd_exchange_rate(1000)      

#In OOP paradigm we follow some of its concepts 
#we have four concepts :
#1. Inheritance : a child class can inherit states and bbehaviours of a parent class
#2. Abstraction : it hides complexities of  a the program by implementing Interfaces 
#3. Enscapulation:Classes can hide their information from other classses 
#4. Polymorphism : A class can generate different  instances

#Method Overloading
#Method Overriding