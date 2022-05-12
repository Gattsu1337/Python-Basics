number_of_visitors = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake_enjoyers = 0
protein_bar_enjoyers = 0
buying = 0
training = 0
for x in range(number_of_visitors):
    activity = input()
    if activity == 'Back':
        back += 1
    elif activity == 'Chest':
        chest += 1
    elif activity == 'Legs':
        legs += 1
    elif activity == 'Abs':
        abs += 1
    elif activity == 'Protein shake':
        protein_shake_enjoyers += 1
    else:
        protein_bar_enjoyers += 1
    if activity in "Back Chest Legs Abs":
        training += 1
    else:
        buying += 1
percent_buying = buying / number_of_visitors * 100
percent_training = training / number_of_visitors * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake_enjoyers} - protein shake")
print(f"{protein_bar_enjoyers} - protein bar")
print(f"{percent_training:.2f}% - work out")
print(f"{percent_buying:.2f}% - protein")