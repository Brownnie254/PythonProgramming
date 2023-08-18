#SIMPLE LOGIN SYSTEM

user={
    "username": "user123",
    "password": "1234",
    "timeline1": {
        "username":"Biggie",

        "posted": "Live In Naivasha"

    },


    "timeline2": {
        "username":"Ranjoz",

        "posted": "coding"
    }

}
#User authentication
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
if username == user["username"] or password == user["password"]: 
    print("=====WELCOME TO FACEBOOK=====")

    print(user["timeline1"])
    print("=====================")
    print(user["timeline2"])
    print("=====================")
else:
    print("=====ACCESS DENIED======")
    print("====TRY AGAIN!!====")

#Task1:
# Attack(Hack) the system to grant access with only your username  
# #Task2:
# #Granted Access with both wrong credential



#Mpesa application
#Deposit
#Withdraw
#Change Pin
#Send Money
