change = float(input())
change = int(change * 100)
counter = 0 #1.23
while change > 0:
    if change >= 200:
        change -= 200
        counter += 1
    elif change >= 100:
        change -= 100
        counter += 1
    elif change >= 50:
        change -= 50
        counter += 1
    elif change >= 20:
        change -= 20
        counter += 1
    elif change >= 10:
        change -= 10
        counter += 1
    elif change >= 5:
        change -= 5
        counter += 1
    elif change >= 2:
        change -= 2
        counter += 1
    elif change >= 1:
        change -= 1
        counter += 1
print(counter)





