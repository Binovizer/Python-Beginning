from Utils.Util import Util
from models.SavingAccount import SavingAccount
from models.Address import Address
from models.Customer import Customer
from models.CurrentAccount import CurrentAccount
from Utils.AdminUtil import AdminUtil

def printMainMenu():
    print("\n\nEnter: ")
    print("1 for Sign Up")
    print("2 for Sign In")
    print("3 for Admin Sign In")
    print("4 for Quit")

def getAddresFromInput():
    address = Address()
    print("Enter Your Address Please ")
    address.set_line_1(str(input("Address Line 1: ")))
    address.set_line_2(str(input("Address Line 2: ")))
    address.set_city(str(input("City: ")))
    address.set_state(str(input("State: ")))
    pincode = input("Pincode: ")
    while(True):
        if not pincode.isdigit(): 
            print ("Enter only digits\n")
            pincode = input("Pincode: ")
            continue
        elif len(pincode) != 6:
            print ("Enter 6 digits\n")
            pincode = input("Pincode: ")
            continue
        else: 
            break
    address.set_pincode(pincode)
    return address

def validateAmount(input_msg):
    while True:
        try:
            amount = float(input (input_msg))
        except ValueError:
            print("Please enter amount Correctly.")
        else:
            return amount
    
def validateNumber(x):
    while(True):
        if not x.isdigit(): 
            print ("Enter only digit\n")
            x = input(" : ")
            continue
        else:
            return int(x)  
    
def printCustomerSubMenu():
    print("\n\nEnter: ")
    print("1 for Address Change")
    print("2 for Money Deposit")
    print("3 for Money Withdrawal")
    print("4 for Print Statement")
    print("5 for Transfer Money")
    print("6 for Account Closure")
    print("7 for Customer Logout",end="")    

def validatePassword(password, input_msg):
    while(True):
        if len(password) < 8:
            print ("Password Must be min 8 characters long.\n")
            password = input(input_msg)
            continue
        else:
            return password


print("Hello!!")
print("Welcome to the Swiss Bank!!!")
not_valid = False
while(not not_valid):
    printMainMenu();
    x = input(":")
    while(True):
            if not x.isdigit(): 
                print ("Enter only digit\n")
                printMainMenu()
                x = input(" : ")
                continue
            else:
                x = int(x) 
                break
    if(x == 1):
        print("Please Enter your Details to continue: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        address = getAddresFromInput()
        new_account = None
        account_type_str = None
        print("Account Type")
        print("1 for Saving Account")
        print("2 for Current Account")
        account_type = validateNumber(input(" : "))
        if(account_type == 1):
            account_type_str = "Saving"
            balance = validateAmount("Enter Opening Balance Please: ")
            new_account = SavingAccount(balance)
        elif(account_type == 2):
            account_type_str = "Current"
            balance = validateAmount("Enter Opening Balance Please: ")
            while(balance < CurrentAccount.min_balance):
                print("Sorry! Min Opening Balance Should be "+str(CurrentAccount.min_balance))
                balance = validateAmount("Enter Opening Balance Please: ")
            new_account = CurrentAccount(balance)
        else:
            print("Invalid Choice")

        new_user = Customer(fname, lname,address)
        print("Please Enter Your Password")
        password = validatePassword(input("Password: "), "Password: ")
        re_password = validatePassword(input("Re-Password: "), "Re-Password: ")
        while(password != re_password):
            print("Please enter the same password.")
            password = validatePassword(input("Password: "), "Password: ")
            re_password = validatePassword(input("Re-Password: "), "Re-Password: ")
        
        new_user.set_password(password)
        cust_id = Util.save(new_user)
        new_user.set_cust_id(cust_id)
        print("Your Customer ID is : ",new_user.get_cust_id())
        print("Please Keep it Safe.")
        Util.save(new_account, new_user.get_cust_id(), account_type_str)
        new_account = None
        new_user = None
        address  = None
        
         
    elif(x == 2):
        print("\n\nPlease Login to Continue: ")
        logged_in = False
        while(not logged_in):
            user_id = input("Customer Id: ")
            password = validatePassword(input("Password : "), "Password: ")
            user = Util.checkCredentials(user_id, password)
            if(user != None):
                user.set_cust_id(user_id)
                user_account = Util.get_db_account(user_id)
                print(user_account)
                logged_in = True
            else:
                print("\nCustomer Id or Password is incorrect. Please try again...")
        
        print("\n\nWelcome " + user.get_first_name() + " " + user.get_last_name() + "!")
        
        while(logged_in):
            printCustomerSubMenu();
            choice = validateNumber(input(" : "))
            if(choice == 1):
                address = getAddresFromInput()
                address.set_address_id(user.get_address())
                Util.update(address)
                print("\n\nYour Address has been changed Successfully")
            elif(choice == 2):
                money = validateAmount("Enter Amount : ")
                user_account.deposit(money)
            elif(choice == 3):
                money = validateAmount("Enter Amount : ")
                user_account.withdraw(money)
            elif(choice == 4):
                user_account.printStatement()
            elif(choice == 5):
                to_account = input("\nEnter Recipient Account No: ")
                money = validateAmount("Enter Money to be transferred: ")
                Util.transfer(user_account, to_account, money);
            elif(choice == 6):
                print("\n\nAre you sure you want to close your account ?")
                print("Enter :")
                print("1 for Yes")
                print("2 for No")
                sure = validateNumber(input(" : "))
                if(sure == 1):
                    user_account.close();
                    print("Your Account is closed.")
                    print("\nThank You for Banking with us.")
                    print("Your remaining account balance " + str(user_account.get_balance()) + " will be sent to you through cheque on your address.")
                logged_in = False
                                        
            elif(choice == 7):
                    user = None
                    user_account = None
                    logged_in = False
                    print("Successfully Logged Out.")
            else:
                print("\nWrong Choice. Please choose proper option.\n\n")
        
    elif(x == 3):
        print("\n\nPlease Login to Continue: ")
        logged_in = False
        while(not logged_in):
            user_id = input("Username: ")
            password = input("Password: ")
            if(Util.checkAdminCredentials(user_id, password)):
                logged_in = True
            else:
                print("\nUsername or Password is incorrect. Please try again...")
        print("\n\nEnter: ")
        print("1 to Print Closed Account History")
        print("2 for Logout")
        choice = validateNumber(input(" : "))
        if(choice == 1):
            print("\n\nALl Details are as follows")
            AdminUtil.printClosedAccounts()
        elif(choice == 2):
            print("\n\nSuccessfully Logged out")
        else:
            print("\n\nInvalid Choice.")
        
        
    elif(x == 4):
        print("\n\nThank You for Choosing Us.")
        print("Bye!")
        not_valid = True
    else:
        print("\n\nInvalid Choice. Please Re-enter.")