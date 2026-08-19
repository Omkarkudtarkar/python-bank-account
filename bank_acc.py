
class Account():
    def __init__(self,bal,acc_no ):
        self.balance= bal
        self.acc_no = acc_no

    def debit(self,amount):
        self.balance -= amount 
        print("Rs.", amount,"debited") 
        print("total balance =",self.get_balance())

    def credit (self,amount):
        self.balance += amount 
        print("Rs.", amount,"credited") 
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(4500,1236)
acc1.debit(500)
acc1.credit(8000)
