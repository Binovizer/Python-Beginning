customer_details = {1001:"John",1004:"Jill",1005:"Joe",1003:"Jack"}

print("Details of Customers : \n",customer_details) # Details of Customer
print("\nNo of customers",len(customer_details)) # No of customers
print("\nSorted Names of Customers : ",sorted(customer_details.values())) # Sorted Names of Customers 
del(customer_details[1005])
print("\nAfter Deleting 1005 : ",customer_details)
customer_details[1003] = "Mary"
print("\nUpdating 1003 to Mary : ",customer_details)
print("\nIs 1002 in customer_details : ",1002 in customer_details)