class Customer:
    
    def __init__(self, fname = None, lname = None, address = None):
        if(fname is not None):
            self.firstName = fname
        if(lname is not None):
            self.lastName = lname
        if(address is not None):
            self.address = address

    def get_password(self):
        return self.__password


    def set_password(self, value):
        self.__password = value


    def del_password(self):
        del self.__password

        
    def get_cust_id(self):
        return self.__cust_id


    def get_first_name(self):
        return self.__firstName


    def get_last_name(self):
        return self.__lastName


    def get_address(self):
        return self.__address


    def get_transactions(self):
        return self.__transactions


    def set_cust_id(self, value):
        self.__cust_id = value


    def set_first_name(self, value):
        self.__firstName = value


    def set_last_name(self, value):
        self.__lastName = value


    def set_address(self, value):
        self.__address = value


    def set_transactions(self, value):
        self.__transactions = value


    def del_cust_id(self):
        del self.__cust_id


    def del_first_name(self):
        del self.__firstName


    def del_last_name(self):
        del self.__lastName


    def del_address(self):
        del self.__address


    def del_transactions(self):
        del self.__transactions

    cust_id = property(get_cust_id, set_cust_id, del_cust_id, "cust_id's docstring")
    firstName = property(get_first_name, set_first_name, del_first_name, "firstName's docstring")
    lastName = property(get_last_name, set_last_name, del_last_name, "lastName's docstring")
    address = property(get_address, set_address, del_address, "address's docstring")
    transactions = property(get_transactions, set_transactions, del_transactions, "transactions's docstring")
    password = property(get_password, set_password, del_password, "password's docstring")
    
    def __str__(self):
        return "\n\nCustId: " + str(self.get_cust_id()) + " \nFull Name: " + self.firstName +" "+ self.get_last_name() + " \n*****Address**** \n" + str(self.get_address())
    
    