# for loops and the range() function

'''
for item in list_of_items:
    #Do something to each item
'''
# for loop with range
for number in range(1, 11):       # Prints from 1 to 10, not 11.
    print (number)
    




# range with a step
for number in range(1, 11, 3):   # Prints from 1 to 10 with a step 3, step works from the second iteration.
    print (number)				 # 1 (initially)
                                 # 1+3=4
                                 # 4+3=7
                                 # 7+3=10
                                 # Loop ends
                          
                          
                          
# printing the sum of numbers 1-100
total=0
for number1 in range(1, 101):    # 1, 101 -> takes numbers from 1-100
    total += number1

print (total)