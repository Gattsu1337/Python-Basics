desired_height = int(input())
starting_height = desired_height - 30
success = True
current_attempt = 0
attempt_counter = 0
failed_jumps = 0
while desired_height >= current_attempt:
    current_attempt = int(input())
    attempt_counter += 1
    while starting_height >= current_attempt:
        if current_attempt > starting_height:
            starting_height += 5
            failed_jumps = 0
        else:
            failed_jumps += 1
            if failed_jumps == 3:
                success = False
                break
if success:
    print(f"Tihomir succeeded, he jumped over {desired_height}cm after {attempt_counter} jumps.")
else:
    print(f"Tihomir failed at {starting_height}cm after {attempt_counter} jumps.")


