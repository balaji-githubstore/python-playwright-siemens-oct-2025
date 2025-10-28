import employee_module

employee_module.Employee.company_name="Siemens"

# 1st object creation
emp1=employee_module.Employee(101,"sds",444)
emp2=employee_module.Employee()

emp1.emp_id=101
emp1.emp_Name="John"
emp1.emp_salary=2000

emp2.display_employee_details()
emp1.display_employee_details()

employee_module.Employee.display_company_Details()