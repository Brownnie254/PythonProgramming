#Create a list of 5 numbers
#Create a variable and assign it zero
#Iterate over the list and return the largest number from the list

numbers =[10, 20, 30, 16, 9, 100]
counter = 0

for number in numbers:
    if counter < number:
        counter = number


print(counter)

#Get the smallest number
#Hint: counter should have the largest number

numbers =[10, 20, 30, 16, 9, 100]
counter = 100

for number in numbers:
    if counter > number:
        counter = number


print(counter)