def addPrice(item_price):
    item_price += 25
    print("Item price inside function : ",item_price)
    
item_price = 10
print("Item Price Before calling method : ",item_price)
addPrice(item_price)
print("Item Price After calling method : ",item_price)