
# step 2
# Oakland, Atlanta, New York City, 
# Seattle, Memphis, Miami, Boston, 
# Los Angeles, Denver, and New Orleans
US_cities = ["Oakland", "Atlanta", "New York City",
"Seattle", "Memphis", "Miami", "Boston", "Los Angeles",
"Denver", "New Orleans"]

print(US_cities)

def print_city(list) :
    for x in list :
        print(x)
    return 

print(print_city(US_cities))

def reorganize_list(list) :
    counter = 0
    while counter < len(list) :
        city1 = list[counter]
        city2 = list[counter + 1]
        
        if len(city1) >= len(city2) :
            counter += 1
            continue
        elif counter + 1 == len(list) - 1 :
            break
        else :
            list.remove(city1)
            list.append(city1)
            counter += 1
        
    return list

print(reorganize_list(US_cities))

def sort_list(list) :
    return sorted(list)

print(sort_list(US_cities))

# step 3

print(US_cities[0], US_cities[3], US_cities[-3])

# step 4

four_cities = US_cities[4 : 8]

print(four_cities)

# step 5

US_cities[0] = "San Francisco"
US_cities[2] = "Brooklyn"
US_cities[-3] = "Hollywood"
US_cities[5] = "Tampa"

print(US_cities)

# step 6

US_cities.append("Oakland")
US_cities.extend(["New York City", "Los Angeles"])
US_cities.insert(0, "Miami")

print(US_cities)

# step 6
del US_cities[6]
US_cities.pop(7)
US_cities.remove("Denver")

print(US_cities)

