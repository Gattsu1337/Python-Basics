all_steps = 0
steps_on_way_home = 0
command = input()
goal_reached = False
while all_steps < 10000:
    if command != 'Going home':
        all_steps += int(command)
    else:
        steps_on_way_home = int(input())
        all_steps += steps_on_way_home
        break
    if all_steps >= 10000:
        goal_reached = True
        break
    command = input()
if all_steps >= 10000:
    goal_reached = True
difference = abs(all_steps - 10000)
if goal_reached:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")