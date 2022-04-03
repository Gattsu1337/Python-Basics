budget = float(input())
video = int(input())
processor = int(input())
ram = int(input())

price_video = video * 250
price_processor = price_video * 0.35
price_ram = price_video * 0.1

total_cost = price_video + processor * price_processor + ram * price_ram
discount = 0
if video > processor:
    discount = total_cost * 0.15
total_sum = total_cost - discount
difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")