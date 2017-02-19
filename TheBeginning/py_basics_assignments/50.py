import re
student_id = input("Enter student id : ")
if(re.search("[^0-9]", student_id)):
    print("Sorry! Student ID can only contains digit")
else:
    student_name = input("Enter student name : ")
    if re.search("[^a-zA-Z]", student_name):
        print("Name can only contain alphabets")
    else:
        print("Hello",student_name.capitalize())
        fees_amount = input("Enter Fees Amount : ")
        if re.search("^\d+(\.\d{1,2})?$", fees_amount):
                college_name = "akgec"
                email_id = student_name.lower()+"@"+college_name+".com"
                print("\nStudent ID : ",student_id)
                print("Student Name : ",student_name)
                print("Student Fees : ",fees_amount)
                print("Student Email ID : ",email_id)
        else:
                print("Sorry! Only two digits are allowed after decimal point")