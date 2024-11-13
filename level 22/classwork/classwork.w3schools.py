# all examples from w3schools
# append() 
# adds an inputed variable in the list
print("--------------------------------------------------------")
append_example_list = ["konti","konstnatine"]
append_example_list.append("kontio")
print(append_example_list)
print()
# clear()
# removes all items from the list
clear_example_list = [1,2,3,4,5,6,7,8,9,10]
clear_example_list.clear()
print(clear_example_list)
print()
# boom!
# copy copies the list and outputs it!
copy_exaple_list = ["copy 1","copy 2","copy 3","copy 4",]
# all of this is about to get copied
# this is the first list!
print(copy_exaple_list)
x = copy_exaple_list.copy()
print(x)
print()
# EZ
# now time for count()!
fruits = ["apple", "banana", "cherry","cherry"]
# cherry comes up in the list TWO times!
z = fruits.count("cherry")

print(z)
print()
# now time for extend()
# with extend you can combine list AKA extending them!
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

print()

# You can combine cars with fruits!
# index we all know this 
fruits = ['apple', 'banana', 'cherry']

y = fruits.index("cherry")

print(y)
print()
# cherry is the second index!
# insert puts the orange in the 1st index
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)
# yea pretty lame
# now time for pop!
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)
print()
# removed banana!
# next up remove()
# basically pop but NO INDEX you can just say the name!

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)
print()
# reverse() 
# THE NAME TELLS YOU WHAT IT DOES!!!!!
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)
print()
# LAST BUT NOT LEAST SORT()

Nums = [10,9,8,7,6,5,4,3,2,1]

Nums.sort()

print(Nums)
# it just sorts them
print("--------------------------------------------------------")