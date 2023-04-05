import os
import shutil

# prints message to terminal
# os.system('echo "Hello World!"')

# os module to manipulate directories
#
# # Directory
directory = "test_dir"
#
# # Path to parent dir
parent_dir = "C:/Users/fshei/Desktop/Python"
#
# # Path
#
path = os.path.join(parent_dir, directory)
#
# # Create the directory
#
# os.mkdir(path)
# print("Directory '% s' created" % directory)

# Put a file in the new directory

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(os.path.join(path, filename), "w") as file1:
    toFile = "content of the file is written here"
    file1.write(toFile)
print("File " + filename + " created in " + directory + " folder")