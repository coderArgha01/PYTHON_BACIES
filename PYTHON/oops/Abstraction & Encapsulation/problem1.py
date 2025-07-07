

#create Account class with 2 attributes balance & account no .create methods for debit,credit & printin the balance

class account :
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no=account_no
    def debit(self,amount):
        self.balance -=amount
        print("rs",amount,"was debited")
        print("total balance :",self.get_balance)
    def credit(self,amount):
        self.balance +=amount
        print("rs",amount,"was credited")
        print("total balance :",self.get_balance)
    def get_balance(self):
        return self.balance    

acc1=account(12000,789)
print(acc1.account_no)
acc1.debit(2000)
acc1.credit(3000)

del acc1()

