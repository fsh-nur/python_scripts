# Python scripting

# Easy to understand
# Many libraries
# Large community
# Language interprability

# Why do we care about scripting?

# Use python to automate tasks that I would have to do manually, such as creating a file or folder.

# Automate repetitive manual tasks using code

# Some examples of things we can write scripts for as DevOps engineers:

# Python to query a database
# Write Python script to execute a shell command
# Python to create a backup
# Python script to fetch I.P's addresses of an autoscaling
# Python scri[t to check the expiry date of an SSL certificate

# Seven in built modules that allow us to do some interesting things:

# sys
# os
# subprocess
# math
# random
# datetime
# json

# sys module
#
# import sys
# print(sys.version)
#
# # os module
# import os
# print(os.getcwd())
#
# os.chdir("C:/Users/fshei/Desktop/Python/")
# print(os.getcwd())
#
# os.rmdir("new_dir")
#

# subprocess module
# import subprocess

# Be careful to not create an infinite loop
# subprocess.run(["python", "hello_world.py"])

# math module

import math


pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

# random module

import random
randum = random.randrange(1, 10)

print(randum)

# datetime module

import datetime

whatisthedate = datetime.datetime.now()

print(whatisthedate)

#JSON module
import json

x = {
"name": "John",
    "age": 30,
    "city": "London"

}

y = json.dumps(x)
print(y)