total_days = int(input())
days_of_stay = total_days - 1
accommodation_type = input()
rating = input()
cost_per_day = 0
if accommodation_type == 'room for one person':
    cost_per_day = 18.00
    final_sum = cost_per_day * days_of_stay
elif accommodation_type == 'apartment':
    cost_per_day = 25.00
    final_sum = cost_per_day * days_of_stay
    if days_of_stay < 10:
        final_sum *= 0.7
    elif 10 <= days_of_stay <= 15:
        final_sum *= 0.65
    else:
        final_sum *= 0.5
else:
    cost_per_day = 35.00
    final_sum = cost_per_day * days_of_stay
    if days_of_stay < 10:
        final_sum *= 0.9
    elif 10 <= days_of_stay <= 15:
        final_sum *= 0.85
    else:
        final_sum *= 0.8
if rating == 'positive':
    final_sum *= 1.25
else:
    final_sum *= 0.9

print(f"{final_sum:.2f}")
