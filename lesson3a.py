#Collections(Arrays): groupps of data on the same variable
#We have:
#List:[]
#Tuple:()
#Dictionary : {}
#Sets : {}
student1 = "Bob"
student2 = "Jane"
student3 = "Sally"

students = ["Bob", "Jane", "Sally" ]
#Lists: stores data in collection using a square bracket, each comma separated
#Properties: Ordered, mutable(changeable),allow duplicate data


counties = [" Nakuru", "Kajiado", "Mombasa", "Nairobi", "Bomet","Kisumu"]
student =["Sally",23 ,False, 3.57]
print(type(counties))
#List Operations
#1. printing elements of a list
print(counties)
#2. Accessing items on a list
#Ordered: Indexing -> Items are given numeric values starting from zero
# [0]
print(counties[0])
print(counties[3])
#3. Range of values (:)
#The first index included, but the last index is excluded
print(counties[1:])
print(counties[:3])
print(counties[1:3])
print(counties[1:5])
#4.List methods
# a) Add a new item to the list -> append()
counties.append("Nyandarua")
print(counties)
newCounties = ["Kilifi","Eldoret", "Garissa"]
counties.extend(newCounties)
print(counties)

#append and extend ,add items to the end of the list
# insert (0,""):
counties.insert(1, "Kwale")
print(counties)
#b) Removing item from a list
counties.pop()
print(counties)

counties.remove("Nyandarua")
print(counties)
counties[2:2] = ["Migori" ,"Taita"]
print(counties)
print(len(counties))


counties.clear()
print(counties)

print(counties.count("Kwale"))

print(counties)

