

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")    
    def __add__(num1,num2):
        newreal=num1.real+num2.real
        newimg=num1.img+num2.img
        return complex(newreal,newimg)
            
num1=complex(4,5)
num1.shownumber()

num2=complex(8,10)
num2.shownumber()

num3=num1+num2
num3.shownumber()