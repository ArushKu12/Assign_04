#Making a Class of Employee

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f" Salary of {self.name} has been updated to ${self.salary}")

    def show_info(self):
        print(f"The name of employee is {self.name}")
        print(f"Salary of {self.name} is ${self.salary}")

    def __del__(self):
        print(f"Record of employee {self.name} is deleted ")


employee_1 = Employee("Mehak", 40000)

employee_2 = Employee("Ashok", 50000)

employee_3 = Employee("Viren", 60000)

# part a of question

employee_1.update_salary(70000)

print()

# part b
del employee_3