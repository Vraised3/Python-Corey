student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}  # 'key':'value'
# Keys can be any mutable datatype
print(student)
print(student['courses'])
print(student.get('phone', 'Not found'))  # Prints none by default instead of error

student['phone'] = '555-555'  # Appends key and keyvalue
student['name'] = 'Jane'  # Update keyvalue
print(student, '\n')

student.update({'name': 'John', 'age': 26, 'phone': '555-5555'})
del student['age']  # Delete value
print(student)
student['age'] = 26
print(student)
age = student.pop('age')  # Return and delete value
print(age)
print(student, '/n')

print(len(student))
print(student.keys())  # Returns Keys
print(student.values())  # Returns Values
print(student.items())  # Key and value pairs
for key, items in student.items():
    print(key, items)
