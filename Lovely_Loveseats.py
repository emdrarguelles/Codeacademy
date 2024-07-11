# description 1
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# price 1
lovely_loveseat_price = 254.00

# description 2
stylish_settee_description = "\nStylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# price 2
stylish_settee_price = 180.50


# description 3
luxurious_lamp_description = "\nLuxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# price 3
luxurious_lamp_price = 52.15

# tax
sales_tax = .088

# customer total (running)
customer_one_total = 0

# customer item descriptions
customer_one_itemization = ""

# customer bought lovely_loveseats so added price
customer_one_total = customer_one_total + lovely_loveseat_price

# customer bought lovely_loveseats so added description
customer_one_itemization = customer_one_itemization + lovely_loveseat_description

# customer bought luxurious_lamp so added price
customer_one_total = customer_one_total + luxurious_lamp_price

# customer bought luxurious_lamp so added description
customer_one_itemization = customer_one_itemization + luxurious_lamp_description

# total tax
customer_one_tax = customer_one_total * sales_tax

# total cost after tax
customer_one_total = customer_one_total + customer_one_tax
print("\nCustomer One Items:")
print(customer_one_itemization)
print("\nCustomer One Total:")

# want to round it up to 2 decimal places
rounded_number = format(customer_one_total, ".2f")
print(rounded_number)