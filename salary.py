opened_tabs = int(input())
salary = float(input())
penalty = 0
for websites in range(1, opened_tabs + 1):
    name_of_website = input()
    if name_of_website == 'Facebook':
        penalty += 150
    elif name_of_website == 'Instagram':
        penalty += 100
    elif name_of_website == 'Reddit':
        penalty += 50
if penalty >= salary:
    print('You have lost your salary.')
else:
    difference = abs(salary - penalty)
    print(f'{round(difference)}')
