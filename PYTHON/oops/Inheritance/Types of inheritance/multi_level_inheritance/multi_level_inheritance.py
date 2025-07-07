

class   car:
    color = "blue"
    @staticmethod
    def start():
        print("car start")
    def stop():
        print("car stop")    
class toyota(car):
    def __init__(self,name):
        self.name=name

class fortune(toyota):
    def __init__(self, type):
        self.type=type

car1=fortune("desel")
print(car1.type)
print(car1.color)
        