from models.Address import Address
from models.CurrentAccount import CurrentAccount
from models.Customer import Customer
from models.SavingAccount import SavingAccount
import mysql.connector as connector


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
            args = (str(obj.get_address_id()), obj.get_line_1(), obj.get_line_2(), obj.get_city(), obj.get_state(), obj.get_pincode())
            cursor.execute("Insert into address values(%s, %s, %s, %s, %s, %s)", args)
            if cursor.lastrowid:
                print("Address Successfully Inserted")
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')
            
            db.commit()
            db.close()
        
        if(isinstance(obj, Customer)):
            print("Inside Customer")
            Util.save(obj.get_address())
            address_id = str(obj.get_address().get_address_id())
            db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
            cursor = db.cursor()
            args = (obj.get_cust_id(), obj.get_password(), obj.get_first_name(), obj.get_last_name(), address_id)
            cursor.execute("Insert into customer values(%s, %s, %s, %s, %s)", args)
            if cursor.lastrowid:
                print("Customer Successfully Inserted")
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')
            
            db.commit()
            db.close()
        
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
            if cursor.lastrowid:
                print("Saving Account Successfully Inserted")
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')
            
            db.commit()
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
            if cursor.lastrowid:
                print("Current Account Successfully Inserted")
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')
                
            db.commit()
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
        cursor.execute("Select first_name, last_name, address_id from customer where cust_id = %s and password = %s", args)
        results = cursor.fetchall();
        if len(results) > 0:
            user = Customer();
            user.set_first_name(results[0][0])
            user.set_last_name(results[0][1])
            user.set_address(results[0][2])
        db.close()
        return user
    
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