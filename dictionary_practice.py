
## dictionary section

# step 2
prices = {
    "chicken" : 1.59,
    "beef" : 1.99,
    "cheese" : 1.00,
    "milk" : 2.50
}

# step 3
friends_age = {
    "Pedro" : 19,
    "Mariana" : 19,
    "Rachel" : 19,
    "Kierra" : 19
}

# step 4
chicken_price = prices["chicken"]
beef_price = prices["beef"]
cheese_price = prices["cheese"]
milk_price = prices["milk"]

print(chicken_price, beef_price, cheese_price, milk_price)

# step 5
pedro_age = friends_age["Pedro"]
mariana_age = friends_age["Mariana"]
rachel_age = friends_age["Rachel"]
kierra_age = friends_age["Kierra"]

print(pedro_age, mariana_age, rachel_age, kierra_age)

# step 6
shoes = {
    "Jordan 13" : 1,
    "Yeezy" : 8,
    "Foamposite" : 10,
    "Air Max" : 5,
    "SB Dunk" : 20
}

# step 7
shoes["SB Dunk"] = 18
print(shoes)

shoes["Yeezy"] = 9
print(shoes)

shoes["Yeezy"] = 16
shoes["SB Dunk"] = 25
shoes["Jordan 13"] = 8
shoes["Foamposite"] = 17
shoes["Air Max"] = 12
print(shoes)

shoes["Yeezy"] = 13
shoes["SB Dunk"] = 22
shoes["Jordan 13"] = 5
shoes["Foamposite"] = 14
shoes["Air Max"] = 9
print(shoes)

# step 8
prices["cereal"] = 3.46
friends_age["Crystal"] = 19
shoes["Nike SB"] = 3

print(prices, friends_age, shoes)

# step 9
del prices["beef"]
del friends_age["Rachel"]
del shoes["Yeezy"]

print(prices, friends_age, shoes)

## lists section




