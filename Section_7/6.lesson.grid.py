

# data_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     ["network_in", "network_out", "servout_timeout"]
# ]
# row= data_grid[1]
# value = data_grid[1][1]
# print("row :", row, "value:", value)

employee_data= [
    ["IT", 4000, 101, 'Active'],
    ["HR", 5000, 102, 'Inctive'],
    ["IT", 6000, 103, 'Active'],
    ["Sales", 3500, 104, 'Active']
]
# SALARIES = [row[1] for row in employee_data]
# print(SALARIES)
# it_SALARIES = [row[1] for row in employee_data if row[0]== "IT"]
# print(it_SALARIES)

# average_salary = sum(it_SALARIES)/len(it_SALARIES)
# print (f" the average salary :{average_salary}")
department = set([emp[0] for emp in employee_data])  # provides unique values
print(department)

adjusted_salaries = [employee[1] + 5000 for employee in employee_data ]
print(adjusted_salaries)
it_dept = [employee[1] + 5000 for employee in employee_data if employee[0] == "IT" ]
print(it_dept)
high_employee_salary = [employee for employee in employee_data if employee[1]> 2500]
print(high_employee_salary)