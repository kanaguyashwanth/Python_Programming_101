# Nesting lists and dictionaries

'''
SYNTAX:

dictionary = {
Key: [List],
Key2: {dict},
}
'''

# Simple dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}


# Nesting a List in a List
alphabets = ["A", "B", ["C", "D"]]


# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}


# Nesting a Dictionary inside a List
travel_log = [
   {"country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
   {"country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
]


'''
[{
    Key: [List],
    Key2: {Dict},
},
{
    Key: Value,
    Key2: Value,
}]
'''

# NOTE
'''
Dictionaries are accessed by Key
whereas Lists are accessed by Index
'''