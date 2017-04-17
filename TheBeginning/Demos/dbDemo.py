import mysql.connector as connector
db = connector.connect(user='root',
                       password='3464',
                       host='127.0.0.1',
                       database='python_db')
cursor = db.cursor()
args = ("Nadeem",)
cursor.execute("Insert into demo(name) values ( %s )", args)
if cursor.lastrowid:
    print("Address Successfully Inserted")
    print('last insert id', cursor.lastrowid)
else:
    print('last insert id not found')

db.commit()
db.close()