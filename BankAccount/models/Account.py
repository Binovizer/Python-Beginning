import datetime

class Account:
    
    def __init__(self, balance):
        self.opening_date = datetime.date.today()
        self.closing_date = None
        self.balance = balance

    def get_balance(self):
        return self.__balance


    def set_balance(self, value):
        self.__balance = value


    def del_balance(self):
        del self.__balance

        
    def withdraw(self, money):
        pass
    
    def deposit(self, money):
        pass
    
    def printStatement(self, cust_id, from_date, to_date):
        pass
    

    def get_cust_id(self):
        return self.__cust_id


    def get_opening_date(self):
        return self.__opening_date


    def get_closing_date(self):
        return self.__closing_date


    def set_cust_id(self, value):
        self.__cust_id = value


    def set_opening_date(self, value):
        self.__opening_date = value


    def set_closing_date(self, value):
        self.__closing_date = value


    def del_account_id(self):
        del self.__account_id


    def del_cust_id(self):
        del self.__cust_id


    def del_opening_date(self):
        del self.__opening_date


    def del_closing_date(self):
        del self.__closing_date

    cust_id = property(get_cust_id, set_cust_id, del_cust_id, "cust_id's docstring")
    opening_date = property(get_opening_date, set_opening_date, del_opening_date, "opening_date's docstring")
    closing_date = property(get_closing_date, set_closing_date, del_closing_date, "closing_date's docstring")
    balance = property(get_balance, set_balance, del_balance, "balance's docstring")
    
    