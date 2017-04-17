import sys
from Utils.Util import Util
from uuid import uuid4
from models.SavingAccount import SavingAccount
from models.Address import Address
from models.Customer import Customer
from models.CurrentAccount import CurrentAccount
from Utils.AdminUtil import AdminUtil

def checkCredentials(user_id, password):
    if(user_id == password):
        return True
    return False

print("Hello!!")
print("Welcome to the Bank Account Project.")
not_valid = False
while(not not_valid):
    print("\n\nEnter: ")
    print("1 for Sign Up")
    print("2 for Sign In")
    print("3 for Admin Sign In")
    print("4 for Quit")
    x = int(input(":"))
    if(x == 1):
        print("Please Enter your Details to continue: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        address = Address()
        print("Enter Your Address Please ")
        address.set_line_1(str(input("Address Line 1: ")))
        address.set_line_2(str(input("Address Line 2: ")))
        address.set_city(str(input("City: ")))
        address.set_state(str(input("State: ")))
        address.set_pincode(str(input("Pincode: ")))
        address.set_address_id()
        new_account = None
        account_type_str = None
        print("Account Type")
        print("1 for Saving Account")
        print("2 for Current Account")
        account_type = int(input(" : "))
        if(account_type == 1):
            account_type_str = "Saving"
            balance = float(input("Enter Opening Balance Please: "))
            new_account = SavingAccount(balance)
        elif(account_type == 2):
            account_type_str = "Current"
            balance = float(input("Enter Opening Balance Please: "))
            while(balance < CurrentAccount.min_balance):
                print("Sorry! Min Opening Balance Should be "+str(CurrentAccount.min_balance))
                print("Enter Proper Opening Balance Please")
                balance = float(input(" : "))
            new_account = CurrentAccount(balance)
        else:
            print("Invalid Choice")

        new_user = Customer(fname, lname,address)
        new_user.set_cust_id(str(uuid4()))
        new_account.set_cust_id(new_user.get_cust_id())
        print("Your CustomerId is : "+str(new_user.get_cust_id()))
        print("Please Keep It Safe.")
        print("Please Enter Your Password")
        password = input(" : ")
        re_password = input("Re-enter: ")
        while(password != re_password):
            print("Please enter the same password")
            print("Please Enter Your Password")
            password = input(" : ")
            re_password = input("Re-enter: ")
        
        new_user.set_password(password)
        Util.save(new_account, new_user.get_cust_id(), account_type_str)
        Util.save(new_user)
        print(new_account)
        print(new_user)
        
         
    elif(x == 2):
        print("\n\nPlease Login to Continue: ")
        logged_in = False
        while(not logged_in):
            user_id = input("Username: ")
            password = input("Password: ")
            user = Util.checkCredentials(user_id, password)
            if(user != None):
                user.set_cust_id(user_id)
                user_account = Util.get_db_account(user_id)
                print(user_account)
                logged_in = True
            else:
                print("Username or Password is incorrect. Please try again...")
        print("Welcome "+user.get_first_name()+" "+user.get_last_name() + "!")
        
        while(logged_in):
            print("\n\nEnter: ")
            print("1 for Address Change")
            print("2 for Money Deposit")
            print("3 for Money Withdrawal")
            print("4 for Print Statement")
            print("5 for Transfer Money")
            print("6 for Account Closure")
            print("7 for Customer Logout",end="")
            choice = int(input(":"))
            if(choice == 1):
                address = Address()
                print("\n\nEnter Your Address Please ")
                address.set_line_1(str(input("Address Line 1: ")))
                address.set_line_2(str(input("Address Line 2: ")))
                address.set_city(str(input("City: ")))
                address.set_state(str(input("State: ")))
                address.set_pincode(str(input("Pincode: ")))
                address.set_address_id(user.get_address())
                Util.update(address)
                print("\n\nYour Address has been changed Successfully")
            elif(choice == 2):
                money = float(input("\n\nEnter amount: "))
                user_account.deposit(money)
            elif(choice == 3):
                money = float(input("\n\nEnter amount: "))
                user_account.withdraw(money)
            elif(choice == 4):
                user_account.printStatement()
            elif(choice == 5):
                to_account = input("Enter Recipient Account No: ")
                money = input("Enter Money to be Transferred : ")
                print(str(money)+" has been transferred to "+str(to_account))
            elif(choice == 6):
                print("Are you sure you want to close your account ?")
                print("Enter :")
                print("1 for Yes")
                print("2 for No")
                sure = int(input(" : "))
                if(sure == 1):
                    user_account.close();
                    print("Thank You for Banking with us.")
                    print("Your remaining account balance " + str(user_account.get_balance()) + " will be sent to you through cheque on your address.")
                    print(user.get_address())
                    logged_in = False
                else:
                    sys.exit() 
            elif(choice == 7):
                    user = None
                    user_account = None
                    logged_in = False
                    print("Successfully Logged Out.")
            else:
                print("Wrong Choice. Please choose proper option.\n\n")
        
    elif(x == 3):
        print("\n\nPlease Login to Continue: ")
        logged_in = False
        while(not logged_in):
            user_id = input("Username: ")
            password = input("Password: ")
            if(Util.checkAdminCredentials(user_id, password)):
                logged_in = True
            else:
                print("Username or Password is incorrect. Please try again...")
        print("Welcome Mr.Nadeem")
        print("Enter: ")
        print("1 to Print Closed Account History")
        print("2 for Logout")
        choice = int(input(" : "))
        if(choice == 1):
            print("ALl Details are as follows")
            AdminUtil.printClosedAccounts()
        elif(choice == 2):
            print("Successfully Logged out")
        else:
            print("Invalid Choice.")
        
        
    elif(x == 4):
        print("Thank You for Choosing Us.")
        print("Bye!")
        not_valid = True
    else:
        print("Invalid Choice. Please Re-enter.")