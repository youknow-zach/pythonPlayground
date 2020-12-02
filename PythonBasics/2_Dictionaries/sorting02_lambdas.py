states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

# prints the state names sorted by the length of the first city name in city list
print(sorted(states, key=lambda cities1: len(states[cities1][0])))

# function for next sort: return number of cities in list that begin with 'S'
def s_city_count(city_list):
    ct = 0
    for city in city_list:
        if city[0].upper() == "S":
            ct += 1
    return ct

# sort in order of states with most cities that start with 'S'
print(sorted(states, key=lambda cities2: s_city_count(states[cities2]), reverse=True))

# this function will replace the lambda
# it takes the state name and returns the value list of cities from 'states'
def s_city_count_for_state(state):
    cities_list = states[state]
    return s_city_count(cities_list)

print(sorted(states, key=s_city_count_for_state))
