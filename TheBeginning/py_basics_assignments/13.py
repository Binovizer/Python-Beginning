bill_id = 101
customer_id = 1001
bill_amount = int(input("Enter the bill amount : "))

if (bill_amount >= 1000) : 
    discount = 5
elif (bill_amount >= 500) :
    discount = 2
else:
    discount = 1
    
discounted_bill_amount = bill_amount - bill_amount * discount / 100;

print("Bill Id : %d" %bill_id)
print("Customer Id : %d" %customer_id)
print("Bill Amount : Rs. %d" %bill_amount)
print("Discounted Bill Amount : Rs. ",discounted_bill_amount)