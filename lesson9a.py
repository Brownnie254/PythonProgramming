#Modules/Librabries
#A module is a python file containing python functions that can be called on another python file.
#Inside file: lesson9a we create some functions
#Inside file: lesson9b we will call the functions from lesson9a file
#Therefore lesson lesson9a is a module.

#Create 3 functions :

def add(num1,num2):
    sum = num1 + num2
    print(f"Answer is {sum}")



def multiply(num1,num2):
    product = num1 * num2
    print(f"Answer is {product}")


def subtract(num1,num2):
    subtract = num1 - num2
    print(f"Answer is {subtract}") 




def division(num1,num2):
    division = num1 / num2
    print(f"Answer is {division}")