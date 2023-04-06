import json
import os

# json = json.loads(open("C:/Users/fshei/Desktop/Python/scripting/example.json").read())
# value = json['name']
# print(value)


# Script to create absolute path variable
script_dir = os.path.dirname(__file__)

print("The script is located at: " + script_dir)
script_absolute_path = os.path.join(script_dir, 'example.json')
print("The script path is: " + script_absolute_path)

# script parse

json = json.loads(open(script_absolute_path).read())
value = json['name']
print(value)

# Loop through json keys and values

for key in json:
    value = json[key]
    print("The key and value are ({}) = ({})".format(key, value))
