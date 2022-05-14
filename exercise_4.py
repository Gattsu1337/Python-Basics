price_per_kilo = 12.45
number_of_cats = int(input())
group1 = 0
group2 = 0
group3 = 0
total_grams = 0
for x in range(number_of_cats):
    grams_of_food = float(input())
    total_grams += grams_of_food
    if 100 <= grams_of_food < 200:
        group1 += 1
    elif 200 <= grams_of_food < 300:
        group2 += 1
    elif 300 <= grams_of_food < 400:
        group3 += 1
kilos_of_food = total_grams / 1000
total_price = price_per_kilo * kilos_of_food
print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")