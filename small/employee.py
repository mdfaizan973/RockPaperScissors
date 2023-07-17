
def average_age_of_employees_with_s_job_title(company):
    emp_s = [emp['age'] for emp in company['employees']
      .values() if emp['job_title'].lower().startswith('s')]
    ages = sum(emp_s) / len(emp_s) if emp_s else 0
    print(ages)
      


company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}

print(average_age_of_employees_with_s_job_title(company))  
