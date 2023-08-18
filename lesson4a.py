#Dictionaries: Collection {}
#Properties of a Dictionary: Unordered , no duplicates , mutable(Changeable) -> Keys
#Key - value pair 


student1 = ["Joseph", 34 , "male" , False ,["Programming" , "SQL"]]
#With Lists data is accessed using indexing
student2 = {
    "name": "Joseph" ,
    "age": 34 ,
    "gender": "Male" ,
    "isPresent": False,
    "subjects":["Programming" , "SQL"],
    "scores" : {
        "programming" : 100,
        "sql" : 87 
    }

    }
print(type(student1))
print(type(student2))
#Operations
#1. printing dictionary
print(student2)

#2, Accessing items on a dictionary
#We use the key to access 
print(student2["age"])
#Access subjects from the dictionary
print(student2["subjects"])


#3. Updating values -> we use the key
student2["age"] = 35
print(student2)
#Update value "Programming" to "Programming in Python"
student2["subjects"][0] = "Programming in Python"
print(student2)

#4. Adding items to a dictionary
student2["email"] = "Joes@gmail.com"
print(student2)
print(student2)
# Nested Dictionary
print(student2["scores"]["sql"])

#Methods - functions 
print(student2.keys())
print(student2.values())


student2.clear()
print(student2)
 # API -Application Programming Interface
 # JSON - JavaScript Object Notation(Standard Data Format)