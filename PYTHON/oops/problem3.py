

#Create a class called order which stores item & its prices
#use Dunder function __gt__()to convey that:
#order1>order2 if price of order1>price of order2


class order():
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(or1,or2): 
        return or1.price>or2.price

or1=order("chipes",50)
or2=order("tea",20)

print(or1>or2)