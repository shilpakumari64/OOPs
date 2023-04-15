class Employee:
    increment = 1.5
    no_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.4
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)


print(Employee.no_of_employee)
emp1 = Employee('shi', 'singh', 2000)
emp2 = Employee('sona', 'sis', 3000)
print(Employee.no_of_employee)
# print(emp1.salary)
# emp1.increase()
# print(emp1.salary)
