# Dictionaries - Key-Value Pair

'''
SYNTAX:

programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", "Loop": "The action of doing something over and over again.", "Function": "A piece of code that you can easily call over and over again."
}

print (programming_dictionary["Bug"])

OUTPUT: An error in a program that prevents the program from running as expected.

NOTE: Spell the key properly to get the item from the dictionary (When mispelt, it returns KeyError).

'''

programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from the dictionary
print (programming_dictionary["Bug"])

# Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Empty List vs. Empty Dictionary
empty_list = []
empty_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

# Loop through a dictionary (Prints only the keys of the dictionary)
for thing in programming_dictionary:
    print(thing)
    
# Loop through a dictionary (Print key and the value) - Prints the key(Bug/Function/Loop) and then on next line it prints the value
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wiping an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
