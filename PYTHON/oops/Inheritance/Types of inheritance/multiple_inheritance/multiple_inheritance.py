

class A():
   valA= " i am in class A"
class B():
    valB=print("i am class  B")
class C(A,B):
   valC= print(" i am class C")


class1=C
print(class1.valA)