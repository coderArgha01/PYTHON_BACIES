

students={
    "name" : "Argha Mondal" ,
    "Subjects" :{                # nested dictonary
        "phy" : 97,
        "che" : 88,
        "math" :82
    },
    "Age" : 24
}


print(students.update({"Roll" : 2251179}))
print(students)  
print(list(students))   

print(list(students.keys()))       #using dict.keys()
print(list(students.values()))     #using dict.values()
print(len(list(students)))

print(str(students["Subjects"]["math"]))