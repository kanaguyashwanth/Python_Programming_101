# CODING EXERCISE: BMI 2.0

'''
Enter your height(m): 155
Enter your weight(kg): 50
Your BMI is: 22.0 and is Normal Weight

CONDITION:
BMI = weight(kg) / height(m^2) ^ 2
BMI < 18.5       ---> Underweight
BMI > 18.5 < 25 ---> Normal Weight
BMI > 25 < 30    ---> Overweight
BMI > 30 < 35    ---> Obese
BMI > 35         ---> Clinically Obese
'''

height = float (input ('Enter your height(m): '))
weight = float (input ('Enter your weight(kg): '))

BMI = weight / (height*height)
BMI = round (BMI, 2)

if BMI <= 18.5:
    b_type = "Underweight"
    print (f"Your BMI is {BMI} and you are {b_type}")
elif BMI < 25:
    b_type = "Normal Weight"
    print (f"Your BMI is {BMI} and you are {b_type}")
elif BMI < 30:
    b_type = "Overweight"
    print (f"Your BMI is {BMI} and you are {b_type}")
elif BMI < 35:
    b_type = "Obese"
    print (f"Your BMI is {BMI} and you are {b_type}")
else:
    b_type = "Clinically Obese"
    print (f"Your BMI is {BMI} and you are {b_type}")
