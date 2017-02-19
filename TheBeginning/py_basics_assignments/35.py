java_course = {"John","Jack","Jill","Joe"}
python_course = {"Jack","John","Eric","Jill"}

print("No of people enrolled for python course : ",len(python_course))
print("\nName of people enrolled for python course : \n",python_course)
print("\nName of people enrolled for java course : \n",java_course)
print("\n",len(python_course & java_course)," enrolled for both java and python course. Names are : \n",python_course & java_course)
print("\n",len(python_course ^ java_course)," enrolled for either java and python course but not both. Names are : \n",python_course ^ java_course)
print("\n",len(python_course | java_course)," enrolled for either java and course. Names are : \n",python_course | java_course)


