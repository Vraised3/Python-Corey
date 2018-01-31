class Employee:

    raise_amount = 1.04  # Same for all instances, i.e. class variable
    # Class variable is the default for instances and class call

    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1  # Increments in each instance

    def fullname(self):
        print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Vishnu', 'V', 50000)
emp_2 = Employee('Test', 'Case', 60000)

# print(emp_1.__dict__) # No raise amount
# print(Employee.__dict__) # Raise amount attribute exists

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06  # Creates raise amount attribute for only emp_1

print(emp_1.__dict__)
print(Employee.__dict__)

# When an instance tries to access an attribute it looks at class variables
# if it is not present in the class, it see if it is present within the instance

print(Employee.raise_amount)
print(emp_1.pay)
print(emp_1.raise_amount)  # instance doesn't have this attribute yet
emp_1.apply_raise()  # Accessing the class's raise amount attribute
print(emp_1.pay)
print(emp_2.pay)
print(Employee.num_of_emps)
