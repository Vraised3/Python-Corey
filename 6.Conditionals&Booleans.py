language = 'Python'

if language == 'Python':  # Condition is true
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
# Python doesn't have Switch-Case statements as If-Elif-Else is enough

print('\n')

user = 'Admin'
logged_in = False

if user != 'Admin' or logged_in:
    print('Please Log In')
else:
    print('Welcome Admin')

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)  # False because a and b are two different objects
print(id(a))  # ID of a is different than ID of b ^
print(id(b))
b = a  # Now these are same objects in memory
print(a is b) # i.e. id(a) == id(b) is True
print(a == b,'\n')

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence
# Any empty sequence, For example, '', (), []
# Any empty mapping, for example, {}

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evalutated to False')
