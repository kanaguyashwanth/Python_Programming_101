# LISTS

# Variabe --> Single piece of Data
# List    --> Grouped pieces of Data

# Where to use?
'''
Storing all states of the US in a singele variable
'''

# Why is it important?
'''
Order
'''

# How order works?
'''
fruits = ['Apple', 'Cherry', 'Pear']

INDEX ->     0         1        2
            -3		  -2	   -1   (since the Index starts from zero, the last item has the index -1)
'''

# SYNTAX for LISTS:
'''
fruits = [item1, item2]
fruits = ['cherry', 'apple', 'pear']
'''

# EXAMPLE 1: [Storing the States in the  order of it Joining the Union in a List]
states_of_america = ["Delaware", "Pennsylvania",
                     "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina",
                     "New Hampshire", "Virginia",
                     "New York", "North Carolina",
                     "Rhode Island", "Vermont",
                     "Kentucky", "Tennessee",
                     "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri",
                     "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota",
                     "Oregon", "Kansas",
                     "West Virginia", "Nevada",
                     "Nebraska", "Colorado",
                     "North Dakota", "South Dakota",
                     "Montana", "Washington",
                     "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]

print (f'States of America: {states_of_america}')
print ('\n')

print (f'State that joined the Union first: {states_of_america[0]}')
print ('\n')

print (f'State that joined the Union last: {states_of_america[-1]}')
print ('\n')


# EXAMPLE 2: Changing the items in the List
fruits = ['apple', 'pear', 'cherry']
fruits[1] = 'mango'
print (f'Fruits: {fruits}')
print ('\n')


# EXAMPLE 3: Adding an item to the end of the List
'''
Append function - Adds single item to the end of the list
'''
fruits.append('Banana')
print (f'Fruits: {fruits}')
print ('\n')


# EXAMPLE 4: Adding multiple items to the end of the List
'''
Extend function - Adds multiple items to the end of the list
'''
fruits.extend(['Guava', 'Pomegranate', 'Pineapple'])
print (f'Fruits: {fruits}')
print ('\n')

# EXAMPLE 5: Look out for other functions on the List
length_of_list1 = len(states_of_america)
length_of_list2 = len(fruits)
print (f'The length of list_1(states): {length_of_list1}')
print (f'The length of list_2(fruits): {length_of_list2}')
