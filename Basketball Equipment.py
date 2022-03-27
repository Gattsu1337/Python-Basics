anual_fee = int(input())

basketball_shoes = anual_fee - (anual_fee * 40 / 100)
basketball_outfit = basketball_shoes - (basketball_shoes * 20 / 100)
basketball = basketball_outfit * 25 / 100
basketball_accessories = basketball * 20 / 100

sum = anual_fee + basketball_accessories + basketball + basketball_outfit + basketball_shoes
print(sum)