# Functions with Outputs

'''
def my_function():
    result = 3 * 2
    return result
output = my_function()
print (output)
    
    (or)
    
    
def my_function():
    return 3 * 2
output = my_function()
print (output)
'''

# Example 1: [Output from function]
def my_function():
    result = 3 * 2
    return result
output = my_function()
print (output)


# Example 2: [Converting string to Title Case] [Function with a single return statement]
'''
INPUT:
aNGela
they're bill's friends from the UK

OUTPUT:
Angela
They're Bill's Friends From The UK
'''

# First Name + Last Name = Name
def format_name(f_name, l_name):
    converted_f_name = f_name.title()
    converted_l_name = l_name.title()
    return f"{converted_f_name} {converted_l_name}"

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

formated_string = format_name (f_name, l_name)
print(formated_string)