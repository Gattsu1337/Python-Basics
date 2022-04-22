from sys import maxsize
number = int(input())
max_number = -maxsize
sum_of_numbers = 0
for z in range(0, number):
    current_number = int(input())
    sum_of_numbers += current_number
    if current_number > max_number:
        max_number = current_number
if max_number == sum_of_numbers - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    difference = abs(max_number - (sum_of_numbers - max_number))
    print('No')
    print(f'Diff = {difference}')