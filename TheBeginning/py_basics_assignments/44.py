price_list = [1050,2200,8575,485,234,150,399];

def costliest_item(price_list):
    return max(price_list)

def average(price_list):
    total = 0
    for i in price_list:
        total += i
    return round(total/len(price_list),2)

def sortByPrice(price_list):
    #price_list.sort();
    return sorted(price_list)

print(costliest_item(price_list))
print(average(price_list))
print(sortByPrice(price_list))