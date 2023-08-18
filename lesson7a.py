#Python loops : is used to repeat a code a number of times based on a condition 
# message 100 times
# print("Hello")
# print("Hello")

#In python : for , while 
#Kotlin : for, while, do-while
#In JS: for , while , forEach()

#For loop:
#Syntax: for variable in sequence(collection) 
#            statements


#For Loop in Range() : Check the condition

for message in range(10):
    print(f"Hello {message}")

# print the first  20 numbers
# for i


print("======================")
for index in range(21):
    print(index)

#Range function with starting point
print("================")
for index in range(5, 21):
    print(index)

#Range function with increament/ decreament


print("================")
for index in range(10, 110, 10):
    print(index)

# Summarize :
# #Default : range (starting 0, limit , increament 1)
# Modified : range (start, limit , interval/decreament(-interval))


print("=================")
#print numbers from 100 to 60 , with interval of 10
for index in range(100,50,-10):
    print(index)

