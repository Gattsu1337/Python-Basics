savings = 0
current_sum = 0
destination = input()
while destination != 'End':
    min_budget = float(input())
    while min_budget > savings:
        current_sum = float(input())
        savings += current_sum
    print(f'Going to {destination}!')
    savings = 0
    destination = input()

