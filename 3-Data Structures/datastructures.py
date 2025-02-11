# #lists in python

# list = [1,2,3,4,5]
# print(type(list))

# fruits = ['apple', 'banana', 'cherry']

# fruits.append("orange")
# print(fruits)

# print(fruits[-1])
# print(fruits[1:3])

# #modifying the list elements
# fruits[1] = "mango"
# print(fruits)

# fruits.insert(1, "grapes")
# #list methods
# #append() - adds an element to the end of the list
# fruits.append("kiwi")

# #insert() - adds an element at the specified position
# fruits.insert(1, "watermelon")

# fruits.remove("banana")
# #removes the first occurence of the element with the specified value



# tuple = (1,2,3,4,5)#Sets

# print(type(tuple))

# set = {1,2,3,4,5}

# #dictionaries

# [] ,() ,{}

student ={"name":"John", "age":25, "courses":["Math", "CompSci"]}


print(student["name"])
print(student["courses"][0])
student["name"] = "savi saluwadana"

print(student["name"])
student["phone"] = "0712345678"
print(student["phone"])

keys = student.keys()
print(keys)
# print(student.keys())
print(student.values())
print(student.items())
