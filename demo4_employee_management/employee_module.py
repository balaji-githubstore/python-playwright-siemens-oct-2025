class Employee:
    company_name = None

    # constructor
    def __init__(self,emp_id=None,emp_Name=None,emp_salary=None):
        self.emp_id = emp_id
        self.emp_Name = emp_Name
        self.emp_salary = emp_salary

    def display_employee_details(self):
        print(self.emp_id)
        print(self.emp_Name)
        print(self.emp_salary)
        print(Employee.company_name)

    @staticmethod
    def display_company_Details():
        print(Employee.company_name)

    @property
    def get_emp_id(self):
        return self.emp_id





