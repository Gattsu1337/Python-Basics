hour = int(input())
minutes = int(input())

added_minutes = 15
final_minutes = minutes + added_minutes
final_hour = hour

if final_minutes > 59:
    final_hour = hour + 1
    final_minutes -= 60

if final_hour > 23:
    final_hour -= 24

if final_minutes <= 9:
    print(f'{final_hour}:0{final_minutes}')
else:
    print(f'{final_hour}:{final_minutes}')
