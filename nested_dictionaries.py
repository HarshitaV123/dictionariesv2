# empty nested dictionary
my_dict={"dict1":{},"dict2":{}}
print(my_dict)

# nested diction having same keys
my_dict2={"dict1":{"name": "Bob","place":"New York"},"dict2":{"name":"Sally","place":"Idaho"}}
print(my_dict2)

# nested dictionary having different keys
my_dict3={"dict1":{"pet":"dog","color":"blue"},"dict2":{"name":"Susan","season":"spring"}}
print (my_dict3)

# accessing value from a nested dictionary
pet=my_dict3["dict1"]["pet"]
print("I have a "+pet)