amount_of_bought_food = int(input()) * 1000
no_more_food = False
command = input()
total_eaten_food = 0
while command != 'Adopted':
    eaten_food = int(command)
    total_eaten_food += eaten_food
    command = input()
difference = abs(amount_of_bought_food - total_eaten_food)
if amount_of_bought_food < total_eaten_food:
    no_more_food = True
if no_more_food:
    print(f"Food is not enough. You need {difference} grams more.")
else:
    print(f"Food is enough! Leftovers: {difference} grams.")