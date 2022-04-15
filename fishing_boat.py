budget = int(input())
season = input()
number_of_fishermen = int(input())
rental_price = 0
if season == 'Spring':
    rental_price = 3000
elif season == 'Summer' or season == 'Autumn':
    rental_price = 4200
elif season == 'Winter':
    rental_price = 2600
if number_of_fishermen <= 6:
    rental_price *= 0.9
elif number_of_fishermen <= 11:
    rental_price *= 0.85
else:
    rental_price *= 0.75
if season != 'Autumn' and number_of_fishermen % 2 == 0:
    rental_price *= 0.95
difference = abs(budget - rental_price)
if budget >= rental_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")