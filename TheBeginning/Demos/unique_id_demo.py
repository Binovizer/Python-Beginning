import uuid
id_set = set()
n = 1
while(n <= 100):
    uid = uuid.uuid4()
    print(uid)
    id_set.add(uid)
    n += 1

if(len(id_set) == 100):
    print("Working")
else:
    print("Not Working")