from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message

time_now = dt.now()
print(f"The date today is {time_now:%A, %B %d, %Y at %I:%M %p}.\n")

target_year = randint(1800, 3001)

base_cost = Decimal("1.00")
cost_multiplier = abs(time_now.year - target_year)
final_cost = base_cost * cost_multiplier
#print(final_cost)

destinations = ["Paris", "Germany", "Japan", "Prague", "Taiwan", "Korea", "Siargao"]

target_destination = choice(destinations)
#print(target_destination)

generate_time_travel_message(target_year, target_destination, final_cost)