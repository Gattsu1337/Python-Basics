current_number = 1
number = int(input())
all_is_printed = False
for rows in range(1, number + 1):
    for colons in range(1, rows + 1):

        print(current_number, end=' ')
        current_number += 1
        if current_number > number:
            all_is_printed = True
            break
    if all_is_printed:
        break
    print()
