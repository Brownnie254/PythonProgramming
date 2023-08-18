#USSD: Accessible by short codes e,g *444#

#Withdrawal Function:

customer = {
    "pin": 2024,
    "name": "Brown mark",
    "balance": 15000,
    "status": "active",
    "phone": "+254702480881"
}
while True:
    def withdraw(pin, amount, agent_no):
        print("===WELCOME===")
        if pin == customer["pin"]:
            print("==ACCESS GRANTED==")
            if amount <= customer["balance"]:
                print(f"Confirmed. Successfully withdrawn Kshs. {amount} from Agent No.  {agent_no}")
                balance = customer["balance"] - amount
                print(f"Your Balance is  {balance}")
                print("Thank You!!")
            else:
                print("Insufficient Account Balance!")   
        else:
            print("===ACCESS DENIED===")
            print("Wrong PIN!!")

    #Deposit
    def deposit(pin,amount, agent_no):
        print("===WELCOME TO DEPOSIT===")
        if customer["status"] == "active":
            if pin == customer["pin"]:
                print("===ACCESS GRANTED===")
                print("PLEASE WAIT.......")
                current_balance = amount + customer["balance"]
                print(f"Thank you for Depositing At agent_no {agent_no}")
                print(f"Your Current balance is  {current_balance}")
            else:
                print("=====ACCESS DENIED=====") 
                print("WRONG PIN!!")
        else:
            ("====Sorry! Please Activate Your Account====")  



    #check balance
    def check_balance(pin):
        if customer["status"] == "active":
            if pin == customer["pin"]:
                print(f"Confirmed Your Current Balance is {customer['balance']}") 
            else:
                print("ACCESS DENIED")
                print("Wrong PIN!!")
        else:
            ("====Sorry! Please Activate Your Account====")

    # CHANGE PIN



    def change_pin(current_pin, new_pin, confirm_new):
        if customer["status"] == "active":
            if current_pin == customer["pin"]:
                if new_pin == confirm_new:
                    customer["pin"] == confirm_new
                    print("PIN updated successfully")
                    print(f"Your new PIN is {customer['pin']}")
                else:
                    print("PIN dont match")    
                    print("Try Again!!")
            else:
                print("PIN dont match")    
                print("Try Again!!")
        else:
            print("======Account Not Active.======")        


    def Menu():
        print("SIMPLE M-PESA USSD APP")
        print("===WELCOME===")
        print("\n")
        print("1. Withdraw ")
        print("2. Deposit ")
        print("3. Check Balance ")
        print("4. Change PIN")
        print("5. Loans -and Savings ")
        print("6. Fuliza Mpesa")
        print("0. Exit ")
        print(" ")


        option = int(input("Please Enter Your Choice?: "))
        if option == 1:
            withdraw( int(input("Enter Your PIN: ")), int(input("Enter Amount: ")), int(input("Enter Agent_No: ")))

        elif option == 2:
            deposit( int(input("Enter Your PIN: ")), int(input("Enter Amount: ")), int(input("Enter Agent_No: ")))    

            
         
        elif option == 3:
            check_balance(int(input("Enter Your PIN: "))) 
        elif option == 4:
            change_pin( int(input("Enter Your Current  PIN: ")), int(input("Enter New PIN: ")), int(input("Confirm Your New PIN: ")))

        print("Other options Development")   


    Menu()    
    