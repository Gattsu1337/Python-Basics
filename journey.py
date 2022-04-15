budget = float(input())
season = input()
destination = ''
place = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        budget *= 0.3
        place = 'Camp'
    else:
        budget *= 0.7
        place = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        budget *= 0.4
        place = 'Camp'
    else:
        budget *= 0.8
        place = 'Hotel'
else:
    destination = 'Europe'
    budget *= 0.9
if destination == 'Europe':
    place = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")