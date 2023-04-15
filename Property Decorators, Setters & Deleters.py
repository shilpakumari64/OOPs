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
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split('-')
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day == 'sunday':
            return False
        else:
            return True

    @property
    def email(self):
        if self.fname == None:
             return 'Email invalid'
        else:
            return self.fname + self.lname + '@gmail.com'


    @email.setter
    def email(self, given_email):
        new_list = given_email.split('@')[0].split('.')
        self.fname = new_list[0]
        self.lname = new_list[1]

    @email.deleter


    def email(self):
        self.fname = None
        self.lname = None


if __name__ == '__main__':
    shilpa = Employee('sis', 'so', 9000)
    sona = Employee('sos', 's', 8000)
    print(shilpa.email,sona.email)
    sona.lname = 'khanna'
    print(sona.email)
    shilpa.email ='lol.lik@gmail.com'
    print(shilpa.email)
    del shilpa.email
    print(shilpa.email)
