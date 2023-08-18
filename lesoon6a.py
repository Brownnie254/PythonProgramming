number = 21
if number % 7 == 0:
    print(f"{number} is Divisible by 7")
else:
    print(f"{number} is not Divisible by 7")

#If--Else If--Else
#Grading System:



#Equal to 40 -> E
#Equal to 50 -> D
#Equal to 60 -> C
#Equal to 70 -> B
#Equal to 80 -> A

print("=====WELCOME=====")
score = int(input("Enter Your Score: "))
if score == 40:
    print("Grade E")
elif score == 50:
    print("Grade D")
elif score == 60:
    print("Grade C")  
elif score == 70:
    print("Grade B") 
elif score == 80:
    print("Grade A") 
else:
    print("Invalid Score!!")
    print("Try Again")            
         