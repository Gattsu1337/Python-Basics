from math import floor
number_of_processors = int(input())
number_of_employees = int(input())
work_days = int(input())
work_time = number_of_employees * work_days * 8
processors_made = floor(work_time / 3)
difference = abs(processors_made - number_of_processors)
difference *= 110.10
if processors_made < number_of_processors:
    print(f"Losses: -> {difference:.2f} BGN")
else:
    print(f"Profit: -> {difference:.2f} BGN")