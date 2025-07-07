
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

car1=toyota("fortune")
print(car1.color)
                