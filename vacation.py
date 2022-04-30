money_for_vacation = float(input())
owned_money = float(input())
days_counter = 0
days_spending = 0
money = 0
while owned_money < money_for_vacation:

    action = input()
    money = float(input())
    days_counter += 1
    if action == 'spend':
        owned_money -= money
        if owned_money < 0:
            owned_money = 0
        days_spending += 1
        if days_spending % 5 == 0:
            print(f"You can't save the money.")
            print(days_counter)
            break
    else:
        days_spending = 0
        owned_money += money
if owned_money >= money_for_vacation:
    print(f'You saved the money for {days_counter} days.')