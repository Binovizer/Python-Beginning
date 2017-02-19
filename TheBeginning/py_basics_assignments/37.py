#import operator

student_marks = {"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}

total = 0.0
for element in student_marks.values() :
    total += float(element)

print("Average is : ",total/len(student_marks))

#sorted_marks_list = sorted(student_marks, key=operator.itemgetter(1))
sorted_marks_list = sorted(student_marks, key=student_marks.__getitem__,reverse=True) #In Descending Order
#print(sorted_marks_list)

count = 1
print("Top three students are : ",end="")
for element in sorted_marks_list:
    if(count > 3):
        break    
    print(element," ",end="")
    count += 1

