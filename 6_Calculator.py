# Exercise - Combining dictionaries and functions (CALCULATOR)

'''
What is the first number?: 7
+
-
*
/
Pick an operation: +
What's the next number?: 3
7.0 + 3.0 = 10.0
Type 'y' to continue calculating with 10.0, or type 'n' to start a new calculation: y
Pick an operation: *
What's the next number?: 2
10.0 * 2.0 = 20.0
Type 'y' to continue calculating with 20.0, or type 'n' to start a new calculation: n

What's the first number?: 3
+
-
*
/
Pick an operation: *
What's the next number?: 5
3.0 * 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: 

'''


# CODE:

'''
def operation(num1, oper, num2):
    
    if oper == '+':
        num_res = num1 + num2
    elif oper == '-':
        num_res = num1 - num2
    elif oper == '*':
        num_res = num1 * num2
    else:
        num_res = num1 / num2
'''

# ADD
def add (num1, num2):
    return num1 + num2
# SUBTRACT
def subtract (num1, num2):
    return num1 - num2
# MULTIPLY
def multiply (num1, num2):
    return num1 * num2
# DIVIDE
def divide (num1, num2):
    return num1 / num2


num1 = float (input ("What is the first number?: "))

# Printing list of Operators
operators = ['+', '-', '*', '/']
for n in range (len(operators)):
    print (operators[n])

oper = input ('Pick an operation: ')
num2 = float (input ("What's the next number?: "))

# Creating a Dictionary for Operations (keys: values)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

function = operations[oper]
output = function(num1, num2)

print (f'{num1} {oper} {num2} = {output}')

cont_calc = input ("Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")

while cont_calc == 'y':
    
    num1 = output
    
    # Printing list of Operators
    operators = ['+', '-', '*', '/']
    for n in range (len(operators)):
        print (operators[n])

    oper = input ('Pick an operation: ')
    num2 = float (input ("What's the next number?: "))
    
    function = operations[oper]
    output = function(num1, num2)
    
    print (f'{num1} {oper} {num2} = {output}')
    cont_calc = input ("Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")


