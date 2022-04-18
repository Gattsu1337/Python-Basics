number = int(input())
left_sum = 0
right_sum = 0
for x in range(number):
    current_number_left = int(input())
    left_sum += current_number_left
for z in range(number):
    current_number_right = int(input())
    right_sum += current_number_right
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    difference = abs(left_sum - right_sum)
    print(f'No, diff = {difference}')