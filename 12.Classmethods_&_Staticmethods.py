import datetime
# Python OOP


class Employee:
    # Regular methods in a class automatically take the instance as the first argument
    # To take a different argument than the instance we use class method
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod  # @ - decorator, altering such that we recieve class as first method instead of instance
    def set_raise_amt(cls, amount):  # (class variable name, argument)
        cls.raise_amt = amount  # Affects the original class variable and makes all the instances follow

    @classmethod #Applies to class variables
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day): # Does not require self or cls
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Vishnu', 'V', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Employee.set_raise_amt(1.05) # same as Employye.raise_amt = 1.05
emp_1.set_raise_amt(1.05)  # Changes class variable, Affects the class and all instances, not just emp_1 instance

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
# print(emp_1.apply_raise())

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
