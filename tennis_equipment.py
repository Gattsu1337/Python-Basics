from math import floor, ceil
cost_for_racket = float(input())
cost_for_shoes = cost_for_racket / 6
rackets = int(input())
shoes = int(input())
other_equipment = 0
sum1 = rackets * cost_for_racket + shoes * cost_for_shoes
other_equipment = sum1 * 0.2
final_cost = sum1 + other_equipment
Djokovic = final_cost / 8
sponsors = final_cost * 7 / 8
print(f"Price to be paid by Djokovic {floor(Djokovic)}")
print(f"Price to be paid by sponsors {ceil(sponsors)}")
