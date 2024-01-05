class Account:

  def __init__(self,owner,balance=0):
    self.owner = owner
    self.balance = balance
  
  def deposit(self,dep_amt): 
    self += dep_amt
    print("Added {} to the balance".format(dep_amt))

  def withdrawal(self,wd_amt):

    if self.balance >= wd_amt:
      self.balance -= wd_amt
      print("Withdrawal accepted!!!")
    else:
      print("Sorry not enough funds!!!")

  def __str__(self):
    return "Owner : {} \n Balance: {}".format(self.owner,self.balance)


a = Account("Sam",500)
a.balance
print(a)
a.deposit(100)
print(a)
a.withdrawal(600)
    
