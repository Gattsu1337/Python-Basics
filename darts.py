player = input()
command = input()
retired = True
starting_points = 301
successful_shots = 0
unsuccessful_shots = 0
while command != 'Retire':
    area = command
    points = int(input())
    if area == 'Double':
        points *= 2
    elif area == 'Triple':
        points *= 3
    if points > starting_points:
        points = 0
        unsuccessful_shots += 1
        successful_shots -= 1
    starting_points -= points
    successful_shots += 1
    if starting_points == 0:
        retired = False
        break
    command = input()
if not retired:
    print(f"{player} won the leg with {successful_shots} shots.")
else:
    print(f"{player} retired after {unsuccessful_shots} unsuccessful shots.")
