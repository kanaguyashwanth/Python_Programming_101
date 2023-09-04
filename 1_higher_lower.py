# EXERCISE - higher lower
'''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/

Compare A: Cristiano Ronaldo, a footballer, from Portugal.
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Vin Diesel, a Actor, from United States.
Who has more followers? Type 'A' or 'B': A

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/

You're right! Current score: 1
Compare A: Vin Diesel, a Actor from United States.
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: David Beckam, a Footballer from United States.
Who has more followers? Type 'A' or 'B': B

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/

You're right! Current score: 2
Compare A: David Beckam, a Footballer from United States.
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Kendall Jenner, a Reality TV personality and Model, from United States.
Who has more followers? Type 'A' or 'B': 
'''



# CODE
from art import logo
from art import vs
from game_data import data
import random

current_score = 0

def hi_lo():
    global current_score
    print (logo)
    print (f"Current Score: {current_score}")
    
    rand_int = random.randint(0, 49) # Total 50 ---> len(data)
    data_A = data[rand_int]
    print (f"Compare A: {data_A['name']}, a {data_A['description']}, from {data_A['country']}")
    
    print (vs)
    
    rand_int = random.randint(0, 49) # Total 50 ---> len(data)
    data_B = data[rand_int]
    print (f"Against B: {data_B['name']}, a {data_B['description']}, from {data_B['country']}")

    answer = input("Who has more followers? Type 'A or 'B': ")
    
    if (data_A['follower_count'] > data_B['follower_count']) and (answer == 'A'):
        current_score += 1
        print (f"You're right! Current Score: {current_score}")
        hi_lo()
    elif (data_A['follower_count'] < data_B['follower_count']) and (answer == 'B'):
        current_score += 1
        print (f"You're right! Current Score: {current_score}")
        hi_lo()
    else:
        current_score = 0
        hi_lo()
        

hi_lo()