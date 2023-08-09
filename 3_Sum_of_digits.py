# CODING EXERCISE: Sum of Digits
'''
Enter a two digit number: 26 ---> OUTPUT: 8
'''

num = input ("Enter a two digit number: ")
n_2_str = str (num)
first_digit = int(n_2_str[1])
last_digit = int(n_2_str[0])
print ("Sum of digits: " + str(first_digit + last_digit))
