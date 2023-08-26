# Exercise - Secret Auction Program

'''
What's your name?: James
What's your bid?: $345
.
.
.


NOTE: This dictionary contains
Name - key
Bid - value
'''    


print ('Welcome to the secret auction program.')


def auction_program (name, bid, choice):
    # Dictionary
    bidder = {}
    bidder["name"] = name
    bidder["bid"] = bid
    details.append(bidder)

    

# List of dictionary
details = []

choice = 'yes'
while (choice == 'yes'):
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    auction_program(name, bid, choice)
    choice = input("Are there any other bidders? Type 'yes' or 'no'.")


if choice == 'no':
    
    big = details[0]['bid']
    for n in range (len(details)-1):   # NOTE: When range is used, make sure you decrement it by 1 because suppose if the length is 2, then the range it takes as 0,2 instead of 0,1.
        if int(details[n]['bid']) > int(details[n+1]['bid']):
            big = details[n]['bid']
            win_name = details[n]['name']
        else:
            big = details[n+1]['bid']
            win_name = details[n+1]['name']
    
    print (f'The winner is {win_name} with a bid of {big}.')