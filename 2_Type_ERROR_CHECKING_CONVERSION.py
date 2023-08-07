# TYPE ERRORS, TYPE CHECKING AND TYPE CONVERSION

'''
What are functions?
-They perform certain tasks like machines on factories.
-Suppose there is a potato maker, we can only feed potatoes and not rocks.
'''

# TYPE ERROR
# print (len(34466)) - Gives a Type Error, since len function won't accept Integers!

# TYPE CHECK
num_char = len (input("What is your name? "))
print("\n")
print("Performing Type Check")
print(type(num_char))
print("\n")
# print ("Your name has " + num_char + " characters.") - Gives a Type Error, since num_char is an Integer and we are trying to print Strings

# TYPE CONVERSION
new_num_char = str(num_char)
print ("Your name has " + new_num_char + " characters.")
print("\n")


# TYPE CONVERSION - EXAMPLE 2
a = float (123)
print(type(a))
print(70 + float("100.5"))  # Here, 100.5 is a string converted to float and then added to an integer
print(str(70) + str(100))   # Here, 70 and 100 are strings and are being CONCATENATED

