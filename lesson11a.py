#OPP : is style (paragigm) of programming where everything(real-world entities) is treated as an object e,g a car, person, road
#Object: Real world entity that has states (properties) and behaviours(methods)
#States : Things that the object posses
#Methods: Things that the object can do.

#Object: Instance of a class
#Instantiation: process of creating objects from a class


#E,g Account: States(Balance,status,name,pin) then Methods(Withdraw , Deposit, Change PIN)
#Students :States(Name, Course,Gender) Methods(Learn, Exam.......)
#Class: Blueprint(template) of an object because it will define properties and methods of an object
#Class shirt : properties(color, price, size), methods(Purchase(), change price())
#Shirt1(red, 300, XL) Changeprice(250)
#Shirt2(black, 1500, M) Changeprice(1800)


#Class: Designs how squares look like

class Square:
    def __init__(self, width ,height):
        self.width = width
        self.height = height

    def area(self):
        area_square = -self.width * self.height
        print(f"The Area is {area_square}")

    def perimeter(self):
        perimeter_square = (self.width + self.height)*2
        print(f"Perimeter is {perimeter_square}")   




#Objects : Treated as variables
square1 =Square(5,5)
square1.area()
square1.perimeter() 


square2 = Square(10,10)
square2.area()
square2.perimeter()


name = "bob"
print(type(name))

name.capitalize()

list1 = ["Bob", "Sally", ]
list1.append("Brown")
print(list1)