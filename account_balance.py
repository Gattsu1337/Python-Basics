money = 0
while True:
    current_payment = input()
    if current_payment == 'NoMoreMoney':
        break
    elif float(current_payment) < 0:
        print(f'Invalid operation!')
        break
    money += float(current_payment)
    print(f'Increase: {float(current_payment):.2f}')
print(f'Total: {money:.2f}')