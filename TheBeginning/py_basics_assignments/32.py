a = [int(x) for(x) in input("Enter numbers : ").split(sep=' ')] #Taking list as an input
print("List before sorting : ",a)
#Bubble Sort
for i in range(0,len(a)) :
    for j in range(0,len(a)-i-1) :
        if (a[j] < a[j+1]):
            temp = a[j];
            a[j] = a[j+1];
            a[j+1] = temp
            
print("List after sorting : ",a)