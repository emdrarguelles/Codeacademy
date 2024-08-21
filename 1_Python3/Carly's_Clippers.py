hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# create a variable to sum up all prices
total_price = 0

# create a loop to add all price
for price in prices:
  total_price = total_price + price

# create a variable to get average price
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

# use list comprehension to reduce all prices by 5 dollars
new_prices = [price - 5 for price in prices]
print(new_prices)

# create a variable for total revenue
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue = total_revenue + (prices[i] * last_week[i])
print("Total Revenue:", total_revenue)

# get daily average
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# use list comprehension to advertise cuts under 30
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)