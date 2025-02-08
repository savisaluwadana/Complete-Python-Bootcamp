#lists in python

list = [1,2,3,4,5]
print(type(list))

fruits = ['apple', 'banana', 'cherry']

fruits.append("orange")
print(fruits)

print(fruits[-1])
print(fruits[1:3])

#modifying the list elements
fruits[1] = "mango"
print(fruits)

fruits.insert(1, "grapes")
#list methods
#append() - adds an element to the end of the list
fruits.append("kiwi")

#insert() - adds an element at the specified position
fruits.insert(1, "watermelon")

fruits.remove("banana")
#removes the first occurence of the element with the specified value

