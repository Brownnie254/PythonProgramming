#For loop in a sequence(Collection)
#Collection: string , list, tuples, dictionaries

language = "Python"
for letter in language:
    print(letter)

print("============")
#list sequence
#loops with conditions


proLanguages = ["Python","C", "Java","JavaScript","C#"]
for language in proLanguages:
    if language == "Java":
        print("Java Exists")

    print(language)


#Assumption:
#1. create a list of 8 counties in kenya
#2. create 2 empty lists namely :single , double

#Task:
#Iterate through the list of 8 counties checking whether it has either single name or double name 
#If it has single name append to single empty list, otherwise append to double empty lists

counties = ["Nairobi" , "Taita Taveta", "Garrisa", "Uasin Gishu", "Nakuru", "Homa Bay","Murang`a","Kakamega"]

double = []
single = []


for county in counties:
    if " " in county:
        double.append(county)
    else:
        single.append(county)
print(double)
print(single)  



# Others methods 