# Control Flow : A way to control program execution
#Three categories:
#1. Sequential control Flow : Default codes executed line by line (no identation)

#2. Conditional Control Flow : Codes are executed based on some criterias/ condtions
#3. Iterative control flow : Codes are executed a number of times based on some conditions


#CONDITIONAL:
#WE have 3 conditions , if, else, else if (elif), nested if

# IF: One condition is checked if condition return True if statement is executed
# Conditions/expression: checked return boolean (True, False)
#Statements :Code that is executed when condition is either True or False


age = 18
if age >= 18:
    print("ISSUED WITH ID")



#IF ELSE: One condition is checked, if condition return True ifstatement is executed, otherwise else statement is executed.   


age = 17
if age >= 18:
    print("ISSUED WITH ID")
    
else:
    print("PLEASE TRY NEXT TIME!!")

#Applying the idea of modulus(%) and conditions
#Write a program to test whethr a number is even (divide by 2) or odd
#Request the number from the user
number = int(input("Enter The Number: "))
if number % 2 == 0: 
    print("Even Number!!!")
else:
    print("Odd Nummber!!")