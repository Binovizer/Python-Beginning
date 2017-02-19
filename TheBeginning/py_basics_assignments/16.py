emp_id = 1001
basic_salary = 15000
allowances = 6000

monthly_gross_salary = basic_salary + allowances
# print("Monthly Gross Salary : ",monthly_gross_salary)

if (monthly_gross_salary > 20000):
    tax_percentage = 30
elif (monthly_gross_salary > 10000):
    tax_percentage = 20
elif (monthly_gross_salary > 5000):
    tax_percentage = 10
else:
    tax_percentage = 0

income_tax = monthly_gross_salary * tax_percentage / 100
net_pay = monthly_gross_salary - income_tax

print("Employee Id : ",emp_id)
print("Basic salary : ",basic_salary)
print("Allowances : ",allowances)
print("Gross Pay : ",monthly_gross_salary)
print("Income tax : ",income_tax)
print("Net Pay : ",net_pay)