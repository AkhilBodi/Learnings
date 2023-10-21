#                                           --------------------- CHAPTER 1 - Getting Started---------------------
# print("Hello Python Interpreter") 

#                                           --------------------- CHAPTER 2 - Variables and Simple Data Types ---------------------

# variables
# message = "Hello Python world!"
# print(message)

# message = "Hello Python Crash Course world"
# print(message)

# strings
# name = "ada lovelace"
# print(name.title())
# print(name.upper())
# print(name.lower())

# Using Variables in Strings
# first_name = "akhil"
# last_name = "bodi"
# full_name = f"{first_name} {last_name}" # f-­strings
# print(full_name)
# message = f"Hello, {full_name.title()}!"
# print(message)

# print("Python")
# print("\tPython") # tab
# print("My friends are: \nmahesh\nvamshi\nmyself") # newline
# print("My friends are: \n\tmahesh\n\tvamshi\n\tmyself") # newline & tab

# language = "python "
# print(language)
# print(language.rstrip()) # rstrip()
# language = " python"
# print(language)
# print(language.lstrip()) #lstrip()

#Try It Yourself
# name = input()
# message = f"Hello {name},would you like to learn some Python today?"
# print(message)

# name = input()
# print(name.lower())
# print(name.upper())
# print(name.title())

# name = input()
# quote = f'{name} once said, “A person who never made a mistake never tried anything new.”'
# print(quote)

# famous_person = input() # Akhil Bodi Here!
# message = f'{famous_person} said "The less the friends the more the success"'
# print(message)

# name = "   \t\nAkhil   "
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())

# Numbers

#Integers
# print(2 + 3) #add
# print(3 - 2) #subtract
# print(2 * 3) #multiply
# print(3 / 2) #divide
# print(3**2) #exponent
# print(2 + 3*4)
# print((2 + 3) * 4) #order of expression

#Floats
# print(0.1 + 0.1)
# print(2 * 0.1)
# print(0.2 + 0.1)
# print(3 * 0.1)

#Integers and Floats
# print(4/2) # div between int gives float
# print(1 + 2.0)
# print(3.0 ** 2)

# universe_age = 14_000_000_000 # group digits using underscores
# print(universe_age)

#Multiple Assignment 
# x, y, z = 1, 0, 1 # using just a single line.
# print(x)
# print(y)
# print(z)

#Constants
# MAX_CONNECTIONS = 5000 # Python pro-grammers use all capital letters to indicate a variable should be treated as a constant and never be changed

# Try It Yourself
# print(5 + 3)
# print(10 - 2)
# print(2 * 2 * 2)
# print(64/8)

# favorite_number = 8
# message = f"my favorite number is {2 + 8 - 1 * 2}"
# print(message)

# Comments
# How Do You Write Comments?
# In Python, the hash mark (#) indicates a comment. Anything following a hash mark in your code is ignored by the Python interpreter

# The main reason to write comments is to explain what your code is supposed to do and how you are making it work.
# import this # The Zen of Python


#                                           --------------------- CHAPTER 3 - Introducing Lists ---------------------

# names = ['sai', 'saratchandra', 'phaneendra', 'akhil']
# print(names)

# Accessing Elements in a List using indesx number
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# print(names[2].title()) # formatting the element

#negative indexing
# print(names[-1])
# print(names[-2])
# print(names[-3])
# print(names[-4])

#Using Individual Values from a List
# intro = f"My name is {names[3].title()}."
# print(intro)

# Changing, Adding, and Removing Elements

#Modifying Elements in a List
# cars = ["skoda","mahindra","tata","suzuki"]
# print(cars)
# cars[3] = "hyundai"
# print(cars)

# Adding Elements to a List

#Appending Elements to the End of a List
# cars = ["skoda","mahindra","tata","suzuki"]
# cars.append("hyundai")
# print(cars)
# cars = []
# cars.append("skoda")
# cars.append("mahindra")
# cars.append("tata")
# cars.append("suzuki")
# cars.append("hyundai")
# print(cars)

#Inserting Elements into a List
# cars = ["skoda","mahindra","tata","suzuki"]
# cars.insert(3,"hyundai")
# print(cars)

# Removing Elements from a List

#Removing an Item Using the del Statement
# cars = ["skoda","mahindra","tata","suzuki","hyundai"]
# del cars[-1]
# print(cars)
# del cars[0]
# print(cars)

#Removing an Item Using the pop() Method
# cars = ["skoda","mahindra","tata","suzuki","hyundai"]
# pop_car = cars.pop()
# print(cars)
# # print(pop_car)
# print(f"{pop_car.title()} is one of my favorites.")

#Popping Items from any Position in a List
# first_pos = cars.pop(0)
# print(f"My first car was {first_pos}.")

#Removing an Item by Value
# print(cars)
# cars.remove('suzuki')
# print(cars)

# expensive = 'suzuki'
# cars.remove(expensive)
# print(f"\n{cars}")
# print(f"\n{expensive.title()} is too expensive for me.")

# Try It Yourself
# guest_list = ["mahesh","tarak","krishna"]
# print(f"\nHey {guest_list[0].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[1].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[2].title()}. Here's your invitation to the dinner at my place tomorrow.")

# print(f"\n{guest_list[2].title()} cannot make it tomorrow for dinner.")

# guest_list[2] = "Raja"
# print(f"\nHey {guest_list[0].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[1].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[2].title()}. Here's your invitation to the dinner at my place tomorrow.")

# print("Hey everyone good news. We found a bigger dinner table")
# guest_list.insert(0,"akhil")
# guest_list.insert(2,"mani")
# guest_list.append("nani")
# print(f"\nHey {guest_list[0].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[1].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[2].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[3].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[4].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[5].title()}. Here's your invitation to the dinner at my place tomorrow.")

# print("Sorry. The table is only for two.")
# guest_list.pop()
# guest_list.pop()
# guest_list.pop()
# guest_list.pop()

# print(f"\nHey {guest_list[0].title()}. Here's your invitation to the dinner at my place tomorrow.")
# print(f"\nHey {guest_list[1].title()}. Here's your invitation to the dinner at my place tomorrow.")

# del guest_list[0]
# del guest_list[0]
# print(guest_list)

# Organizing a List

#Sorting a List Permanently with the sort() Method
# cars = ["skoda","mahindra","tata","suzuki","hyundai"]
# print(cars)
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

#Sorting a List Temporarily with the sorted() Function
# print(f"original: {cars}")
# print(f"sorted: {sorted(cars)}")
# print(f"reverse sorted: {sorted(cars,reverse=True)}")
# print(f"original: {cars}")

#Printing a List in Reverse Order
# print(cars)
# cars.reverse()
# print(cars)
# cars.reverse()
# print(cars)

#Finding the Length of a List
# print(len(cars))


#                                           --------------------- CHAPTER 4 - Working with Lists ---------------------

# friends = ["akhil","mahesh","vamshi"]
# for friend in friends:
    # print(friend)
    # print(f"Hi {friend.title()}. How are you? ")
    # print(f"Been waiting for you. Are you ready {friend.title()}?\n") 

# print("Let's Go!")

#Try It Yourself
# pizzas = ["veg pizza","paneer pizza","double cheese pizza"]
# for pizza in pizzas:
#     print(pizza.title())
#     print(f"I like {pizza.title()}.")
# print(f"I really love {pizzas[0].title()}")
# print(f"I really love {pizzas[1].title()}")
# print(f"I really love {pizzas[2].title()}")

# animals = ["dog","cat","parrot"]
# for animal in animals:
#     # print(animal.title())
#     print(f"A {animal.title()} would make a great pet.")

# print(f"{animals[0].title()},{animals[1].title()},{animals[2].title()} - Any of these animals would make a great pet!")

# Making Numerical Lists

#Using the range() Function
# for value in range(1,5):   # off-by-one
#     print(value)

# for value in range(1,6): # n+1 to include the value
#     print(value)

#Using range() to Make a List of Numbers
# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2)) # skip numbers in a given range by passing a third argument to range()
# print(even_numbers)

# squares = []
# for value in range(1,11):   # finding the square of the numbers in the given range using two asterisks aka exponents
#     squares.append(value**2)
# print(squares)

#Simple Statistics with a List of Numbers
# digits = []
# for digit in range(0,10):
#     digits.append(digit)
# print(digits)
# print(min(digits))
# print(max(digits))
# print(sum(digits))


# List Comprehensions

# squares = [value**2 for value in range(1,11)]
# print(squares)

#Try It Yourself

# count = [num for num in range(1,21)]
# print(count)

# one_mil = list(range(1,1000001))
# for num in one_mil:
#     print(num)

# print(max(one_mil))
# print(min(one_mil))
# print(sum(one_mil)) 

# odd_num = list(range(1,21,2))
# for num in odd_num:
#     print(num)

# threes = list(range(3,31,3    ))
# for num in threes:
#     print(num)

# cubes = list(range(1,11))
# for num in cubes:
#     print(num**3)

# cubes = [num**3 for num in range(1,11)]
# print(cubes)


# Working with Part of a List

#Slicing a List
# players = ["gill","rohit","virat","rahul","sky"]
# print(players[0:3])
# print(players[:4])
# print(players[1:])
# print(players[-3:])
# print(players[0::2])

#Looping Through a Slice
# print("The first 3 players are : ")
# for player in players[0:3]:
#     print(player.title())

#Copying a List
# my_foods = ["dal","egg plant","curd"]
# friend_foods = my_foods[:]
# print(f"My foods are: \n{my_foods}")
# print(f"\nMy friend's foods are: \n{friend_foods}")

# my_foods.append("gulab jamun")
# friend_foods.append("jalebi")

# print(f"\nMy foods are: \n{my_foods}")
# print(f"\nMy friend's foods are: \n{friend_foods}")

# Try It Yourself
# print(f"The first three players are {players[:3]}")
# print(f"The middle three players are {players[1:4]}")
# print(f"The last three players are {players[2:]}")

# friend_pizzas = pizzas[:]
# pizzas.append("mix veg pizza")
# friend_pizzas.append("double crust cheese pizza")
# print(f"My favorite pizzas are: ")
# for pizza in pizzas:
#     print(pizza.title())

# print("My friend's favorite pizzas are : ")
# for friend_pizza in friend_pizzas:
#     print(friend_pizza.title())

# Tuples - immutable

# dimensions = (120,80)
# print(dimensions[0])
# print(dimensions[1])

# for dimension in dimensions:   #Looping Through All Values in a Tuple
#     print(dimension)

# print("\nOriginal dimensions are : ")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (150,100)   #Writing over a Tuple
# print("\nAltered dimensions are : ")
# for dimension in dimensions:
#     print(dimension)

# Try It Yourself
# buffet_menu = ("roti","dal","curry","rice","curd")
# print("Original Menu : ")
# for items in buffet_menu:
#     print(items)
# print("\nChanged Menu : ")
# # buffet_menu[0] = "naan" # doing this on-purpose
# buffet_menu = ("roti","dal","curry","sambar","dessert")
# for items in buffet_menu:
#     print(items)


#                                           --------------------- CHAPTER 5 - if Statements ---------------------

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# Conditional Tests

#Checking for Equality
# car = 'bmw'
# print(car == 'bmw') # True
# print(car == 'audi') # False

# print(car == 'BMW') # False - Testing for equality is case sensitive in Python
# print(car.upper() == 'BMW' ) # True - The test is now case insensitive

#Checking for Inequality
# toppings = 'mushrooms'

# if toppings != 'anchovies':
#     print("Hold the anchovies")

#Numerical Comparisons

# age = 20
# print(age == 20) # True
# print(age > 18) # True
# print(age < 20) # Flase as they both are equal

#Checking Multiple Conditions
    # Using and
# age1 = 20
# age2 = 22
# print((age1 > 18) and (age2 > 22)) # False - both individual tests must pass

    # Using or
# print((age1 > 18) or (age2 > 22)) # True - either or both of the individual tests must pass

#Checking Whether a Value Is in a List

# toppings = ["onions","tomato","greens"]
# print("onions" in toppings) # True - checks for the existence if present  prints true
# print("Extra cheese" in toppings) # False - checks for the existence if not present prints false

#Checking Whether a Value Is Not in a List

# blocked_users = ["Ajoe","Bjoe","Cjoe"]
# user = "Djoe"

# if user not in blocked_users:
#     print(f"{user.title()}, you can message.")

# Try It Yourself

# bike = "yamaha"
# print("Is bike == yamaha? I predit True.")
# print(bike == "yamaha")

# print("\nIs car == HD? I predit False.")
# print(bike == "HD")

# bike = "Yamaha"
# # print(bike.lower() == "yamaha")
# car = "audi"
# print(bike == "Yamaha" and car == "audi")
# print(bike == "yamaha" or car == "Audi")

# print("Ajoe" in blocked_users)
# print("Bjoe" not in blocked_users)


# if Statements

#Simple if Statements
# age = 19
# if age > 18:
#     print("You are eligible to vote.")

#if-else Statements
# age = 17
# if age > 18:
#     print("You are eligible to vote.")
# else:
#     print("Sorry, you are too young to vote.")


#The if-elif-else Chain

age = 14

# if age < 4:
#     print("Your entry is free!")
# elif age < 18:
#     print("Your entry costs $25")
# else:
#     print("Your entry costs $40")

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40

# print(f"You entry fee is ${price}")

#Using Multiple elif Blocks

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20

# print(f"You entry fee is ${price}")

#Omitting the else Block
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age > 65:
#     price = 20

# print(f"You entry fee is ${price}")

#Testing Multiple Conditions

# cart = ["pencil","pen","sharpner"]

# if "pencil" in cart:
#     print("pencil addded to cart.")
# if "eraser" in cart:
#     print("eraser addded to cart.")
# if "pen" in cart:
#     print("pen addded to cart.")
# if "sharpner" in cart:
#     print("sharpner addded to cart.")

# print("\nCart full")

# Try It Yourself

# alien_color = "green"

# if alien_color == "green":
#     print("You have earned 5 points.")

# alien_color = "yellow"
# if alien_color == "green":
#     print("You have earned 5 points.")

# alien_color = "green"
# if alien_color == "green":
#     print("You have earned 5 points.")
# elif alien_color == "yellow":
#     print("You have earned 10 points.")

# alien_color = "yellow"
# if alien_color == "green":
#     print("You have earned 5 points.")
# elif alien_color == "yellow":
#     print("You have earned 10 points.")

# alien_color = "red"
# if alien_color == "green":
#     print("You have earned 5 points.")
# elif alien_color == "yellow":
#     print("You have earned 10 points.")
# elif alien_color == "red":
#     print("You have earned 15 points.")
# else:
#     print("You have earned no points.")

# age = 19

# if age < 2:
#     category = "a baby"
# elif age == 2 or age < 4:
#     category = "a toddler"
# elif age == 4 or age < 13:
#     category = "a kid"
# elif age == 13 or age < 20:
#     category = "a teenager"
# elif age == 20 or age < 65:
#     category = "an adult"
# else:
#     category = "an elder"

# print(f"You are {category}")

# favorite_fruits = ["apple","tangerine","guava","watermelon"]

# if "apple" in favorite_fruits:
#     print("apple has been added")
# if "tangerine" in favorite_fruits:
#     print("tangerine has been added")
# if "papaya" in favorite_fruits:
#     print("papaya has been added")
# if "guava" in favorite_fruits:
#     print("guava has been added")
# if "watermelon" in favorite_fruits:
#     print("watermelon has been added")

# Using if Statements with Lists

#Checking for Special Items
# cart = ["pencil","pen","sharpner"]

# for item in cart:
#     print(f"{item} has been added to the cart.")

# cart = ["pencil","pen","eraser","sharpner"]

# for item in cart:
#     if item == "eraser":
#         print(f"Sorry. We are out of {item}")
#     else:
#         print(f"{item} has been added to the cart.")

# print("\nDone")

#Checking That a List Is Not Empty

# cart = []

# if cart:
#     for item in cart:
#         print(f"{item} has been added to the cart.")
#     print("\nDone.All items have been added to the cart!")
# else:
#     print("Are you sure to add nothing?")

#Using Multiple Lists

# available_items = ["pencil","pen","sharpner","ruled-books"]
# requested_items = ["pencil","eraser","ruler","sharpner"]

# for item in requested_items:
#     if item in available_items:
#         print(f"{item.title()} has been added to the cart.")
#     else:
#         print(f"Sorry we are out of {item.title()}")

# print("\nDone!")

# Try It Yourself

# usernames = ["alice","bob","jaden","admin"]
# for name in usernames:
#     if name == "admin":
#         print(f"Hello {name}, would you like to see a status report?")
#     else:
#         print(f"Hello {name.title()}, thank you for logging in again.")

# if usernames:
#     for name in usernames:
#         if name == "admin":
#             print(f"Hello {name}, would you like to see a status report?")
#         else:
#             print(f"Hello {name.title()}, thank you for logging in again.")
# else:
#     print("We need to find some users!")

# current_users = ["alice","bob","jaden","mike","sam"]
# new_users = ["Alice","rob","Jaden","nike","ram"]

# for name in new_users:
#     if name.lower() in current_users:
#         print("Please enter a new username.")
#     else:
#         print("The username has been added.")

# lst = [1,2,3,4,5,6,7,8,9]
# for num in lst:
#     if num == 1:
#         print("1st")
#     elif num == 2:
#         print("2nd")
#     elif num == 3:
#         print("3rd")
#     else:
#         print(f"{num}th")


#                                           --------------------- CHAPTER 6 - Dictionaries ---------------------

# A Simple Dictionary

# alien0 = {"color" : "green", "points" : 5}
# print(alien0['color'])
# print(alien0['points'])

#Accessing Values in a Dictionary

# points = alien0["points"]
# print(f"You have earned {points} points.")

#Adding New Key-Value Pairs

# alien0["x_position"] = 0
# alien0["y_position"] = 25
# print(alien0)

#Starting with an Empty Dictionary

# alien0 = {}
# alien0["color"] = "green"
# alien0["points"] = 5
# print(alien0)

#Modifying Values in a Dictionary
# print(f"The alien color is {alien0['color']}")

# alien0["color"] = "yellow"
# print(f"The alien color is {alien0['color']}")

# alien0 = {"x_position" : 0, "y_position" : 25, "speed" : "medium"}
# print(f"Original Position : {alien0['x_position']}")

# if alien0["speed"] == "slow":
#     x_increment = 1
# elif alien0["speed"] == "medium":
#     x_increment = 2
# else:
#     x_increment = 3

# alien0["x_position"] += x_increment
# print(f"New Position : {alien0['x_position']}") 

#Removing Key-Value Pairs
# alien0 = {'color': 'green', 'points': 5}
# print(alien0)

# del alien0['points']
# print(alien0)

# A Dictionary of Similar Objects
# favorite_languages ={
    # "alice" : "c",
    # "bob" :  "java" ,
    # "sam" : "go",
    # "akhil" : "python",
# }

# print(f"Akhil's favorite language is {favorite_languages['akhil'].title()}")

#Using get() to Access Values
# alien0 = {"color" : "green"}
# point_value = alien0.get('points', 'No point value assigned.')
# print(point_value)

#Try It Yourself

# person = {
#     "first_name" : "akhil",
#     "last_name" : "bodi",
#     "age" : "forever young",
#     "city" : "hyderabad"
# }

# print(person["first_name"].title())
# print(person["last_name"].title())
# print(person["age"])
# print(person["city"].title())

# fav_numbers = {
#     "alice" : "0",
#     "bob" :  "7" ,
#     "sam" : "4",
#     "akhil" : "3",
# }

# print(f"Alice favorite number is {fav_numbers['alice']}")
# print(f"Bob favorite number is {fav_numbers['bob']}")
# print(f"Sam favorite number is {fav_numbers['sam']}")
# print(f"Akhil favorite number is {fav_numbers['akhil']}")

# glossary = {
#     "print" : "Helps in displaying that which has been mentioned in the following parantheses on screen.",
#     "variable" : "Helps to store a value just like a container.",
#     "data type" : "Different types of data for different inputs such as strings,int,float etc,.",
#     "list" : "Helps in storing different types of data and is defined by square brackets.",
#     "loop" : "Helps in iterating individual value of a tuple, list, dictionary, etc,."
# }

# print(f"\nprint : {glossary['print']}")
# print(f"\nvariable : {glossary['variable']}")
# print(f"\ndata type : {glossary['data type']}")
# print(f"\nlist : {glossary['list']}")
# print(f"\nloop : {glossary['loop']}")

# Looping Through a Dictionary

#Looping Through All Key-Value Pairs

# user = {
#        "username" : "akhilbodi",
#        "first_name" : "Akhil",
#        "last_name" : "Bodi",
#         }
# for key,value in user.items():
#     print(f"\n{key} is the key : {value} is the value")

# fav_numbers = {
#     "alice" : "0",
#     "bob" :  "7" ,
#     "sam" : "4",
#     "akhil" : "3",
# }

# for name,number in fav_numbers.items():
#     print(f"{name} favorite number is {number}")

# for name in fav_numbers.keys():
#     print(name.title())
    
# friends = ["bob","akhil"]
# for name in fav_numbers.keys():
#     print(name.title())

#     if name in friends:
#         number = fav_numbers[name]
#         print(f"\t{name.title()}, so your favorite number is {number}?")

# if "Raju" not in fav_numbers.keys():
#     print("Raju, Please take the poll")

#Looping Through a Dictionary’s Keys in a Particular Order

# for name in sorted(fav_numbers.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

#Looping Through All Values in a Dictionary

# print("Users favorite numbers are:")
# for numbers in fav_numbers.values():
#     print(numbers)

# print("Users favorite numbers are:")
# for numbers in set(fav_numbers.values()):
#     print(numbers)

# Try It Yourself
# glossary = {
#     "print" : "Helps in displaying that which has been mentioned in the following parantheses on screen.",
#     "variable" : "Helps to store a value just like a container.",
#     "data type" : "Different types of data for different inputs such as strings,int,float etc,.",
#     "list" : "Helps in storing different types of data and is defined by square brackets.",
#     "loop" : "Helps in iterating individual value of a tuple, list, dictionary, etc,.",
# }

# for key,value in glossary.items():
#     print(f"\n{key} : {value}")

# rivers = {
#     "krishna" : "maharashtra",
#     "nile" : "egypt",
#     "godavari" : "telangana",
# }

# for key,value in rivers.items():
#     print(f"\nThe {key.title()} runs through {value.title()}.")

# for key in rivers.keys():
#     print(f"\n{key.title()}.")

# for value in rivers.values():
#     print(f"\n{value.title()}.")

# fav_numbers = {
#     "alice" : "0",
#     "bob" :  "7" ,
#     "sam" : "4",
#     "akhil" : "3",
# }

# friends = ["alice","akhil","vicky","randy"]

# for key in fav_numbers.keys():
#     if key in friends:
#         print(f"Thank you {key.title()} for responding.")
#     else:
#         print(f"{key.title()}, please take the poll.")

# Nesting

#A List of Dictionaries
# alien0 = {"color" : "green", "points" : 5}
# alien1 = {'color': 'yellow', 'points': 10}
# alien2 = {'color': 'red', 'points': 15}

# aliens = [alien0,alien1,alien2]

# for alien in aliens:
#     print(alien)

# aliens = []
# for alien_count in range(30):
#     new_alien = {"color" : "green", "points" : 5}
#     aliens.append(new_alien)

# for alien in aliens[0:5]:
#     print(alien)

# print(f"Total number of aliens are {len(aliens)}")

# for alien in aliens[0:3]:
#     if alien["color"] == "green":
#         alien["color"] = "yellow"
#         alien["speed"] = "medium"        
#         alien["points"] = 10

# for alien in aliens[0:5]:
#     print(alien)

# A List in a Dictionary

# pizza = {
#     "crust" : "thin",
#     "toppings" : ["extra cheese","tomato","onion"]
# }

# print(f"You have ordered {pizza['crust'].upper()} crust pizza with the following toppings : ")
# for topping in pizza["toppings"]:
#     print(f"\t {topping.title()}")

# fav_numbers = {
#     "alice" : [0,2,6],
#     "bob" :  [7,1,3],
#     "sam" : [2,4,9],
#     "akhil" : [1,3,8],
# }

# for name,number in fav_numbers.items():
#     print(f"\n{name.title()} favorite numbers are :")
#     print(f"\t{number}")

# A Dictionary in a Dictionary

# users = {
#     "akhilbodi" : {
#         "first_name" : "akhil",
#         "last_name" : "bodi",
#         "location" : "India",
#     },
#     "alicebob" : {
#         "first_name" : "alice",
#         "last_name" : "bob",
#         "location" : "universe",
#     },
# }

# for username,user_info in users.items():
#     print(f"\nUsername : {username}")
#     full_name = f"{user_info['first_name']} {user_info['last_name']}"
#     location = user_info['location']

#     print(f"\tFull name is {full_name.title()}")
#     print(f"\tLocation is {location.title()}")

# Try It Yourself

# person1 = {
#     "first_name" : "akhil",
#     "last_name" : "bodi",
#     "age" : "forever young",
#     "city" : "hyderabad"
# }
# person2 = {
#     "first_name" : "alice",
#     "last_name" : "bob",
#     "age" : "enough to get married",
#     "city" : "hyderabad"
# }
# person3 = {
#     "first_name" : "bob",
#     "last_name" : "alice",
#     "age" : "Unknown",
#     "city" : "hyderabad"
# }

# people = [person1,person2,person3]
# for person in people:
#     print(person)

# dog = {
#     "name" : "bravo",
#     "owner_name" : "kavis",
# }
# cat = {
#     "name" : "bean",
#     "owner_name" : "sam",
# }
# bird = {
#     "name" : "uno",
#     "owner_name" : "sima",
# }
# pets = [dog,cat,bird]
# for pet in pets:
#     print(pet)

# favorite_places = {
#     "akhil" : ["kerala", "shimla", "assam"],
#     "alice" : ["karnatataka", "gujarat", "punjab"],
#     "bob" : ["tamil nadu", "uttar pradesh", "mizoram"]
# }

# for name, places in favorite_places.items():
#     print(f"\nFavorite places of {name.title()} are :")
#     for place in places:
#             print(f"{place.title()}")

# fav_numbers = {
#     "alice" : [0,2,6],
#     "bob" :  [7,1,3],
#     "sam" : [2,4,9],
#     "akhil" : [1,3,8],
# }

# for name, number in fav_numbers.items():
#     print(f"\nFavorite numbers of {name.title()} are :")
#     for num in number:
#             print(f"{num}")

# cities = {
#     "hyderabad" : ["India", "1,08,01,000", "real home of Koh-i-Noor"],
#     "florence" : ["italy", "7,11,000", "birthplace of piano"],
#     "cape town" : ["south africa", "48,90,000","home to the country's oldest garden"],
# }

# for city,info in cities.items():
#     print(f"\n{city.title()}")
#     print(f"{city.title()} is a city in {info[0].title()}, with a population of {info[1]}. The interesting fact about {city} that it is 'The {info[2].title()}.'") 


#                                           --------------------- CHAPTER 7 - User Input and While Loops ---------------------

# How the input() Function Works

#Writing Clear Prompts

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

#Using int() to Accept Numerical Input

# age = int(input("How old are you? "))
# print(age >= 18)

# height = int(input("How tall are you, in inches? "))
# if height >= 48:
#     print("\nYou are tall enough to ride")
# else:
#     print("\nYou'll be able to ride when you are little older.")

#The Modulo Operator

# number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# Try It Yourself

# user_input = input("what kind of rental car would like to have? ")
# print(f"\nLet me see if I can find you a {user_input.title()}.")

# user_input = int(input("Dinner table for how many people? "))
# if user_input > 8:
#     print("\nSorry you'll have to wait for sometime. The tables are full.")
# else:
#     print(f"\nYour table for {user_input} is ready.")

# user_input = int(input("Enter a number : "))
# if user_input % 10 == 0:
#     print("Your number is a multiple of 10.")
# else:
#     print("Your number is not a multiple of 10.")

# Introducing while Loops

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#Letting the User Choose When to Quit
# prompt = "\nTell me something, and I'll repeat it back to you:  "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
# active = True
# while active:
#     message = input(prompt)
#     if message.lower() == 'quit':
#         active = False
#     else:
#         print(message)

#Using break to Exit a Loop

# prompt = "Enter the name of the place you have visited."
# prompt += "Enter 'quit' to end the program. "

# while True:
#     city = input(prompt)
#     if city.lower() == 'quit':
#         break
#     else:
#         print(f"{city.title()} is such a beautiful place.")

#Using continue in a Loop

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     else:
#         print(current_number)

#Avoiding Infinite Loops - if you omit the counter, the loop will run forever

# Try It Yourself

# prompt = "Enter the toppings that you'd like to have. Enter 'quit' to end. "
# while True:
#     topping = input(prompt)
#     if topping.lower() == 'quit':
#         break
#     else:
#         print(f"will add {topping} to the pizza.") 

# prompt = "Please enter your age : "
# age = int(input(prompt))
# if age < 3:
#     print("The ticket is free!")
# elif age > 3 and age < 12:
#     print("The ticket is $10!")
# else:
#     print("The ticket is $15!")

# Using a while Loop with Lists and Dictionaries

#Moving Items from One List to Another

# unconfirmned_users = ["akhil","alice","bob"]
# confirmed_users = []
# while unconfirmned_users:
#     current_user = unconfirmned_users.pop()
#     print(f"Verfying user : {current_user.title()}")
#     confirmed_users.append(current_user)
# print("\nThe following users has been confirmed: ")
# for user in confirmed_users:
#     print(user.title())

#Removing All Instances of Specific Values from a List

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat','dog']
# while 'dog' in pets:
#     pets.remove('dog')
# print(pets)

#Filling a Dictionary with User Input
# responses = {}
# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("\nName the place you want to go someday. ")

#     responses[name] = response 

#     repeat = input("\nWould you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
# for name,response in responses.items():
#     print(f"{name.title()} would like to go to {response.title()}")

# sandwich_orders = ["paneer sandwich","veg cheese sandwich","veg grilled sandwich","vegetable sandwich"]
# finished_sandwich = []
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I made your {current_sandwich.title()}.")
#     finished_sandwich.append(current_sandwich)
# print("\nThe finished sandwiches are: ")
# for sandwich in finished_sandwich:
#     print(sandwich.title())

# sandwich_orders = ["pastrami","paneer sandwich","veg cheese sandwich","pastrami","veg grilled sandwich","vegetable sandwich","pastrami"]
# finished_sandwich = []
# print("Deli has run out of pastrami\n")
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I made your {current_sandwich.title()}.")
#     finished_sandwich.append(current_sandwich)
# print("\nThe finished sandwiches are: ")
# for sandwich in finished_sandwich:
#     print(sandwich.title())

# responses = {}
# poll_active = True

# while poll_active:
#     name = input("\nEnter your name: ")
#     response = input("What is your dream vacation? ")
#     responses[name] = response

#     repeat = input("\nWould you like to take poll for another person? (yes/no) ")
#     if repeat.lower() == "no":
#         poll_active = False

# for name,response in responses.items():
#     print(f"{name.title()} dream vacation is {response.title()}.")


#                                           --------------------- CHAPTER 8 - Functions ---------------------


# Defining a Function

#Passing Information to a Function
# def greet_user(username):
#     """Displays a greeting"""      # docstring  
#     print(f"Hello, {username.title()}.")

# greet_user("akhil bodi")

#Arguments and Parameters

# def display_message(learning):
#     print(f"In this chapter we are learning about {learning.title()}.")

# display_message("functions")

# def favorite_book(book_name):
#     print(f"My favorite book is {book_name.title()}.")

# favorite_book("atomic habits")

# Passing Arguments

#Positional Arguments
# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet("Rhino","butcher")
# describe_pet("Eagle","conqueror")  #Multiple Function Calls

#Order Matters in Positional Arguments


#Keyword Arguments
# def describe_pet(animal_type = "eagle",pet_name = "conqueror"):
#         print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet()

#Default Values
# def describe_pet(pet_name,pet_type="eagle"):
#     print(f"My {pet_type}'s name is {pet_name.title()}.")

# describe_pet("conqueror")

#Equivalent Function Calls
# def describe_pet(pet_name,pet_type="eagle"):
#     print(f"My {pet_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name="conqueror")

#Try It Yourself

# def make_shirt(size,message):
#     print(f"The shirt size is {size.title()} and the message is '{message.title()}'.")

# make_shirt("m","wakanda forever")

# def make_shirt(size="m",message="wakanda forever"):
#     print(f"The shirt size is {size.title()} and the message is '{message.title()}'.")

# make_shirt()
# def make_shirt(message,size="l"):
#     print(f"The shirt size is {size.title()} and the message is '{message.title()}'.")

# make_shirt(message="i love python")
# make_shirt(message="i love python",size="m")
# make_shirt("wakanda forever","m")

# def describe_city(city,country="India"):
#     print(f"{city.title()} is in {country.title()}.")

# describe_city("hyderabad")
# describe_city("banglore")
# describe_city("florence",country="italy")

# Return Values

# def full_name(first_name,last_name):
#     """Return a full name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# author = full_name("akhil","bodi")
# print(author)

#Making an Argument Optional
# def full_name(first_name,last_name,middle_name = ""):
#     """Return a full name"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#         return full_name.title()
#     else:
#         full_name = f"{first_name} {last_name}"
#         return full_name.title()

# author = full_name("akhil","bodi")
# print(author)

#Returning a Dictionary
# def build_person(first_name,last_name):
#     """Return a dictionary of information about a person"""
#     person = {"first" : first_name, "last" : last_name}
#     return person

# name = build_person("akhil", "bodi")
# print(name)

# def build_person(first_name,last_name,age=None):
#     """Return a dictionary of information about a person"""
#     person = {"first" : first_name, "last" : last_name}
#     if age:
#         person["age"] = age
#     return person
# name = build_person("akhil", "bodi",23)
# print(name)

#Using a Function with a while Loop
# while True:
#     print(f"\nPlease enter your name :")
#     print(f"\nEnter 'q' to quit")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("last name: ")
#     if l_name == 'q':
#         break
#     full_name = f"{f_name} {l_name}"
#     print(full_name)   

# Try It Yourself
# def city_country(city,country):
#     return f"{city.title()}, {country.title()}"

# city1 = city_country("hyderabad","india")
# city2 = city_country("banglore","india")
# city3 = city_country("chennai","india")
# print(city1)
# print(city2)
# print(city3)

# def make_album(artist_name,album_title,no_of_songs = None):
#     if no_of_songs:
#         album = {"name":artist_name.title(), "title" : album_title.title(),"number of songs" : no_of_songs}
#         return album
#     else:
#         album = {"name":artist_name.title(), "title" : album_title.title()}
#         return album

# album1 = make_album("coldplay","hymn for the weekend")
# album2 = make_album("ed sheeran","divide",16)
# album3 = make_album("one direction","four")
# print(album1)
# print(album2)
# print(album3)

# def make_album_usr():
#     while True:
#         print("Enter 'q' anytime to quit.")
#         artist_name = input("Enter artist name: ")
#         if artist_name == 'q':
#             break
#         album_title = input("Enter album title: ")
#         if album_title == 'q':
#             break
#         album = {"name" : artist_name.title(), "title" : album_title.title()}
#         print(album)
    
# make_album_usr()

#Passing a List
# def greet_users(names):
#     for name in names:
#         print(f"Hello, {name.title()}!")

# greet_users(["akhil","alice","bob"])

#Modifying a List in a Function
# designs = ["phone case","keychain","mask"]
# printed_models = []

# while designs:
    # current_design = designs.pop()
    # print(f"Printing model : {current_design}")
    # printed_models.append(current_design)

# print("\nThe following designs have been printed: ")
# for model in printed_models:
#     print(model)

# def design_models(designs,printed_models):
#     while designs:
#         current_design = designs.pop()
#         print(f"Printing model : {current_design}")
#         printed_models.append(current_design)

# def completed_models(printed_models):
#     print("\nThe completed models are: ")
#     for model in printed_models:
#         print(model)

# designs = ["phone case","keychain","mask"]
# printed_models = []

# design_models(designs,printed_models)
# completed_models(printed_models)
# print(designs)

#Preventing a Function from Modifying a List
# def design_models(designs,printed_models):
#     while designs:
#         current_design = designs.pop()
#         print(f"Printing model : {current_design}")
#         printed_models.append(current_design)

# def completed_models(printed_models):
#     print("\nThe completed models are: ")
#     for model in printed_models:
#         print(model)

# designs = ["phone case","keychain","mask"]
# printed_models = []

# design_models(designs[:],printed_models)    # [:] works as a copy
# completed_models(printed_models)
# print(designs)

# Try It Yourself
# def show_messages(messages):
#     for message in messages:
#         print(message.title())

# text_messages = ["hello","how are you?","had lunch?","bye!"]
# show_messages(text_messages)

# def send_messages(messages):
#     while messages:
#         current_message = messages.pop()
#         print(current_message.title())
#         sent_messages.append(current_message)

# text_messages = ["had lunch?","how are you?","hello"]
# sent_messages = []
# send_messages(text_messages)
# print(text_messages)
# print(sent_messages)

# def send_messages(messages):
#     while messages:
#         current_message = messages.pop()
#         print(current_message.title())
#         sent_messages.append(current_message)

# text_messages = ["had lunch?","how are you?","hello"]
# sent_messages = []
# send_messages(text_messages[:])
# print(text_messages)
# print(sent_messages)


# Passing an Arbitrary Number of Arguments
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('cheese',"onions","green pepper")

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print("The toppings requested by customer are: ")
#     for topping in toppings:
#         print(f"- {topping.title()}")

# make_pizza('cheese',"onions","green pepper")

#Mixing Positional and Arbitrary Arguments
# def make_pizza(size,*toppings):
#     print(f"The {size}-inch size will have the following toppings: ")
#     for topping in toppings:
#         print(f"-{topping.title()}")

# make_pizza(12,'cheese',"onions","green pepper")

#Using Arbitrary Keyword Arguments
# def build_profile(first_name,last_name,**user_info):
#     """Building a dictionary about a user based on the provided information"""
#     user_info["first_name"] = first_name
#     user_info["last_name"] = last_name
#     return user_info

# user = build_profile("akhil","bodi",location="india",field="data")
# print(user)

# Try It Yourself

# def toppings(*toppings):
#     print("\nThe following items are the toppings on the sandwich.")
#     for topping in toppings:
#         print(f"-{topping.title()}")

# toppings('cheese')
# toppings('cheese',"onions")
# toppings('cheese',"onions","green pepper")

# def my_profile(**user_info):
#     return user_info

# profile = my_profile(first_name = "akhil",last_name = "bodi", location = "india",occupation = "forever student")
# print(profile)


# def make_car(manufacturer,model_name,**car_info):
#     car_info["manufacturer"] = manufacturer
#     car_info["model_name"] = model_name
#     return car_info

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

# Storing Your Functions in Modules

#                                           --------------------- CHAPTER 9 - Classes ---------------------

# Creating and Using a Class

#Creating the Dog Class

# class Dog:
#     """Attempt to model a dog."""

#     def __init__(self,name,age):
#         """Initialize name and age attributes"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name.title()} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name.title()} has rolled over.")


#Making an Instance from a Class

# my_dog = Dog("bruh",3)
# print(f"My dog name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# my_dog.roll_over()

#Creating Multiple Instances
# my_dog = Dog("bruh",3)
# your_dog = Dog("mar",2)

# print(f"My dog name is {my_dog.name.title()}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog name is {your_dog.name.title()}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()

# Try It Yourself

# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"\n{self.restaurant_name.title()} is located in Hyderabad.")
#         print(f"{self.restaurant_name.title()} has years of excellence in {self.cuisine_type.title()} cuisine.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name.title()} is now open.")

# restaurant1 = Restaurant("khaana","northern indian")

# print(f"The restaurant name is {restaurant.restaurant_name.title()}.")
# print(f"The restaurant is famous for {restaurant.cuisine_type.title()} cuisine.")


# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant2 = Restaurant("vindu","southern indian")
# restaurant3 = Restaurant("chinx","east asian")

# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# class User:
#     def __init__(self,first_name,last_name,user_name,age,location):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.age = age
#         self.location = location

#     def describe_user(self):
#         print(f"\n{self.first_name.title()} {self.last_name.title()} is our new user.")
#         print(f"The username is {self.user_name.lower()}.")
#         print(f"{self.age} years old and lives in {self.location.title()}.")

#     def greet_user(self):
#         print(f"\nHello, {self.first_name.title()} {self.last_name.title()}. Good to see you!")

# user1 = User("akhil","bodi","akhilbodi",23,"hyderabad")
# user2 = User("alice","bob","alice123",10,"rom")
# user3 = User("bob","alice","bob321",10,"rom")

# user1.describe_user()
# user1.greet_user()
# user2.describe_user()
# user2.greet_user()
# user3.describe_user()
# user3.greet_user()

# Working with Classes and Instances

# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
# my_car = Car("rolls royce","phantom",2019)
# print(my_car.get_descriptive_name())

#Setting a Default Value for an Attribute
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
    
# my_car = Car("rolls royce","phantom",2019)
# print(my_car.get_descriptive_name())
# my_car.read_odometer()

#Modifying Attribute Value Directly
# my_car.odometer_reading = 12
# my_car.read_odometer()

#Modifying an Attribute’s Value Through a Method
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot rollback odometer!")
    
# my_car = Car("rolls royce","phantom",2019)
# my_car.update_odometer(12)
# my_car.read_odometer()
# my_car.update_odometer(1)

#Incrementing an Attribute’s Value Through a Method

# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot rollback odometer!")
    
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles


# my_car = Car("rolls royce","phantom",2019)
# my_car.update_odometer(15120)
# my_car.read_odometer()
# my_car.increment_odometer(120)
# my_car.read_odometer()

#Try It Yourself

# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.served = 0

#     def describe_restaurant(self):
#         print(f"\n{self.restaurant_name.title()} is located in Hyderabad.")
#         print(f"{self.restaurant_name.title()} has years of excellence in {self.cuisine_type.title()} cuisine.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name.title()} is now open.")
    
#     def customers_served(self):
#         print(f"{self.restaurant_name.title()} has served {self.served} customers.")

#     def set_number_served(self,served_number):
#         self.served = served_number

#     def increment_number_served(self,increment_number):
#         self.served += increment_number

# restaurant1 = Restaurant("khaana","northern indian")
# restaurant1.set_number_served(3234)
# restaurant1.customers_served()
# restaurant1.increment_number_served(1212)
# restaurant1.customers_served()

# class User:
#     def __init__(self,first_name,last_name,user_name,age,location):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.age = age
#         self.location = location
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"\n{self.first_name.title()} {self.last_name.title()} is our new user.")
#         print(f"The username is {self.user_name.lower()}.")
#         print(f"{self.age} years old and lives in {self.location.title()}.")

#     def greet_user(self):
#         print(f"\nHello, {self.first_name.title()} {self.last_name.title()}. Good to see you!")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0
    

# user1 = User("akhil","bodi","akhilbodi",23,"hyderabad")
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(f"Number of login attempts: {user1.login_attempts}")

# user1.reset_login_attempts()
# print(f"\nlogin attempts have been reset to {user1.login_attempts}.")


# Inheritance

#The __init__() Method for a Child Class

# class Car:                                             # The parent class from above.
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot rollback odometer!")
    
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles


# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)

# my_electric_car = ElectricCar('tesla', 'model x', 2019)
# print(my_electric_car.get_descriptive_name())

#Defining Attributes and Methods for the Child Class

# class Car:                                             # The parent class from above.
#     def __init__(self,make,model,year,battery):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#         self.battery = 75

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot rollback odometer!")
    
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

#     def describe_battery(self):
#         print(f"This car has a {self.battery} kwh battery.")


# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)

# my_electric_car = ElectricCar('tesla', 'model x', 2019)
# print(my_electric_car.describe_battery())

# Instances as Attributes

# class Battery:
#     def __init__(self,battery_size = 75):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f"This car has {self.battery_size} kwh battery.")

#     def get_range(self):
#         if self.battery_size == 75:
#             range = 215
#         elif self.battery_size == 100:
#             range = 315

#         print(f"This car has a range of {range} miles on full charge.")


# class Car:                                             # The parent class from above.
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#         self.battery = 75

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot rollback odometer!")
    
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

#     def describe_battery(self):
#         print(f"This car has a {self.battery} kwh battery.")

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

# my_electric_car = ElectricCar('tesla', 'model x', 2019)
# print(my_electric_car.battery.describe_battery())
# print(my_electric_car.battery.get_range())


# Try It Yourself

# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.served = 0

#     def describe_restaurant(self):
#         print(f"\n{self.restaurant_name.title()} is located in Hyderabad.")
#         print(f"{self.restaurant_name.title()} has years of excellence in {self.cuisine_type.title()} cuisine.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name.title()} is now open.")
    
#     def customers_served(self):
#         print(f"{self.restaurant_name.title()} has served {self.served} customers.")

#     def set_number_served(self,served_number):
#         self.served = served_number

#     def increment_number_served(self,increment_number):
#         self.served += increment_number

# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)

#         self.flavours = ["vanilla","chocolate","strawberry","pineapple","mango"]

#     def flavours_available(self):
#         print(f"The available flavours are {self.flavours}.")

# my_icecream = IceCreamStand("robbins","ice cream")    
# print(my_icecream.flavours_available())

# class User:
#     def __init__(self,first_name,last_name,user_name,age,location):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.age = age
#         self.location = location
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"\n{self.first_name.title()} {self.last_name.title()} is our new user.")
#         print(f"The username is {self.user_name.lower()}.")
#         print(f"{self.age} years old and lives in {self.location.title()}.")

#     def greet_user(self):
#         print(f"\nHello, {self.first_name.title()} {self.last_name.title()}. Good to see you!")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0
    
# class Admin(User):
#     def __init__(self, first_name, last_name, user_name, age, location):
#         super().__init__(first_name, last_name, user_name, age, location)

#         self.privilages= []

#     def show_privilages(self):
#         print(f"The admin privilages are: ")
#         for privilage in self.privilages:
#             print(privilage)

# user_admin = Admin("akhil","bodi","akhilbodi",23,"earth")
# user_admin.privilages = ["can add post", "can delete post", "can add user", "can ban user"]
# print(user_admin.show_privilages())


# class User:
#     def __init__(self,first_name,last_name,user_name,age,location):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.age = age
#         self.location = location
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"\n{self.first_name.title()} {self.last_name.title()} is our new user.")
#         print(f"The username is {self.user_name.lower()}.")
#         print(f"{self.age} years old and lives in {self.location.title()}.")

#     def greet_user(self):
#         print(f"\nHello, {self.first_name.title()} {self.last_name.title()}. Good to see you!")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0
    
# class Admin(User):
#     def __init__(self, first_name, last_name, user_name, age, location):
#         super().__init__(first_name, last_name, user_name, age, location)

        # self.privilages = Privilages()



# new_user = Admin("akhil","bodi","akhilbodi",23,"earth")
# print(new_user.show_privilages())

# class Privilages():
#     def __init__(self,privilages=[]):
#         self.privilages = privilages

#     def show_privilages(self):
#         print(f"The privilages of admin are :")
#         for privilage in self.privilages:
#             print(privilage)

# new_user = Admin("akhil","bodi","akhilbodi",23,"earth")
# new_user_privilages = ["can add post", "can delete post", "can add user", "can ban user"]
# new_user.privilages.privilages = new_user_privilages
# new_user.privilages.show_privilages()

# class Battery:
#     def __init__(self,battery_size = 75):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f"This car has {self.battery_size} kwh battery.")

#     def get_range(self):
#         if self.battery_size == 75:
#             range = 215
#         elif self.battery_size == 100:
#             range = 315

#         print(f"This car has a range of {range} miles on full charge.")

#     def upgrade_battery(self):
#         if self.battery_size != 100:
#             self.battery_size = 100
#             print("Battery upgraded to 100")
#         else:
#             print("Already Upgraded.")

# class Car:                                             # The parent class from above.
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#         self.battery = 75

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot rollback odometer!")
    
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

#     def describe_battery(self):
#         print(f"This car has a {self.battery} kwh battery.")

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

# my_electric_car = ElectricCar('tesla', 'model x', 2019)
# print(my_electric_car.battery.upgrade_battery())
# print(my_electric_car.battery.get_range())

# Try It Yourself

# from random import randint

# class Die:
#     def __init__(self,sides=6):
#         self.sides = sides

#     def roll_die(self):
#         return randint(1,self.sides)

# six_dice = Die()
# results = []
# for num in range(10):
#     result = six_dice.roll_die()
#     results.append(result)

# print(results)

# ten_dice = Die(sides=10)
# results = []
# for num in range(10):
#     result = ten_dice.roll_die()
#     results.append(result)

# print(results)

# twenty_dice = Die(sides=20)
# results = []
# for num in range(10):
#     result = twenty_dice.roll_die()
#     results.append(result)

# print(results)

# from random import choice
# lottery = [1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E']
# winner = []
# while len(winner) < 4:
#     i = choice(lottery)
#     if i not in winner:
#         winner.append(i)

# print(winner)

# from random import choice
# lottery_items = [1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E']
# winning_ticket = [choice(lottery_items) for i in range(4)]
# my_ticket = []
# count = 0
# while my_ticket != winning_ticket:
#     my_ticket = [choice(lottery_items) for i in range(4)]
#     count += 1

# print(count)


#                                           --------------------- CHAPTER 10 - Files and Exceptions ---------------------


# Reading from a File

#Reading an Entire File

# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()
# print(contents)

#File Paths
# file_path = "path"
# with open(file_path) as file:
#     data = file.read()
# print(data)

#Reading Line by Line

# file = "/home/akhilbodi/Documents/Data Science/Journey/Practice/pi_digits.txt"
# with open(file) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# file = "/home/akhilbodi/Documents/Data Science/Journey/Practice/pi_digits.txt"
# with open(file) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

#Working with a File’s Contents
# file = "/home/akhilbodi/Documents/Data Science/Journey/Practice/pi_digits.txt"
# with open(file) as file_object:
#     lines = file_object.readlines()

# pi_string = ""
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

#Large Files: One Million Digits
# file = "pi_million_digits.txt"
# with open(file) as file_object:
#     lines = file_object.readlines()

# pi_string = ""
# for line in lines:
#     pi_string += line.strip()

# print(f"{pi_string[0:100]}")
# print(len(pi_string))

#Is Your Birthday Contained in Pi?
# file = "pi_million_digits.txt"
# with open(file) as file_object:
#     lines = file_object.readlines()

# pi_string = ""
# for line in lines:
#     pi_string += line.strip()

# birthday = input("Enter your birthday in this form - ddmmyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi.")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")


# Writing to a File

#Writing to an Empty File
# file = "learning_python.txt"

# with open(file, 'w') as file_object:
#     file_object.write("I love python")

# with open(file, 'r') as file_obj:
#     content = file_obj.read()
# print(content)

#Writing Multiple Lines

# file = "learning_python.txt"

# with open(file, 'w') as file_object:
#     file_object.write("I love python.\n")
#     file_object.write("I love data science.")


# with open(file, 'r') as file_obj:
#     content = file_obj.read()
# print(content)

#Appending to a File
# file = "learning_python.txt"

# with open(file, 'a') as file_object:
#     file_object.write("\nI love python as it enables me to play with data.\n")
#     file_object.write("I love data science for extracting meaning from the data.\n")


#Try It Yourself

# file = "guest.txt"
# guest_name = input("Please enter your name: ")
# with open(file,"w") as file_object:
#     file_object.write(guest_name.title())

# file = "guest_book.txt"
# while True:
#     guest_name = input("Enter 'q' to quit the program.\nPlease enter your name: ")
#     if guest_name == "q":
#         break
#     with open(file,"a") as file_object:
#         file_object.write(f"{guest_name.title()}\n")
#     print(f"Welcome {guest_name.title()}. Glad to have you here.\n")

# file = "guest_reason.txt"
# while True:
#     name = input("Enter 'q' to quit.\nEnter you name: ")
#     if name == "q":
#         break
#     reason = input("Enter 'q' to quit.\nWhy do you like programming?: ")
#     if reason == "q":
#         break
#     with open(file,'a') as file_object:
#         file_object.write(f"{name.title()} likes programming because - '{reason}.'\n")

# with open(file,'r') as file_object:
#     contents = file_object.readlines()

# for line in contents:
#     print(line)

# Exceptions

#Using try-except Blocks

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Can't divide by zero.")

#Using Exceptions to Prevent Crashes

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break

#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Can't divide by zero.")
#     else:
#         print(answer)

#Handling the FileNotFoundError Exception

# file_name = "me.txt"
# try:
#     with open(file_name,encoding="utf=8") as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry the file '{file_name}' does not exist.")

#Analyzing Text

# file = "guest_reason.txt"
# try:
#     with open(file,"r") as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry the file '{file}' does not exist.")
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {file} has {num_words} words.")

# def count_words(file):
#     """Counts the number of words in the file"""
#     try:
#         with open(file,"r") as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {file} has {num_words} words.")


# # filename = "guest_reason.txt"
# # count_words(filename)

# files = ["guest_reason.txt", "guest_book.txt","guest.txt","pi_million_digits.txt","num.txt"]
# for file in files:
#     count_words(file)

#Try It Yourself

# try:
#     input1 = input("Enter a number: ")
#     input1 = int(input1)
#     input2 = input("Enter a number: ")
#     input2 = int(input2)

# except ValueError:
#     print("Please enter a valid number.")

# else:
#     print(f"Sum of the numbers {input1} and {input2} is {input1+input2}")

# print("Enter 'q' anytime to quit")
# while True:
#     try:
#         input1 = input("Enter a number: ")
#         if input1 == "q":
#             break
#         input1 = int(input1)

#         input2 = input("Enter a number: ")
#         if input1 == "q":
#             break
#         input2 = int(input2)

#     except ValueError:
#         print("Please enter a valid number.")

#     else:
#         print(f"Sum of the numbers {input1} and {input2} is {input1+input2}")


# Storing Data

#Using json.dump() and json.load()

import json

# numbers = [i for i in range(10)]
# file_name = "numbers.txt"
# with open(file_name,"w") as f:
#     json.dump(numbers,f)

# with open("numbers.txt","r") as f:
#     num = json.load(f)

# print(num)

#Saving and Reading User-Generated Data

# username = input("Please enter your name : ")

# file_name = "username.json"
# with open(file_name,"w") as f:
#     json.dump(username.title(),f)
#     print(f"Will remember when you comeback, {username.title()}!")

# with open("username.json") as f:
#     username = json.load(f)
#     print(f"Welcome back {username}!")

# filename = "username.json"

# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("Please enter your name : ")
#     with open(filename,"w") as f:
#         json.dump(username,f)
#         print(f"Will remember when you comeback, {username.title()}!")       
# else:
#     print(f"Welcome back {username}!")


# def greet_user():
#     """Greet the user by the entered name."""
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("Please enter your name : ")
#         with open(filename,"w") as f:
#             json.dump(username,f)
#             print(f"Will remember when you comeback, {username.title()}!")       
#     else:
#         print(f"Welcome back {username.title()}!")

# greet_user()