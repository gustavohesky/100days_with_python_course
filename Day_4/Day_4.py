## Random Module

import random

# random_integer = random.randint(1,10)
# print(random_integer)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

# heads_or_tails = random.randint(0,1)
# if heads_or_tails == 1:
#     print("Heads")
# else:
    # print("Tails")

##Lists

states_of_america = ["Delaware","Pennysylvania"]
print(states_of_america[0])

# Adding a state to the list
states_of_america.append("Hawai")
print(states_of_america)

#Exercise - Who pays the bill?

friends = ['Leonardo','Clovis','Felipe','Edgar','Vagner']
print(random.choice(friends))

random_index = random.randint(0,4)
print(friends[random_index])


#Nested list
# dirty_dozen = ["Strawberries","Spinach","Kale", "Collard","Grapes","Peaches","Pears","Nectarines","Apples","Blackberries","Cherries","Blueberries"]

fruits = ["Strawberries","Grapes","Peaches","Pears","Nectarines","Apples","Blackberries","Cherries","Blueberries"]
vegetables = ["Spinach","Kale", "Collard"]

dirty_dozen = [fruits,vegetables]
print(dirty_dozen)


