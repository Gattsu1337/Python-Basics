holiday = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2
price = puzzle * number_of_puzzles + talking_doll * number_of_dolls + teddy_bear * number_of_bears + minion * \
        number_of_minions + truck * number_of_trucks
toys_number = number_of_dolls + number_of_trucks + number_of_bears + number_of_minions + number_of_puzzles
if toys_number >= 50:
    discount = price * 0.25
else:
    discount = 0
total_sum = price - discount
rent = total_sum * 0.1
profit = total_sum - rent
if profit < holiday:
    needed_sum = holiday - profit
    print(f"Not enough money! {needed_sum:.2f} lv needed.")
else:
    left_sum = profit - holiday
    print(f"Yes! {left_sum:.2f} lv left.")