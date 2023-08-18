#Data Types
#Specify the format(type) of data stored on a variable e,g number, letter collection.....
#Specify the operations done on that variable
#In python mostly used data types are: 
#Integers(Int): are numeric values without decimal, e,g age
#Floatin points (floats): Numbers with decimal places e,g distance, height, speed...
#Strings (str): Sequence of character enclosed inside either a double or single quotes e,g name, course, gender
#Booleans (bool): A value having only two instances e,g True or False
#Collections (Arrays): list, tuple, dictionary, sets
#type()

#Escape sequence : used to introduce speacial characters inside a string, \n(breaking in a new line)


message = "i love programming"
print(type(message))


weather ='It\'s a Chilly Morning'
print(weather)
paragraph = 'This is the first line ,\n This is the second line'
print(paragraph)

firstMessage = "I love "
secondMessage = "Python"

#Concatenation - merge strings
 
wholeMessage = firstMessage + secondMessage
print(wholeMessage)

#len(): Returns the number of characters in a string
password = input("Enter Your Password")
print(len(password))