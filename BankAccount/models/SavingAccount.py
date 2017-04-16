from models.Account import Account

class SavingAccount(Account):
    
    min_balance = 0.0
    interest_rate = 7.5
    
    def __init__(self, balance = None):
        if(balance is not None):
            super(SavingAccount, self).__init__(balance)
        self.no_of_withdraw = 10


    def get_no_of_withdraw(self):
        return self.__no_of_withdraw


    def set_no_of_withdraw(self, value):
        self.__no_of_withdraw = value


    def del_no_of_withdraw(self):
        del self.__no_of_withdraw

    
#     def withdraw(self, money):
#         if(self.__balance - money >= SavingAccount.min_balance):
#             self.__balance -= money
#             save(self);
#             print("Successfully Withdrawn")
#         else:
#             print("Not Have Enough Balance to Complete this transaction")  
#             
#     def deposit(self, money):
#         if(money <= 1000000):
#             self.__balance += money
#             save(self);
#         else:
#             print("Sorry! Max Deposit limit(at a time) is 1 Million.")
#         print("Successfully Deposited")
     
    def __str__(self):
        return "\n\nCustomerID: " + str(self.get_cust_id()) + " \nOpening Date: " + str(self.get_opening_date()) + " \nBalance: " + str(self.get_balance()) +" \nNo of withdrawals Left(This Month) : " + str(self.get_no_of_withdraw())
        
    no_of_withdraw = property(get_no_of_withdraw, set_no_of_withdraw, del_no_of_withdraw, "no_of_withdraw's docstring")
