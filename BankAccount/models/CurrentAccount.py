from models.Account import Account

class CurrentAccount(Account):
    
    min_balance = 5000.0
    interest_rate = 0
    
    def __init__(self, balance = None):
        if(balance is not None):
            super(CurrentAccount, self).__init__(balance)

    
    def withdraw(self, money):
        if(self.__balance - money >= CurrentAccount.min_balance):
            self.__balance -= money
            save(self);
            print("Successfully Withdrawn")
        else:
            print("Not Have Enough Balance to Complete this transaction.Minimum Balance should be "+str(CurrentAccount.min_balance))  
            
    def deposit(self, money):
        if(money <= 1000000):
            self.__balance += money
            save(self);
        else:
            print("Sorry! Max Deposit limit(at a time) is 1 Million.")
        print("Successfully Deposited")
   
    def __str__(self):
        return "\n\nCustomerID: " + str(self.get_cust_id()) + " \nOpening Date: " + str(self.get_opening_date()) + " \nBalance: " + str(self.get_balance())
    