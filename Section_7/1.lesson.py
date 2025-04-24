#  input conversions

# temp = input("enter a number:")
# print(type(temp))
# result = 100 + int(temp)
# print("100 + {} = {}".format(temp, result))

# input example
 
# current_year = 2025
from datetime import datetime
current_year = datetime.now().year
birthdate = input ("Enter your birth year:\n")
age = current_year - int(birthdate)
print (f"Your agr is apprx: {age} yrs old")
