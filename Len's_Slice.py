# Your code below:
# Create a list for pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# pizza slice costs 
prices = [2, 6, 1, 3, 2, 7, 2]

# count all $2 slices and print how many
num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)

# find length of toppings list
num_pizzas = len(toppings)

# print how many pizzas we sell
print("We sell", num_pizzas, "different kinds of pizza!")

# Create a 2D list with price and toppings
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# adding a new pizza topping "peppers"
pizza_and_prices.append([2.5, "peppers"])

# sort 2D list in ascending order
pizza_and_prices.sort() 

# store first element of 2D list
cheapest_pizza = pizza_and_prices[0]
# test print("Cheapest", cheapest_pizza)

# store most expensive pizza
priciest_pizza = pizza_and_prices[-1]
# test print("Priciest", priciest_pizza)

# removing anchovies
pizza_and_prices.pop()

# Print pizza_and_prices
print(pizza_and_prices)

# 3 lowesr pizza costs
three_cheapest = pizza_and_prices[0:3]

# print for the mice
print(three_cheapest)




