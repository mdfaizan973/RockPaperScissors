# Sample employee data
employees = [
    {'name': 'John', 'salary': 3000,"designation":"developer"},
    {'name': 'Ema', 'salary': 4000,"designation":"manager"},
    {'name': 'Kelly', 'salary': 3500,"designation":"tester"}
]

maxsalary = max(employees, key=lambda emp: emp['salary'])

print("Max Salary Person:", maxsalary['salary'])
