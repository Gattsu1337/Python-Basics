month = input()
days = int(input())
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    studio_cost = studio_price * days
    apartment_cost = apartment_price * days
    if 14 >= days > 7:
        studio_cost *= 0.95
    elif days > 14:
        studio_cost *= 0.7
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    studio_cost = studio_price * days
    apartment_cost = apartment_price * days
    if days > 14:
        studio_cost *= 0.8
else:
    studio_price = 76
    apartment_price = 77
    studio_cost = studio_price * days
    apartment_cost = apartment_price * days
if days > 14:
    apartment_cost *= 0.9
print(f'Apartment: {apartment_cost:.2f} lv.')
print(f'Studio: {studio_cost:.2f} lv.')
