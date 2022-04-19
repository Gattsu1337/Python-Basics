number = int(input())
even_sum = 0
odd_sum = 0
for x in range(number):
    current_number = int(input())
    if x % 2 == 0:
        even_sum += current_number
    elif x % 2 != 0:
        odd_sum += current_number
if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    difference = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {difference}')