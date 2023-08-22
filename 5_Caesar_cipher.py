# Exercise - Caesar Cipher

'''
NOTE:
a - 0
b - 1
c - 2
.
.
.

'''

from art import logo
print (logo)

from alpha import alphabet

# Variables - direction, text, shift
direction = input ("Type 'encode' to encrypt / 'decode' to decrypt: ")
text = input ("Type your message: ").lower()
shift = int (input ("Type your shift number: "))





# Creating a function to encrypt with parameters - text, shift
def encrypt(txt, shft):
    
    from alpha import alphabet
    # Logic for shifting the alphabets:
        # Get the position of each letter in 'text' and match it with alphabet list with position
        # Now, increment with 'shift' and swap it from the alphabet list.
    position_list = [] # List of position numbers that matches with the text
    
    for i in range(len(txt)):
        for j in range(len(alphabet)):
            if txt[i] == alphabet[j]:
                position_list.append(j)
    # print(position_list) 			# Remeber, this is inside the function and cannot be printed outside the scope.


    # Shifting the posititon values by incrementing with shft value and reset the value to 0 after 25
    for i in range (len(position_list)):
        position_list[i] += shft
    # print(position_list)
    
    
    # Printing the shifted text using the position_list
    shft_str = ''
    for i in range (len(position_list)):
        shft_str += alphabet[position_list[i]%26]
    print(f'The encoded text is {shft_str}')





def decrypt(txt, shft):
    from alpha import alphabet
    # LOGIC
    # Get the position_list
    # Decrement the shift value from the position_list
    # Print the string
    
    # Getting Position_List
    position_list = [] # List of position numbers that matches with the text
    for i in range(len(txt)):
        for j in range(len(alphabet)):
            if txt[i] == alphabet[j]:
                position_list.append(j)
    # print(position_list) 			# Remeber, this is inside the function and cannot be printed outside the scope.
    
    # Shifting the posititon values by decrementing with shft value and reset the value to 0 after 25
    for i in range (len(position_list)):
        position_list[i] -= shft

    # Printing the shifted text using the position_list
    shft_str = ''
    for i in range (len(position_list)):
        shft_str += alphabet[position_list[i]%26]
    print(f'The decoded text is {shft_str}')


if direction == 'encode':
    encrypt(txt = text, shft = shift, )
elif direction == 'decode':
    decrypt(txt = text, shft = shift)