#If--Else If--Else
#Grading System:



#Between 0-40 -> E
#Between 41-50 -> D
#Between 51-60 -> C
#Between 61-70 -> B
#Between 71-100 -> A

print("=====WELCOME=====")
score = int(input("Enter Your Score: "))
if score >= 0 and score <=40 :
    print("Grade E")



elif score >40 and score <=50 :
    print("Grade D")



elif score >50 and score <=60 :
    print("Grade C")



elif score > 60 and score <=70 :
    print("Grade B")



elif score >70 and score <=100 :
    print("Grade A")

else:
    print("Invalid Score!!")
    print("Try Again")            
         