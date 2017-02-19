bill_id = 101
customer_id = 1001
bill_amount = int(input("Enter the bill amount : "))
if (bill_amount > 500) : 
    discounted_bill_amount = .98 * bill_amount
else :
    discounted_bill_amount = .99 * bill_amount

print("Bill Id : %d" %bill_id)
print("Customer Id : %d" %customer_id)
print("Bill Amount : Rs. %d" %bill_amount)
print("Discounted Bill Amount : Rs. ",discounted_bill_amount)