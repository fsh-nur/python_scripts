# Python libraries and modules
# Extensive libraries in Python - External collections of useful functions and methods

# Python comes with some integrated libraries

from random import *
import math

print(random())

num_float = 235.33

print(math.floor(num_float))

# A module is a set of code or functions with the python extension (you can make your own modules)
# A library is a collection of related modules or packages
# Modules make is easier to read the code
# Libraries without using "from" can be quite hard to read
# Libraries must be installed first in our python project we usually use the pip command
# When a python programmer imports a module, the interpreter searches various locations for the module's definition or body
# When you install a library it only applies to a particular area.


# Modules

import os
import datetime, sys

working_dir = os.getcwd()
print(working_dir)

print(datetime.date.today())

print(sys.path)

def operating_system_information():
    print(os.cpu_count())

operating_system_information()

# pip - pythons packages manager

import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc.status_code)
print(requests_bbc.content)



