number = int(input())
sum_of_numbers = 0
while True:
    if number <= sum_of_numbers:
        break
    current_number = int(input())
    sum_of_numbers += current_number

print(sum_of_numbers)