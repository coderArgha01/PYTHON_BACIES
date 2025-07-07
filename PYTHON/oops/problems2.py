
#Define a Employee class with attributes role,department & salary .this class showdetails methods


class Employee():
    def __init__(self,role,dept,salary):
        self.role=role
        self.department=dept
        self.salary=salary
    def showdetails(self):
        print("role: ",self.role)
        print("department :",self.department)
        print("salary :",self.salary)    



           
e1=Employee("itr","ct","561")
e1.showdetails()           

