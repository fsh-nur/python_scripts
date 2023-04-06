import json
import os
import sys
import yaml

# check there is a file passed
#
# if len(sys.argv) > 1:
#     # opening the file
#     if os.path.exists(sys.argv[1]):
#         source_file = open(sys.argv[1], "r")
#         source_content = json.load(source_file)
#         source_file.close()
#     # if the file isn't found
#     else:
#         print("ERROR: " + sys.argv[1] + " not found")
#         exit(1)
#
# else:
#     print("Wrong execution format")
#
# # processing the coversion
# output = yaml.dump(source_content)

# target_file = open(sys.argv[2], "w")
# target_file.write(output)
# target_file.close()

# if len(sys.argv) > 1:
#     if os.path.exists(sys.argv[2]):
#         source_file = open(sys.argv[2], "r")
#         source_content = yaml.load(source_file)
#         source_file.close()
#     else:
#         print("ERROR: " + sys.argv[2] + " not found")
#         exit(2)
# else:
#     print("Wrong execution format")
#
# output = json.(source_content)
#
# target_file = open(sys.argv[1], "w")
# target_file.write(output)
# target_file.close()
