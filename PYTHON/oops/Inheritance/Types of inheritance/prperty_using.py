
class student:
    def __init__(self,phy,chem,bio):
        self.phy=phy
        self.chem=chem
        self.bio=bio
    @property
    def perchentage(self):
        return  str((self.phy+self.chem+self.bio)/3) +"%" 


stu1=student(78,82,98)
print(stu1.perchentage)       
        
stu1.bio = 87
print(stu1.perchentage)
