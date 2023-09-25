# CONSTRUCTORS - Specifies what should happen when an Object is being constructed. (a.k.a INITIALIZING Object)

'''
SYNTAX:
class Car:
    def __init__(self):
    #initialise attributes
'''

'''
EXAMPLE 1: Setting Objects attribute ---> seats

class Car():
    def __init__(self, seats):
        self.seats = seats

# Creating an Object and passing in data
my_car = Car(5)     # Car seats = 5, since the init function contains seat ---> a.k.a   my_car.seats = 5


USE OF INIT FUNCTION:
- Makes it lot quicker when creating lots of objects which will be needing all the same attributes.
'''


class User:

    def __int__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
'''
NOTE:
The name of the attribute and the name of the self.{name} need not be the same.
'''

user_1 = User("001", "yashwanth")
user_2 = User("002", "angela")

print(user_1.username)
print(user_2.id)
print(user_1.followers)
print(user_2.followers)
