from models.Account import Account

class SavingAccount(Account):
     
    min_balance = 0.0
    interest_rate = 7.5
     
    def __init__(self, balance = None):
        if(balance is not None):
            super(SavingAccount, self).__init__(balance)
        self.no_of_withdraw = 10
        self.account_type = "Saving"
 
    def get_account_type(self):
        return self.__account_type
 
 
    def set_account_type(self, value):
        self.__account_type = value
 
 
    def del_account_type(self):
        del self.__account_type
 
 
 
    def get_no_of_withdraw(self):
        return self.__no_of_withdraw
 
 
    def set_no_of_withdraw(self, value):
        self.__no_of_withdraw = value
 
 
    def del_no_of_withdraw(self):
        del self.__no_of_withdraw
         
      
    def __str__(self):
        return "\n\nCustomerID: " + str(self.get_cust_id()) + " \nOpening Date: " + str(self.get_opening_date()) + " \nBalance: " + str(self.get_balance()) +" \nNo of withdrawals Left(This Month) : " + str(self.get_no_of_withdraw())
         
    no_of_withdraw = property(get_no_of_withdraw, set_no_of_withdraw, del_no_of_withdraw, "no_of_withdraw's docstring")
    account_type = property(get_account_type, set_account_type, del_account_type, "account_type's docstring")
