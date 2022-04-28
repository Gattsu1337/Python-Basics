failed_threshold = int(input())
poor_grades_counter = 0
failed = False
total_problems = 0
average = 0
last_problem = ""
current_problem = input()
while current_problem != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        poor_grades_counter += 1
        if poor_grades_counter == failed_threshold:
            failed = True
            break
    average += current_grade
    total_problems += 1
    last_problem = current_problem
    current_problem = input()
if failed:
    print(f"You need a break, {failed_threshold} poor grades.")
else:
    average /= total_problems
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {total_problems}")
    print(f"Last problem: {last_problem}")