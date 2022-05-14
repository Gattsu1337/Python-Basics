number_of_locations = int(input())
average_gold = 0
for location in range(number_of_locations):
    expected_average_gold = float(input())
    days_spent_digging = int(input())
    for current_day in range(days_spent_digging):
        gold_earned_that_day = float(input())
        average_gold += gold_earned_that_day
    average_gold /= days_spent_digging
    difference = abs(average_gold - expected_average_gold)
    if average_gold < expected_average_gold:
        print(f"You need {difference:.2f} gold.")
    else:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    average_gold = 0