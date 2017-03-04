n = int(input())
for i in range(n):
    credit = int(input())
    no_of_items = int(input())
    items = [int(x) for x in input().split()]
    for j in range(len(items)):
        remain = credit - items[j];
        items[j] = None;
        if (items.__contains__(remain)):
            index = items.index(remain)
            print("Case #%d: %d %d"%(i+1, j+1, index+1))