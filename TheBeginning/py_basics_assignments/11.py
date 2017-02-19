bill_amount = int(input("Enter the bill amount : "))
if (bill_amount > 500) : 
    bill_amount = .98 * bill_amount
else :
    bill_amount = .99 * bill_amount

print("You have to pay : %d" %bill_amount)