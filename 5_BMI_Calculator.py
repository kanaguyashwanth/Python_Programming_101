# CODING CHALLENGE: BMI CALCULATOR

height = input ('Enter your height(m): ')
weight = input ('Enter your weight(kg): ')

'''
LOGIC: BMI = Weight (kg) / (Height (m^2) )^2

OUTPUT must be a Whole Number
'''

w = float (weight)
h = float (height)

bmi = w / (h*h)
 
print('Your BMI is : ' + str(int(bmi)))