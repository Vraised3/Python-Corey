#########################################################LISTS##########################################
courses = ['History', 'Math', 'Physics', 'Compsci']
print(courses[2])  # Index starts at zero
print(courses[-1])  # -1 is the last item
# print(courses[4]) Index is out of range
print(courses[:2])  # Second index is not inclusive, i.e. [0,1] not 2
print(courses[1:])
courses.append('art')  # Add art to the end
print(courses)
courses.insert(0, 'art')  # Place in Index and shift all from Index onwards right
print(courses)
courses.remove('art')  # Will remove first art
print(courses, '\n')

courses_2 = courses[:3]
print(courses_2)
courses_2.insert(0, courses[3:])  # List within a list
print(courses_2)
print(courses_2[0])  # Sublist indexed
# courses_2.remove()
courses.extend(courses_2[:3])  # Does not create sublist within list
print(courses, '\n')

popped = courses.pop()  # Takes away the last value from courses and stores in popped
print(popped)
print(courses, '\n')

courses.reverse()  # Reverse the list
print(courses)
courses = ['History', 'Math', 'Physics', 'Compsci']
num = [1, 5, 2, 4, 3]
courses.sort()  # Strings sorted in Alphabetical order
num.sort()  # Numbers sorted in Numerical Order
print(courses)
print(num, '\n')

courses = ['History', 'Math', 'Physics', 'Compsci']
num = [1, 5, 2, 4, 3]
courses.sort(reverse=True)  # Single command to sort in reverse order
num.sort(reverse=True)
print(courses)
print(num, '\n')

courses = ['History', 'Math', 'Physics', 'Compsci']
num = [1, 5, 2, 4, 3]
sorted_courses = sorted(courses)
print(sorted_courses)
print(courses.index('Compsci'))  # Shows index for particular value
print('Math' in courses, '\n')  # Check if value is in list

for item in courses:  # Loop through values in list
    print(item)  # Print statement goes to new line by default
print('\n')

for index, course in enumerate(courses, start=1):  # Enumerates index and starts at 1 - user defines unless default
    print(index, course)
print('\n')

courses = ['History', 'Math', 'Physics', 'Compsci']
courses_str = ' - '.join(courses)  # Add a seperator
print(courses_str, '\n')

new_list = courses_str.split(' - ')  # Returns original list, splits by seperator
print(courses_str)
print(new_list, '\n')

###################################################TUPLES##############################################################
# Lists are Mutable, Tuples are Immutable
list_1 = ['History', 'Math', 'Physics', 'Compsci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'art'

print(list_1)
print(list_2, '\n')  # Same because they're the same Mutable object

tuple_1 = ('History', 'Math', 'Physics', 'Compsci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'art'  # Immutable, does not support item assignment

print(tuple_1)
print(tuple_2, '\n')

##################################################SETS###############################################################
# Sets don't care about order - They are optimized for membership tests better than the others
cs_courses = {'History', 'Math', 'Physics', 'Compsci'}  # Order changes each time at initialization
art_courses = {'History', 'Math', 'Art', 'Design', 'Math'}  # Removes duplicates, i.e. Math

print(cs_courses)

print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))  # Exist in both
print(cs_courses.difference(art_courses))  # Not intersect
print(cs_courses.union(art_courses))  # All sets

#######################################################################################################################
# Empty Lists
empty_list = []
empty_list = list()

# Empty tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty sets
# empty_set = {} # Wrong, this will create empty dictionary
empty_set = set() # Right way
