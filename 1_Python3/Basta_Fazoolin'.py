from datetime import time
from datetime import datetime

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

  def calculate_bill(self, purchased_items):
    total_cost = 0
    for item in purchased_items:
      total_cost += self.items[item]
    return total_cost

b_start_time = str(time(11, 0))
b_end_time = str(time(16, 0))

b_start_time_obj = datetime.strptime(b_start_time, "%H:%M:%S")
b_end_time_obj = datetime.strptime(b_end_time, "%H:%M:%S")

b_readable_start_time = b_start_time_obj.strftime("%I:%M %p")
b_readable_end_time = b_end_time_obj.strftime("%I:%M %p")

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},b_readable_start_time, b_readable_end_time)

e_start_time = str(time(15, 0))
e_end_time = str(time(18, 0))

e_start_time_obj = datetime.strptime(e_start_time, "%H:%M:%S")
e_end_time_obj = datetime.strptime(e_end_time, "%H:%M:%S")

e_readable_start_time = e_start_time_obj.strftime("%I:%M %p")
e_readable_end_time = e_end_time_obj.strftime("%I:%M %p")

early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, e_readable_start_time, e_readable_end_time)

d_start_time = str(time(17, 0))
d_end_time = str(time(23, 0))

d_start_time_obj = datetime.strptime(d_start_time, "%H:%M:%S")
d_end_time_obj = datetime.strptime(d_end_time, "%H:%M:%S")

d_readable_start_time = d_start_time_obj.strftime("%I:%M %p")
d_readable_end_time = d_end_time_obj.strftime("%I:%M %p")

dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, d_readable_start_time, d_readable_end_time)

k_start_time = str(time(11, 0))
k_end_time = str(time(21, 0))

k_start_time_obj = datetime.strptime(k_start_time, "%H:%M:%S")
k_end_time_obj = datetime.strptime(k_end_time, "%H:%M:%S")

k_readable_start_time = k_start_time_obj.strftime("%I:%M %p")
k_readable_end_time = k_end_time_obj.strftime("%I:%M %p")

kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, k_readable_start_time, k_readable_end_time)

a_start_time = str(time(10, 0))
a_end_time = str(time(20, 0))

a_start_time_obj = datetime.strptime(a_start_time, "%H:%M:%S")
a_end_time_obj = datetime.strptime(a_end_time, "%H:%M:%S")

a_readable_start_time = a_start_time_obj.strftime("%I:%M %p")
a_readable_end_time = a_end_time_obj.strftime("%I:%M %p")

arepas_menu = Menu("arepas_menu", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},a_readable_start_time, a_readable_end_time)

#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#print(arepas_menu.calculate_bill(['arepa pabellon', 'pernil arepa']))

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "The address of that franchise is {}".format(self.address)
  
  def available_menus(self, time):
    available_items = []
    for menu in self.menus:
      if datetime.strptime(menu.start_time, "%I:%M %p").time() <= time <= datetime.strptime(menu.end_time, "%I:%M %p").time():
        available_items.append(menu)
    return available_items
    
all_menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", all_menus)

new_installment = Franchise("12 East Mulberry Street", all_menus)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#print(flagship_store.available_menus(time(12, 0)))

#print(flagship_store.available_menus(time(17, 0)))

#print(arepas_place.available_menus(time(17, 0)))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

all_franchises = [flagship_store, new_installment]
basta_fooling = Business("Basta Fazoolin' with my Heart", all_franchises)

arepa_business = Business("Take a' Arepa", [arepas_place])

