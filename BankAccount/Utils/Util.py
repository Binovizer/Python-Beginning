from models.Address import Address
from models.Customer import Customer
from models.Transaction import Transaction
import mysql.connector as connector
from models.CurrentAccount import CurrentAccount
from models.SavingAccount import SavingAccount
 
 
class Util:     
     
    @staticmethod
    def save(obj, cust_id = None, account_type = None):
         
        if(isinstance(obj, Address)):
            print("Inside Address")
            db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
            cursor = db.cursor()
            args = (obj.get_line_1(), obj.get_line_2(), obj.get_city(), obj.get_state(), obj.get_pincode())
            cursor.execute("Insert into address(address_line_1, address_line_2, city, state, pincode ) values(%s, %s, %s, %s, %s)", args)
            address_id = cursor.lastrowid
            print("Address ID : ",address_id)
            if address_id:
                print("Address Successfully Inserted")
                print('last insert id', address_id)
            else:
                print('last insert id not found')
                print("Address Insertion Failed.")
             
            db.commit()
            db.close()
            return address_id
         
        if(isinstance(obj, Customer)):
            print("Inside Customer")
            address_id = Util.save(obj.get_address())
            db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
            cursor = db.cursor()
            args = (obj.get_password(), obj.get_first_name(), obj.get_last_name(), address_id)
            cursor.execute("Insert into customer(password, first_name, last_name, address_id) values(%s, %s, %s, %s)", args)
            cust_id = cursor.lastrowid
            print("Customer ID: ", cust_id)
            if cust_id:
                print("Customer Successfully Inserted")
                print('last insert id', cust_id)
            else:
                print('last insert id not found')
                print("Failed to Insert User")
             
            db.commit()
            db.close()
            return cust_id
         
        if(isinstance(obj, SavingAccount)):
            print("Inside SavingAccount")
            if(cust_id is None):
                print("No customer Id provided")
                return None
            if(account_type is None):
                print("No Account Type provided")
                return None
        
            db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
            cursor = db.cursor()
            args = (cust_id, obj.get_balance(), obj.get_opening_date().strftime('%Y-%m-%d'), obj.get_no_of_withdraw(), account_type, "A")
            cursor.execute("Insert into account(account_no, balance, opening_date, no_of_withdrawal, account_type, status) values(%s, %s, %s, %s, %s, %s)", args)
            
            db.commit()
            print("Saving Account with ID: " + str(cust_id) + " created.")
            db.close()
  
             
        if(isinstance(obj, CurrentAccount)):
            print("Inside CurrentAccount")
            if(cust_id is None):
                print("No customer Id provided")
                return None
            if(account_type is None):
                print("No Account Type provided")
                return None
            db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
            cursor = db.cursor()
            args = (cust_id, obj.get_balance(), obj.get_opening_date().strftime('%Y-%m-%d'), account_type, "A")
            cursor.execute("Insert into account(account_no, balance, opening_date, account_type, status) values(%s, %s, %s, %s, %s)", args)
                 
            db.commit()
            print("Current Account with ID: " + str(cust_id) + " created.")
            db.close()
             
    @staticmethod  
    def checkCredentials(user_id, password):
        user = None
        db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
        cursor = db.cursor()
        args = (user_id, password)
        cursor.execute("Select c.first_name, c.last_name, c.address_id, a.status from customer as c, account as a where c.cust_id = %s and c.password = %s and a.account_no = c.cust_id", args)
        results = cursor.fetchall();
        if len(results) > 0:
            if(results[0][3] == 'C'):
                print("Your Account is Closed. Please contact your bank admin.")
            else:
                user = Customer();
                user.set_first_name(results[0][0])
                user.set_last_name(results[0][1])
                user.set_address(results[0][2])
        db.close()
        return user
     
    @staticmethod  
    def checkAdminCredentials(user_id, password):
        login = False
        db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
        cursor = db.cursor()
        args = (user_id, password)
        cursor.execute("Select user_id from admin where user_id = %s and password = %s ", args)
        results = cursor.fetchall();
        if len(results) > 0:
            login = True
        db.close()
        return login
     
    @staticmethod
    def update(obj):
        if(isinstance(obj, Address)):
            db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
            cursor = db.cursor()
            args = (obj.get_line_1(), obj.get_line_2(), obj.get_city(), obj.get_state(), obj.get_pincode(), str(obj.get_address_id()))
            cursor.execute("""UPDATE address SET address_line_1 = %s,
                                     address_line_2 = %s,
                                     city = %s,
                                     state = %s,
                                     pincode = %s
                            WHERE id = %s""", args)
            db.commit()
            db.close()
             
    @staticmethod  
    def get_db_account(account_id):
        user_account = None
        db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
        cursor = db.cursor()
        args = (account_id,)
        cursor.execute("Select account_type, balance, no_of_withdrawal, opening_date from account where account_no = %s ", args)
        results = cursor.fetchall();
        if len(results) > 0:
            if(results[0][0] == "Saving"):
                user_account = SavingAccount()
                user_account.set_no_of_withdraw(results[0][2])
            else:
                user_account = CurrentAccount()
            user_account.set_cust_id(account_id)
            user_account.set_balance(results[0][1])
            user_account.set_opening_date(results[0][3])
  
        db.close()
        return user_account
    
    @staticmethod
    def transfer(user_account, to_account, money):
        if(user_account.get_balance() - money > 0):
            new_account = Util.get_db_account(to_account)
            if(new_account != None):
                Transaction.create(new_account, money, tran_type = "Transfer", add = True, account_id = user_account.get_cust_id())
                new_account.set_balance(new_account.get_balance() + money)
                new_account.updateDBAccountBalance()
                
                Transaction.create(user_account, money, tran_type = "Transfer", add = False, account_id = to_account)
                user_account.set_balance(user_account.get_balance() - money)
                user_account.updateDBAccountBalance()
                print(str(money)+" has been transferred to "+str(to_account))
            else:
                print("Recipient Account Not Found")
                print("Please Check the Recipient Account Number.")
            

    