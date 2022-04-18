from sys import maxsize

number = int(input())
highest_number = -maxsize
lowest_number = maxsize
for x in range(number):
    current_number = int(input())
    if current_number > highest_number:
        highest_number = current_number

    if current_number < lowest_number:
        lowest_number = current_number


print(f'Max number: {highest_number}')
print(f'Min number: {lowest_number}')