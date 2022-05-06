country = input()
device = input()
points_for_difficulty = 0
points_for_execution = 0
if device == 'ribbon':
    if country == 'Bulgaria':
        points_for_difficulty = 9.600
        points_for_execution = 9.400
    elif country == 'Russia':
        points_for_difficulty = 9.100
        points_for_execution = 9.400
    else:
        points_for_difficulty = 9.200
        points_for_execution = 9.500
elif device == 'hoop':
    if country == 'Bulgaria':
        points_for_difficulty = 9.550
        points_for_execution = 9.750
    elif country == 'Russia':
        points_for_difficulty = 9.300
        points_for_execution = 9.800
    else:
        points_for_difficulty = 9.450
        points_for_execution = 9.350
else:
    if country == 'Bulgaria':
        points_for_difficulty = 9.500
        points_for_execution = 9.400
    elif country == 'Russia':
        points_for_difficulty = 9.600
        points_for_execution = 9.000
    else:
        points_for_difficulty = 9.700
        points_for_execution = 9.150
final_points = points_for_execution + points_for_difficulty
if final_points < 20:
    difference = abs(20 - final_points) / 20 * 100
    print(f'The team of {country} get {final_points:.3f} on {device}.')
    print(f"{difference:.2f}%")
