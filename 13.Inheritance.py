# Inherit Attributes and Methods from parent class
class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # class subclass(inherited class)
    raise_amt = 1.10  # Class call uses this over Employee class raise_amt

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Passes to the Employee init method and let that handle it
        self.prog_lang = prog_lang
    # pass  # Walks up method resolution order


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if(employees is None):
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if(emp not in self.employees):
            self.employees.append(emp)

    def remove_emp(self, emp):
        if(emp in self.employees):
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer("Vishnu", "V", 50000, 'Python')
dev_2 = Developer("Test", 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

# print(dev_1.prog_lang)

# print(dev_1.email)
# # print(help(Developer)) # Shows method resolution order
# dev_1.apply_raise()
# print(dev_1.pay)
