import mysql.connector as connector
import uuid
class Transaction:
    
    def __init__(self, transaction_id = 1, transaction_type_id = 1, balance = 0.0
                 ,withdrawals = 0.0, deposits = 0.0 ):
        self.transaction_id = transaction_id
        self.transaction_type_id = transaction_type_id
        self.balance = balance
        self.withdrawals = withdrawals
        self.deposits = deposits

    @staticmethod
    def create(obj, money, tran_type, add = None):
        if(tran_type == "Withdraw"):
            db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
            cursor = db.cursor()
            args = (str(uuid.uuid4()), obj.get_cust_id(), "Withdrawal", obj.get_balance(), money, obj.get_balance() - money)
            cursor.execute("Insert into transaction(transaction_id, cust_id, transaction_type, initial_balance, withdrawals, balance ) values(%s, %s, %s, %s, %s, %s)", args)
            db.commit()
            db.close()
        elif(tran_type == "Deposit"):
            db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
            cursor = db.cursor()
            args = (str(uuid.uuid4()), obj.get_cust_id(), "Deposit", obj.get_balance(), money, obj.get_balance() + money)
            cursor.execute("Insert into transaction(transaction_id, cust_id, transaction_type, initial_balance, deposits, balance ) values(%s, %s, %s, %s, %s, %s)", args)
            db.commit()
            db.close()
            
        elif(tran_type == "Transfer"):
            if(add == True):
                db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
                cursor = db.cursor()
                args = (str(uuid.uuid4()), obj.get_cust_id(), "Transfer", obj.get_balance(), money, obj.get_balance() + money)
                cursor.execute("Insert into transaction(transaction_id, cust_id, transaction_type, initial_balance, deposits, balance ) values(%s, %s, %s, %s, %s, %s)", args)
                db.commit()
                db.close()
            elif(add == False):
                db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
                cursor = db.cursor()
                args = (str(uuid.uuid4()), obj.get_cust_id(), "Deposit", obj.get_balance(), money, obj.get_balance() + money)
                cursor.execute("Insert into transaction(transaction_id, cust_id, transaction_type, initial_balance, withdrawals, balance ) values(%s, %s, %s, %s, %s, %s)", args)
                db.commit()
                db.close()

    def get_transaction_id(self):
        return self.__transaction_id


    def get_transaction_type_id(self):
        return self.__transaction_type_id


    def get_balance(self):
        return self.__balance


    def get_withdrawals(self):
        return self.__withdrawals


    def get_deposits(self):
        return self.__deposits


    def set_transaction_id(self, value):
        self.__transaction_id = value


    def set_transaction_type_id(self, value):
        self.__transaction_type_id = value


    def set_balance(self, value):
        self.__balance = value


    def set_withdrawals(self, value):
        self.__withdrawals = value


    def set_deposits(self, value):
        self.__deposits = value


    def del_transaction_id(self):
        del self.__transaction_id


    def del_transaction_type_id(self):
        del self.__transaction_type_id


    def del_balance(self):
        del self.__balance


    def del_withdrawals(self):
        del self.__withdrawals


    def del_deposits(self):
        del self.__deposits

    transaction_id = property(get_transaction_id, set_transaction_id, del_transaction_id, "transaction_id's docstring")
    transaction_type_id = property(get_transaction_type_id, set_transaction_type_id, del_transaction_type_id, "transaction_type_id's docstring")
    balance = property(get_balance, set_balance, del_balance, "balance's docstring")
    withdrawals = property(get_withdrawals, set_withdrawals, del_withdrawals, "withdrawals's docstring")
    deposits = property(get_deposits, set_deposits, del_deposits, "deposits's docstring")
        