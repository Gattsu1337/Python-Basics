from math import ceil
series = input()
episode = int(input())
work_break = int(input())

lunch = work_break / 8
rest = work_break / 4

free_time = work_break - (lunch + rest)
difference = abs(free_time - episode)
rounded = ceil(difference)
if free_time >= episode:
    print(f"You have enough time to watch {series} and left with {rounded} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {rounded} more minutes.")