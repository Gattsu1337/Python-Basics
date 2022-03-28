chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())




#Пилешко меню – 10.35 лв.
chicken_price = chicken_menus * 10.35
#Меню с риба – 12.40 лв.
fish_price = fish_menus * 12.40
#Вегетарианско меню – 8.15 лв.
vegan_price = vegan_menus * 8.15
sum = chicken_price + fish_price + vegan_price
desert = (20 / 100) * sum
delivery = 2.50

final_sum = sum + desert + delivery

print(final_sum)
#Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
#Цената на доставка е 2.50 лв и се начислява най-накрая.

#Да се отпечата на конзолата един ред: &quot;{цена на поръчката}&quot;