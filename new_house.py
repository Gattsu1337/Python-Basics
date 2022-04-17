flowers_type = input()
number_of_flowers = int(input())
budget = int(input())
price_of_flower = 0

if flowers_type == 'Roses':
    price_of_flower = 5
    if number_of_flowers > 80:
        price_of_flower *= 0.9
elif flowers_type == 'Dahlias':
    price_of_flower = 3.80
    if number_of_flowers > 90:
        price_of_flower *= 0.85
elif flowers_type == 'Tulips':
    price_of_flower = 2.80
    if number_of_flowers > 80:
        price_of_flower *= 0.85
elif flowers_type == 'Narcissus':
    price_of_flower = 3
    if number_of_flowers < 120:
        price_of_flower *= 1.15
elif flowers_type == 'Gladiolus':
    price_of_flower = 2.50
    if number_of_flowers < 80:
        price_of_flower *= 1.20
total_sum = price_of_flower * number_of_flowers
difference = abs(total_sum - budget)
if total_sum <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
