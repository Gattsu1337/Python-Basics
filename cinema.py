type = input()
rows = int(input())
collons = int(input())
if type == 'Premiere':
    ticket = 12.00
elif type == 'Normal':
    ticket = 7.50
elif type == 'Discount':
    ticket = 5.00
income = rows * collons * ticket
print(f'{income:.2f}')