# # collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO Duplicates
# Tuple = () ordered and unchangable. Duplicates OK. Faster

# fruits= ["apple","orange","banana", "coconut"]
# print(dir(fruits))
# dir lists out all atrributes that could be used in a list

# print(help(fruits))
# gives helpful documentation 

# print(len(fruits))
# gives you the length 

# print("apple" in fruits)
# tells you if an element is in something in boolean form

# index can reassign a value replaces a value
# fruits[1] = "pineapple"
# fruits[-1] = "cherry"

# append adds a element to the end of a list
# fruits.append("pineapple") 

# removes an element in a list
# fruits.remove("apple") 

# inserts an element in between
# fruits.insert(0,"pineapple") 

# puts element in alphabetical order
# fruits.sort()

# reverses the order
# fruits.reverse()

# these two can give reverse alphabetical order
# fruits.sort()
# fruits.reverse()

# clears the list 
# fruits.clear()

# print(fruits)

# gives you the place in the list of a certain element
# print(fruits.index("apple"))

# print(fruits[0])
# for fruit in fruits:
#     print(fruit)
    # indet in for loops 

# cars= ["Ford","Volvo", "BMW"]
# # # add 4 new cars in the list 
# # cars.append("Honda")
# # cars.append("bugitti")
# # cars.append("Toyota")
# # # cars.append("Chevy")print out the list of cars in an f-string 
# # # that say "the cars in the list are:" 
# # print(f"the cars in the list are: {cars}")

# # cars[-1]= "austin martin"
# # print(f"the cars are: {cars}")

# # cars.insert(1,"tesla")
# # print(f"the cars now including tesla are: {cars}")

# # print(cars.remove("BMW"))
# # print(f"the list of cars without including BMW are: {cars}")

# # print("Ford" in cars)

# for car in cars: 
#     requestCar= input("Enter a car:")
#     cars.append(requestCar)
#     print(f"The cars in the list are:{cars}")
#     if len(cars) > 10:
#         print("You have reached the maxium number of cars")
#         break

# friends = ["Sam"]
# friends.append("Oscar")
# friends.append("Juan")
# friends.append("Luke")
# friends.append("Chris")
# print(f"The list of friends are: {friends}")

# friends[-1]= "Lucas"
# print(f"the list of friends with are: {friends}")

# friends.insert(2,"Waldo")


# sets 
# sets are unordered and unindexed 
# they are defined using curly brackets 
# they do not allow duplicates 
fruits = {"apple", " banana", "mango", "cherry", "watermelon"}
print(fruits)

# print(dir(fruits)) 
# # methdos that can be used with sets

# print(help(fruits))
# # documentation/methods that can be used with sets

# print(len(fruits))
# # number of elements in a set 
# print("volvo" in fruits) 
# # check if an element is in the set 

# print(fruits.add("orange"))
# # adds an element 

# print(fruits.update(["orange" , "kiwi", "pineapple"]))

# print(fruits.remove("apple"))
# # remove an element 

# print(fruits.pop())
# # remove last element

# print(fruits.clear())
# # clears the set 

# social_security_numbers  = {123456789, 987654321, 12345678}

# print(social_security_numbers.pop())

# print(social_security_numbers)

# print(social_security_numbers.add(345678901))
# print(social_security_numbers)
# social_security_numbers.add(123456789)
# print(social_security_numbers)

example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)      
# print(example_tuple)
# print(example_tuple.count(2))
# # counts number of times the number 2 shows up 
# print(dir(example_tuple))
# # # methdos that can be used with sets

# print(help(example_tuple))
# # documentation/methods in tuple 

# print(len(example_tuple))
# # number of elements in a tuple 

# print(2 in example_tuple)
# # check if an element is in the tuple 

# # tuples are useful when you want to store a collection of items that should not be changed
# # such as days of the week, months of the year, etc. 
# # if you want to find the index of a value in a tuple
# # you cant index sets
# print(example_tuple.index(2))

# lymeric = "peter piper picked a peck of pickled peppers peppers" 

# # convert string to a tuple 
# # split it first
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)

# # find how many times the letter "p" appears in the tuple 
# print(lymeric_tuple.count("peck"))

# print(lymeric_tuple.count("peppers"))

# # loops with tuples 
# for item in example_tuple:
#     print(item)

# dictionary 
# dictionaries are unorderdered, changeable and index 
# they are defined using curly brackets 
# they have keys and values 
# keys are unique 
# values can be of any data type 
    
capitals = { "Kenya":"Nairobi",
             "Uganda" : "Kampala",
             "Tanzania" : "dodoma",
             "Rwanda" : "KIigali",
             "China" : "Beijing" ,
             "USA" : "Washington DC",}

print(capitals)
# print(dir(example_tuple))
#  methdos that can be used with dictionary

# print(help(example_tuple))
# documentation/methods that can be used with dictionaries

# print(len(example_tuple))
# if you want to check the value of a key in the dictionary

print(capitals["Kenya"])
print(capitals.get["Kenya"])

# add an item to the dictionary 
capitals["South Africa"] = "Pretoria"
print(capitals)

capitals.update({"Nigeria":"Abuja"})
print(capitals)

capitals.update({"Japan":"Tokyo"})
capitals.update({"Spain":"Madrid"})
capitals.update({"Korea":"Seoul"})
print(capitals)

# capitals.clear() 

# loop through the dictionary 
for key in capitals:
    print(f"these are the {key}")

# print the values in the dictiobary
for value in capitals.values():
    print(value)    

items_all= capitals.items() #key value pairs
for key, value in items_all:
    print(f"{key} is the capital of {value}")
