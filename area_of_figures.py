from math import pi, floor, ceil

shape = input()

if shape == "square":
    side_a = float(input())
    area = side_a * side_a
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif shape == "circle":
    radius = float(input())
    area = pi * radius * radius
elif shape == "triangle":
    side_a = float(input())
    height = float(input())
    area = side_a * height / 2

print(f"{area:.3f}")