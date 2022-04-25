number_of_groups = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for climbers in range(number_of_groups):
    people_per_group = int(input())
    if people_per_group < 6:
        p1 += people_per_group
    elif people_per_group < 13:
        p2 += people_per_group
    elif people_per_group < 26:
        p3 += people_per_group
    elif people_per_group < 41:
        p4 += people_per_group
    elif people_per_group >= 41:
        p5 += people_per_group
all_people = p1 + p2 + p3 + p4 + p5
print(f"{p1 / all_people * 100:.2f}%")
print(f"{p2 / all_people * 100:.2f}%")
print(f"{p3 / all_people * 100:.2f}%")
print(f"{p4 / all_people * 100:.2f}%")
print(f"{p5 / all_people * 100:.2f}%")