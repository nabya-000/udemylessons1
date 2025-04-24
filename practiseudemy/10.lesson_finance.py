
cus_name = 'John Smith'
cus_id = '12345'
cus_balance = 45.67
print ("cus_name: %s , cus_id: %s" % (cus_name, cus_id ))

report_line = 'name: {1}, Balance :${0}'.format (cus_name,cus_balance)
print(report_line)

revenue = 12386.8765
formatted_rev = 'total revenue: ${:,.2f}'.format(revenue)
print(formatted_rev)

text = " python "
new_text = text.ljust(10,"$")
print (new_text)
print (text.center(10,'^'))
print (text.strip())

num ="45"
print (num.zfill(6))

# maketrans() and translate() creates and applies tralslation

trans = str.maketrans('aeiou', '12345')
texts = "hello world"
translated = texts.translate(trans)
print(translated)

# string eg.

employee_name ='John Smith'
emp_dept = 'information technology'

seq_query = """
SELECT
    employee_name
    emp_dept
    hire date
from
    employees
where
    department = 'IT'
    AND DATE >= 2025-01-01

""" 