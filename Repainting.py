amount_of_nylon = int(input())
amount_of_paint = int(input())
amount_of_diluent = int(input())
amount_of_hours = int(input())

nylon = (amount_of_nylon + 2.00) * 1.50
paint = (amount_of_paint + amount_of_paint * 10 / 100) * 14.50
diluent = amount_of_diluent * 5.00
bags = 0.40
sum = (nylon + paint + diluent + bags)
worker_pay = amount_of_hours * (sum * (30 / 100))
final_sum = sum + worker_pay

print(final_sum)