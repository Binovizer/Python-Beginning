import mysql.connector as connector
class AdminUtil:
    
    @staticmethod
    def printClosedAccounts():
        db = connector.connect(user='root',
                                   password='3464',
                                   host='127.0.0.1',
                                   database='python_bank_project')
        cursor = db.cursor()
        args = ("C",)
        cursor.execute("Select account_no, account_type, opening_date, closed_date from account where status = %s ", args)
        results = cursor.fetchall();
        if len(results) > 0:
            print('{0:37}  {1:14}  {2:13}  {3:13}'.format("Account No.", "Account Type", "Opening Date", "Closed Date"))
            for row in results:
                print("{0:37}  {1:14}  {2:13}  {3:13}".format(str(row[0]), str(row[1]), str(row[2]), str(row[3])))
        db.close()