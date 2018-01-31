# Object-Oriented programming with python
class Employee:  # Easy to reuse and build upon
    # pass  # For blank class
    # a = 'hello' # Attribute
    # def fun: # Method
    def __init__(self, first, last, pay):  # (Instance, other arguents)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Vishnu', 'v', 50000)
emp_2 = Employee('Test', 'User', 60000)  # Own unique instances, i.e. different addresses

# emp_1.first = 'Vishnu'
# emp_1.last = 'V'
# emp_1.email = 'Vishnu.V@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000  # Too tiresome to do

print(emp_1.email)
print(emp_2.email)

# print('{} {}'.format(emp_1.first,emp_1.last)) # Instead
print(emp_1.fullname())  # Easier and through an instance
print(Employee.fullname(emp_1))  # Same but need to pass instance as argument
