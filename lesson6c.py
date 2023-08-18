#Nested if conditions
#MOney Withdrawal Application


account ={
    "PIN" : "1234",
    "name": "Derrick",
    "balance" : 10000.00
}
print("===WELCOME TO ABC BANK===")

while True:
    pin = input("Enter Your PIN: ")
    if pin == account["PIN"]:
        print(f"===KARIBU {account['name']}===")
        print(f"Your current balance is Kshs. {account['balance']}")
        amount = int(input("Enter the amount to Withdraw: "))
        
        if amount <= account["balance"]:
            print(f"Confirmed , Withdraw Kshs. {amount}")
            newBalance = account["balance"]- amount
            print(f"Your New Balance is {newBalance}")
            print("=======CONTINUE WITH TRANSACTION?=======")

        else:
            print("Failed!!,Insufficient Account Balance")
            print(f"Your Balance is {account['balance']}")

    else:
        print("Wrong Pin, Try Again!!!!")        