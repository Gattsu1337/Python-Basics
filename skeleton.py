minutes = int(input())
seconds = int(input())
seconds += minutes * 60
lenght = float(input())
seconds_for_one_hundred_meters = int(input())
delay = lenght / 120 * 2.5
total_time = (lenght / 100) * seconds_for_one_hundred_meters - delay
difference = abs(seconds - total_time)
if total_time > seconds:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
else:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")