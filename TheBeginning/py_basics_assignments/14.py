bill_id = 101
customer_id = 1001
bill_amount = int(input("Enter the bill amount : "))

print("Bill Id : %d" %bill_id)
print("Customer Id : %d" %customer_id)
print("Bill Amount : Rs. %d" %bill_amount)


if (bill_id > 100 and bill_id < 1001):
    if (bill_amount >= 500 ):
        discounted_bill_amount = 0.9 * bill_amount
        print("Discounted Bill Amount : ",discounted_bill_amount)
    else :
        print("No discount")
else:
    print("Invalid Customer ID, Customer ID must be in between 101 and 1000 (both inclusive) ")

