# CODING EXERCISE - Love Calculator

'''
Welcome to the Love Calculator!
What is your name?  Arianna Rebolini
What is their name? Channing Tatum

T - 2 L - 1
R - 2 O - 1
U - 1 V - 0
E - 1 E - 1

---------------------
    6     3    %
---------------------

IMPORTANT FUNCTIONS:
- lower() - 'Yashwanth'.lower() = 'yashwanth'
- count() - 'Yashwanth'.count('y') = 0 (CASE-SENSITIVE)

INPUT:
name1 = "Angela Yu"
name2 = "Jack Bauer"

OUTPUT:
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 time
V occurs 0 time
E occurs 2 times
Total = 3

Your score is 53, you are alright together.



CONDITION:
score < 10 and score >90
    "Your score is x, you go together like coke and mentos."
score > 40 and score < 50
    "Your score is y, you are alright together"
else
    "Your score is z."
'''


name1 = input ("Enter your name: ").lower()
name2 = input ("Enter their name: ").lower()

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')

e = name1.count('e') + name2.count('e')

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')

print ('\n')
print (f'T occurs {t} times')
print (f'R occurs {r} times')
print (f'U occurs {u} times')
print (f'E occurs {e} times')
total1 = t + r + u + e
print (f'Total: {total1}')
print ('\n')

print (f'L occurs {l} times')
print (f'O occurs {o} times')
print (f'V occurs {v} times')
print (f'E occurs {e} times')
total2 = l + o + v + e
print (f'Total: {total2}')
print ('\n')

score = int (str(total1) + str(total2))

if (score<10 and score>90):
    print (f"Your score {score}, you go together like coke and mentos.")
if (score>40 and score<50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")