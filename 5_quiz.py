# QUIZ:


# Question 1:
'''
Without running the code below,
what do you think will be printed in the console?

a. 10
b. 12.0
c. 0.21
d. 14
'''

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))



# Question 2:
'''
What would you predict to be the result
of running the following code?

a. Syntax Error
b. 15
c. 10
d. (5, 10)
'''
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)



# Question 3:
'''
What will be printed in the console
after running the following code?

a. NameError
b. SyntaxError
c. None
d. "Pass"
e. "Great"
'''
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))