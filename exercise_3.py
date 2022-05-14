desert = input()
number_of_deserts = int(input())
day_of_december = int(input())
price_of_desert = 0
if day_of_december <= 15:
    if desert == "Cake":
        price_of_desert = 24
    elif desert == "Souffle":
        price_of_desert = 6.66
    else:
        price_of_desert = 12.60
elif day_of_december > 15:
    if desert == "Cake":
        price_of_desert = 28.70
    elif desert == "Souffle":
        price_of_desert = 9.80
    else:
        price_of_desert = 16.98
overall_price = price_of_desert * number_of_deserts
if 100 <= overall_price <= 200 and day_of_december <= 22:
    overall_price *= 0.85
elif overall_price > 200 and day_of_december <= 22:
    overall_price *= 0.75
if day_of_december <= 15:
    overall_price *= 0.9
print(f"{overall_price: .2f}")
