# attributes ---> has
# methods ---> does

'''
[has]
seats = 5


[does]
def enter_race_mode():
    seats = 2
'''

class Car:
    def enter_race_mode():
        self.seats = 2

# NOTE: In order to call the method, we need to get hold of the Object and use dot notation to enter into race mode.


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "yashwanth")
user_2 = User("002", "yash")

user_1.follow(user_2)
print(user_1.username)
print(user_2.id)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
