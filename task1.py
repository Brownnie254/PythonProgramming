#Electricity Bill Calculator
print("=======WELCOME======")
units = int(input("Enter Number Of Units: "))
if units<= 100:
    print("No Charge")

elif units>100 and units<= 200:
    price = (units)* 5
    print(price)

elif units>200:
    price = (units)* 10
    print(price)   

     

