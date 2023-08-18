#Tuples:()
#Properties : Ordered, duplicates allowed, immutable(unchangeable)
#Data from database to/form an application are enclosed on a tuple

counties = ("Nairobi", "Mombasa", "Kisumu",)
print(type(counties))
#Create  tuple with one item
#Print the typeS
towns =("Naivasha",)
print(type(towns))
newCounty = tuple("Naks")
print(type(newCounty))
#methods:
print(counties.index("Mombasa"))

newCounties = list(counties)
newCounties.append("Murang`a")

counties = tuple(newCounties)
print(counties)