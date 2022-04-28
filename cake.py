width = int(input())
length = int(input())
volume = width * length
number_of_slices = input()
all_slices = 0
cake_is_over = False
while number_of_slices != 'STOP':
    number_of_slices = int(number_of_slices)
    volume -= number_of_slices
    if volume < 0:
        cake_is_over = True
        break
    number_of_slices = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(volume)} pieces more.")
else:
    print(f"{volume} pieces are left.")
