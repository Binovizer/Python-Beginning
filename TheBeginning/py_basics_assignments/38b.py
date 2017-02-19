def addList(item_list):
    item_list += ["Iphone 7"]

def updateList(item_list):
    item_list[1] = "Iphone 6s"


item_list = ["Samsung Mobile","Lenovo Mobile"];
print("Item List : ",item_list)
addList(item_list)
print("Item List after calling add : ",item_list)
updateList(item_list)
print("Item list after calling update : ",item_list)