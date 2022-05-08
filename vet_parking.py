days = int(input())
hours = int(input())
final_sum = 0
tax_for_day = 0
tax = 0
for d in range(1, days + 1):
    for h in range(1, hours +1):
        if h % 2 != 0 and d % 2 == 0:
            tax = 2.50
        elif h % 2 == 0 and d % 2 != 0:
            tax = 1.25
        else:
            tax = 1.00
        tax_for_day += tax
    print(f"Day: {d} - {tax_for_day:.2f} leva")
    final_sum += tax_for_day
    tax_for_day = 0
print(f"Total: {final_sum:.2f} leva")