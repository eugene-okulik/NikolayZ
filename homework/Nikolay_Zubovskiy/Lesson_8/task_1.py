import random

employee_salary = [(2700, True), (800, False), (3000, True)]

for salary, bonus in employee_salary:
    if bonus:
        total_salary = int(salary * (1 + random.randint(0, 100) / 100))
        print(f"{salary}, {bonus} - '${total_salary}'")
    else:
       print(f"{salary}, {bonus} - '${salary}'")
