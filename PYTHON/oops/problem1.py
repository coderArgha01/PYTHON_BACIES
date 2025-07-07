
#Define a circle class to create a circle with radius r using the constructor.
#Define an Area()method of the class which calculates the area of the circle.
#Define a Perimeter() method of the class which allows you to calculator the perimeter of the circle



class circle():
    def __init__(self,r):
        self.redious=r
    def Area(self):
        self.area=3.14*(self.redious**2)
        print("Area of the circle is :",self.area)
    def Perimeter(self):
        self.Perimeter=2*3.14*(self.redious)
        print("perimeter of the circle is :",self.Perimeter)

circle1=circle(5)
circle1.Area()
circle1.Perimeter()
