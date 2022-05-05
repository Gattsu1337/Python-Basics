combinations = 0
no_combinations = True
starting_interval = int(input())
ending_interval = int(input())
magical_number = int(input())
for n1 in range(starting_interval, ending_interval + 1):
    for n2 in range(starting_interval, ending_interval + 1):
        combinations += 1
        if n1 + n2 == magical_number:
            no_combinations = False
            print(f'Combination N:{combinations} ({n1} + {n2} = {magical_number})')
            break
    if not no_combinations:
        break
if no_combinations:
    print(f'{combinations} combinations - neither equals {magical_number}')
