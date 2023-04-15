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

    @staticmethod

    def isopen(day):
        if day == 'sunday':
            return False
        else:
            return True


print(Employee.isopen('sunday'))
print(Employee.isopen('monday'))

