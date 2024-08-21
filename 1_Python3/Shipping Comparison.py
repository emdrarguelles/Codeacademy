# define weight
weight = 4.8

# Ground Shipping
GS_cost = ""

if weight <= 2:
    GS_cost = (1.5 * weight) + 20

elif weight > 2:
    if weight <= 6:
        GS_cost = (3 * weight) + 20

elif weight > 6:
    if weight <= 10:
        GS_cost = (4 * weight) + 20

elif weight > 10:
    GS_cost = (4.75 * weight) + 20

# Premium Ground Shipping
PGS_cost = 125

# Drone Shipping
DS_cost = ""

if weight <= 2:
    DS_cost = (4.5 * weight)

elif weight > 2:
    if weight <= 6:
        DS_cost = (9 * weight)

elif weight > 6:
    if weight <= 10:
        DS_cost = (12 * weight)

elif weight > 10:
    DS_cost = (14.25 * weight)

title = "Price Comparisons "
centered = title.center(40)
print(centered)
print("\nGround Shipping: ", GS_cost)
print("\nPremium Ground Shipping: ", + PGS_cost)
print("\nDrone Shipping: ", DS_cost)
