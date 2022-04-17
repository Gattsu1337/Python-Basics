number1 = int(input())
number2 = int(input())
operator = input()
odd_or_even = ''
if operator == '+':
    result = number1 + number2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    print(f'{number1} + {number2} = {result} - {odd_or_even}')
elif operator == '-':
    result = number1 - number2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    print(f'{number1} - {number2} = {result} - {odd_or_even}')
elif operator == '*':
    result = number1 * number2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    print(f'{number1} * {number2} = {result} - {odd_or_even}')
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
        print(f'{number1} / {number2} = {result:.2f}')
    else:
        print(f'Cannot divide {number1} by zero')
elif operator == '%':
    if number2 != 0:
        result = number1 % number2
        print(f'{number1} % {number2} = {result}')
    else:
        print(f'Cannot divide {number1} by zero')