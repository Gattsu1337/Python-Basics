lenght = int(input())
width = int(input())
height = int (input())
percentage = float(input())

volume = lenght * width * height
water = (volume - (volume * percentage / 100)) / 1000
print(water)