# Exercise - Test 3/3

'''
Question 1:
Which line of code will change the starting_dictionary to the final_dictionary?
'''

starting_dictionary = {
    "a": 9,
    "b": 8,
}

'''
final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
'''
'''
OPTIONS:
a. final_dictionary = starting_dictionary.append({"c": 7})
b. final_dictionary = starting_dictionary += {"c": 7}
c. final_ductionary = starting_dictionary["c"]: 7
d. starting_dictionary["c"] = 7
   final_dictionary = starting_dictionary
'''

# ANSWER:
starting_dictionary["c"] = 7
final_dictionary = starting_dictionary

print (final_dictionary)










'''
Question 2:
Which line of code will produce an error?
'''


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

'''
OPTIONS:
a. dict["c"] = [1, 2, 3]
b. for key in dict:
       dict[key] += 1
c. dict[1] = 4
d. print(dict[1])
'''

# ANSWER
# print(dict[1])







'''
Question 3:
Which line of code will print "Steak"?
'''

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

'''
OPTIONS:
a. print(order["main"][2]) 				#OUTPUT: ['Steak']
b. print(order["dessert - 1"][2][0])	#OUTPUT: Error
c. print(order[main][2][0])				#OUTPUT: Error
d. print(order["main"][2][0])			#OUTPUT: Steak
e. print(order["main"][1][0])			#OUTPUT: Burger
'''

# ANSWER
print (order["main"][2][0])
