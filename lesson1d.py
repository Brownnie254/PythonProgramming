#Create a program to perform simple interst taking inputs from the user
#Algorithm/pseudocode: Step by step procedure to perform a task
#Get the formula: (PxRxT)/100
#Get Principal: Amount DEposited
#Get Rate: 
#Time: in months or years
#Apply the formula above
#output your results
Principal = int(input("Enter the Amount DEposited?: "))
Rate = int(input("Enter the Rate?: "))
Time = int(input("Enter the Time: "))

Interest = (Principal * Rate * Time)/100
print(f"Your interest is Kshs. {Interest}")

#Body Mass Index (bmi)
#Create a program to calculate BMI
#Given the formular: weight/(height*height)
#Height = float(input("Enter the height"))

Weight = int(input("Enter the Weight?: "))
Height = float(input("Enter the Height?: "))

BMI= Weight / (Height * Height)
print(f"Your Body Mass Index is {BMI} ")
