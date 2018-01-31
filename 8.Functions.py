def hello_func1():
    pass  # Means don't do anything for now, so that it doesn't give errors


print(hello_func1(), '\n')  # None, since there is nothing in the function


def hello_func2():
    print('Hello Function\n')


hello_func2()


def hello_func3():
    return 'Hello Function\n'


print(hello_func3().upper())  # Can use methods on return variable


def hello_func4(greeting, name='You'):  # Default parameter for name
    return '{} {} Function.'.format(greeting, name)


print(hello_func4('Whatsupp', 'Vishnu'), '\n')  # Have to pass positional arguments before keyword arguments


def student_info(*args, **kwargs):  # Allows to accept an arbitrary number of positional or keyword arguemtns
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)  # Math and Art are printed as a tuple in the positional arguent, kwargs is a dictionary with keywords and values in the keyword argument
print('')

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(courses, info)  # Output {}, instead of passing the values in individually, it passed it both as positional arguments
print('')

student_info(*courses, **info)  # Output same as first, Upacks the values and passes them individually
print('')

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # List, First index is just a placeholder it is not going to be used.


def is_leap(year):
    """Return True for leap years, false for non-leap years."""  # Docstring for describing program
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2017, 2))
