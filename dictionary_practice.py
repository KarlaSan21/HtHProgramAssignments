
# step 2
prices = {
    "chicken" : 1.59,
    "beef" : 1.99,
    "cheese" : 1.00,
    "milk" : 2.50
}

def total_price(x, y) :
    sum = prices[x] + prices[y]
    return "The total price of " + x + " and " + y + " is ", sum

print(total_price("beef", "cheese"))

def price_diff(x, y) :
    diff = prices[x] - prices[y]
    return "The difference in price of " + x + " and " + y + " is ", diff

print(price_diff("beef", "cheese"))


# step 3
friends_age = {
    "Pedro" : 19,
    "Mariana" : 19,
    "Rachel" : 20,
    "Kierra" : 19
}

def oldest(dict) :
    oldest_age = 0
    name = ''

    for key in dict.keys() :
        if dict[key] > oldest_age :
            oldest_age = dict[key]
            name = key
    
    return (name, oldest_age)

print(oldest(friends_age))


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


def shoe_restock(shoe, num) :
    shoes[shoe] *= num
    return shoes

print(shoe_restock("Air Max", 3))

def shoe_clearence(shoe, num) :
    shoes[shoe] //= num
    return shoes

print(shoe_clearence("SB Dunk", 4))



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

