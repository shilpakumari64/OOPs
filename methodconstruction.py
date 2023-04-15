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

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split('-')
        return cls(fname,lname,salary)




emp1 = Employee('shi', 'singh', 2000)
emp2 = Employee('sona', 'sis', 3000)
emp3 = Employee.from_str('sasa-sosO-10000')

print(emp3.lname)

