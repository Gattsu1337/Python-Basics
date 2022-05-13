championship_round = input()
type_of_ticket = input()
numbers_of_tickets = int(input())
photo = input()
paid_photo = True
ticket_cost = 0
if championship_round == 'Quarter final':
    if type_of_ticket == 'Standard':
        ticket_cost = 55.50
    elif type_of_ticket == 'Premium':
        ticket_cost = 105.20
    else:
        ticket_cost = 118.90
elif championship_round == 'Semi final':
    if type_of_ticket == 'Standard':
        ticket_cost = 75.88
    elif type_of_ticket == 'Premium':
        ticket_cost = 125.22
    else:
        ticket_cost = 300.40
else:
    if type_of_ticket == 'Standard':
        ticket_cost = 110.10
    elif type_of_ticket == 'Premium':
        ticket_cost = 160.66
    else:
        ticket_cost = 400
money_for_tickets = ticket_cost * numbers_of_tickets
if money_for_tickets > 4000:
    money_for_tickets *= 0.75
    paid_photo = False
elif money_for_tickets > 2500:
    money_for_tickets *= 0.9
if photo == 'Y' and paid_photo == True:
    money_for_tickets += 40 * numbers_of_tickets
print(f"{money_for_tickets:.2f}")
