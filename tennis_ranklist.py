from math import floor
number_of_tournaments = int(input())
starting_points = int(input())
total_points = starting_points
won_tournaments = 0
for aaa in range(number_of_tournaments):
    reached_round = input()
    if reached_round == 'W':
        total_points += 2000
        won_tournaments += 1
    elif reached_round == 'F':
        total_points += 1200
    else:
        total_points += 720
average = (total_points - starting_points) / number_of_tournaments

percentage = won_tournaments / number_of_tournaments * 100
print(f'Final points: {total_points}')
print(f'Average points: {floor(average)}')
print(f'{percentage:.2f}%')