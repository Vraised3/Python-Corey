import my_module as mm  # Gives aka

courses = ['History', 'Math', 'Physics', 'Compsci']
# Module_Name.Function

index = mm.find_index(courses, 'Math')
print(index, '\n')

from my_module import find_index, test  # Only give access to function and variable in my_module

index = find_index(courses, 'Physics')
print(index)
print(test, '\n')

from my_module import *  # Import all, frowned upon because reader cannot tell which module it is ffrom
index = find_index(courses, 'Compsci')
print(index)
print(test)


##################################Standard Libraries##############################
import sys
print(sys.path)  # All Python compiler paths in a list
# If a module is not in the path, one can append the path which has the module
# sys.path.append('/Path') otherwise add environment varible to windows

import random  # Standard library module
random_courses = random.choice(courses)
print(random_courses, '\n')

import math  # Standard math modules
rads = math.radians(90)
print(rads)
print(math.sin(rads), '\n')

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2017), '\n')

import os
print(os.getcwd())
print(os.__file__)  # Location of file on filesystem

import antigravity
