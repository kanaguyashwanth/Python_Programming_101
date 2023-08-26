# Exercise -

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


# Now, we want to add a Dictionary to a List of dictionaries
'''
new_dictionary = {
    "country": 
    "visits":
    "cities":
}
'''

def add_new_country(countries_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = countries_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    # Adding this created dictionary to a List
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)