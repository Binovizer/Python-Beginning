from models.Account import Account
from models.Transaction import Transaction

class CurrentAccount(Account):
     
    min_balance = 5000.0
    interest_rate = 0
     
    def __init__(self, balance = None):
        if(balance is not None):
            super(CurrentAccount, self).__init__(balance)
        self.account_type = "Current"
 
    def get_account_type(self):
        return self.__account_type
 
 
    def set_account_type(self, value):
        self.__account_type = value
 
 
    def del_account_type(self):
        del self.__account_type
 
     
    def withdraw(self, money):
        if(super(CurrentAccount, self).get_balance() - money >= CurrentAccount.min_balance):
            Transaction.create(self, money, tran_type = "Withdraw");
            new_bal = super(CurrentAccount, self).get_balance() - money
            super(CurrentAccount, self).set_balance(new_bal)
            super(CurrentAccount, self).updateDBAccountBalance()
            print("Successfully Withdrawn " + str(money) + " from account " + super(CurrentAccount, self).get_cust_id())
        else:
            print("Not Have Enough Balance to Complete this transaction.Minimum Balance should be "+str(CurrentAccount.min_balance))  
 
    
    def __str__(self):
        return "\n\nCustomerID: " + str(self.get_cust_id()) + " \nOpening Date: " + str(self.get_opening_date()) + " \nBalance: " + str(self.get_balance())
     
    account_type = property(get_account_type, set_account_type, del_account_type, "account_type's docstring")
    