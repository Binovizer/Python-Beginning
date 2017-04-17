import datetime
import mysql.connector as connector
from models.Transaction import Transaction

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

    def close(self):
        db = connector.connect(user='root',
                               password='3464',
                               host='127.0.0.1',
                               database='python_bank_project')
        cursor = db.cursor()
        args = (datetime.datetime.today().strftime('%Y-%m-%d'), "C", self.get_cust_id())
        cursor.execute("UPDATE account SET closed_date = %s, status = %s where account_no = %s ", args)
        db.commit()
        db.close()
    
    def updateDBAccountBalance(self):
        db = connector.connect(user='root',
                               password='3464',
                               host='127.0.0.1',
                               database='python_bank_project')
        cursor = db.cursor()
        args = (self.get_balance(), self.get_cust_id())
        cursor.execute("UPDATE account SET balance = %s where account_no = %s ", args)
        db.commit()
        db.close()
      
    def withdraw(self, money):
        print("Inside Account Withdraw")
        if(self.__balance - money >= 0):
            Transaction.create(self, money, tran_type = "Withdraw");
            self.__balance -= money
            self.updateDBAccountBalance()
            print("Successfully Withdrawn " + str(money) + " from account " + self.get_cust_id())
        else:
            print("Not Have Enough Balance to Complete this transaction.")  
             
    def deposit(self, money):
        if(money <= 1000000):
            Transaction.create(self, money, tran_type = "Deposit");
            self.__balance += money
            self.updateDBAccountBalance()
            print("Successfully deposited " + str(money) + " to account " + self.get_cust_id())
        else:
            print("Sorry! Max Deposit limit(at a time) is 1 Million.")
    
    def printStatement(self):
        db = connector.connect(user='root',
                               password='3464',
                               host='127.0.0.1',
                               database='python_bank_project')
        cursor = db.cursor()
        args = (self.get_cust_id(),)
        cursor.execute("SELECT transaction_id, transaction_type, initial_balance, deposits, withdrawals, balance from transaction WHERE cust_id = %s ", args)
        results = cursor.fetchall()
        if(len(results) > 0):
            print("\n\nYour Statement : \n")
            print('{0:37}  {1:>16}  {2:>16}  {3:>12}  {4:>13}  {5:>15}'.format("Transaction Id", "Transaction Type", "Initial Balance", "Deposits", "Withdrawals", "Balance"))
            print()
            for row in results:
                formatted_str = None
                if(row[1] == "Deposit"):
                    formatted_str = '{0:37}  {1:16}  {2:16.2f}  {3:12.2f}  {4:13.2f}  {5:15.2f} '.format(row[0], row[1], float(row[2]), float(row[3]), 0.0, float(row[5]));
                elif(row[1] == "Withdrawal"):
                    formatted_str = '{0:37}  {1:16}  {2:16.2f}  {3:12.2f}  {4:13.2f}  {5:15.2f} '.format(row[0], row[1], float(row[2]), 0.0 , float(row[4]), float(row[5]));
                
                print(formatted_str)
                print()
        db.close()
    

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
    
    