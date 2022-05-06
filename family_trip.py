budget = float(input())
nights_of_stay = int(input())
cost_per_night = float(input())
tax_percent = int(input())

budget_after_expenses = budget - (budget * (tax_percent / 100))
if nights_of_stay > 7:
    cost_per_night *= 0.95
cost = nights_of_stay * cost_per_night

difference = abs(budget_after_expenses - cost)
if budget_after_expenses >= cost:
    print(f'Ivanovi will be left with {difference:.2f} leva after vacation.')
else:
    print(f'{difference:.2f} leva needed.')