print("1-->Addition  \n 2 --> Subtraction \n 3-->Multiplication ")
while True:
        choice=int(input("Enter Your Choice! e,g 1"))
        if choice == 1:
            number1 = int(input("Enter First Number?: "))
            number2 = int(input("Enter Second Number?: "))
            sum = number1 + number2
            print(f"{number1} + {number2} = {sum}") 



        elif choice == 2:
            number1 = int(input("Enter First Number?: "))
            number2 = int(input("Enter Second Number?: "))
            subtract = number1 - number2
            print(f"{number1} - {number2} = {subtract}") 

        elif choice == 0:
            break



        else:
            print("Coming Soon!!")


# keywords:
#Break : used to terminate a loop
#Continue : Skip an iteration
          
