width_of_space = int(input())
length_of_space = int(input())
height_of_space = int(input())
command = input()
volume_of_free_space = width_of_space * length_of_space * height_of_space
enough_space = True
occupied_space = 0
while command != 'Done':
    number_of_boxes = int(command)
    volume_of_free_space -= number_of_boxes
    if volume_of_free_space < 0:
        enough_space = False
        break
    command = input()
if not enough_space:
    print(f"No more free space! You need {abs(volume_of_free_space)} Cubic meters more.")
elif enough_space:
    print(f"{volume_of_free_space} Cubic meters left.")