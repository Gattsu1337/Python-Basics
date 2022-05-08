number_of_products = 0
budget = float(input())
final_sum = 0
while budget >= final_sum:
    product = input()
    if product == 'Stop':
        break
    number_of_products += 1
    price_of_product = float(input())
    if number_of_products % 3 == 0:
        price_of_product *= 0.5
    final_sum += price_of_product
if budget < final_sum:
    difference = abs(budget - final_sum)
    print(f"You don't have enough money!")
    print(f"You need {difference:.2f} leva!")
else:
    print(f'You bought {number_of_products} products for {final_sum:.2f} leva.')

