bill_id = input("Enter Bill Id : ")
customer_id = input("Enter Customer Id : ")
bill_amount = input("Enter Bill Amount : ")
customer_name = input("Enter Customer Name : ")

if (len(customer_name) > 2 and len(customer_name) <= 20):
    print("Bill Id : ",bill_id)
    print("Customer Id : ",customer_id)
    print("Bill Amount : ",bill_amount)
    print("Customer Name : ",customer_name)
else:
    print("Invalid Name! Name Length must be in between 3 to 20")