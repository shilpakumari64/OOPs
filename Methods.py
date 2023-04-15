class Employee:
    increment = 1.5
    no_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

        Employee.no_of_employee += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod

    def change_increment(cls, amount):
        cls.increment = amount


emp1 = Employee('shi', 'singh', 2000)
emp2 = Employee('sona', 'sis', 3000)

print(emp1.salary)
emp1.change_increment(2)
emp1.increase()
print(emp1.salary)
