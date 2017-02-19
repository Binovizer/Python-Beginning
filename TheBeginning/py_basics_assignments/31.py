n = int(input("Enter n : "))
fiblist = []      

n1 = 0
n2 = 1
fiblist.append(n1)
fiblist.append(n2)
count = 2

if (n==1):
    fiblist = [0]
elif (n==2):
    fiblist = [0,1]
else:
    while(count < n):
        nth = n1 + n2
        fiblist.append(nth)
        n1 = n2 
        n2 = nth
        count += 1
    
print(fiblist)
