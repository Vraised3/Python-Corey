class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):  # Used for debugging and logging, often used by other developers
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):  # Readable representation of the object and is meant for the ned user
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Vishnu', 'V', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1)  # Returns Employee object like just above when having __repr__ method

print(repr(emp_1))  # Or print(emp_1.__repr__)
print(str(emp_1))  # Or print(emp_1.__str__)

print(1 + 2)

print(int.__add__(1, 2))  # same as print(1+2)
print(str.__add__('1', '2'))

print(emp_1 + emp_2)  # Works using __add__

print(len('test'))
print('test'.__len__()) # Same as above

print(len(emp_1)) # Using __len__(self)
