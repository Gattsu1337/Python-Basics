floors = int(input())
rooms_per_floor = int(input())
room_numbers = ''
for f in range(floors, 0, -1):
    for r in range(rooms_per_floor):
        current_number_of_rooms = f * 10 + r
        if floors == f:
            print(f'L{current_number_of_rooms} ', end='')
        elif f % 2 != 0:
            room_numbers += f'A{current_number_of_rooms} '
        else:
            room_numbers += f'O{current_number_of_rooms} '
    print(room_numbers)
    room_numbers = ''
