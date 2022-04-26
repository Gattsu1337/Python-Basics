name = input()
failed_classes = 0
grade = 1
average = 0
while grade <= 12:
    current_grade = float(input())
    if current_grade < 4.00:
        failed_classes += 1
        if failed_classes > 1:
            break
    else:
        grade += 1
        average += current_grade


if failed_classes > 1:
    print(f'{name} has been excluded at {grade} grade')
else:
    print(f'{name} graduated. Average grade: {average / 12:.2f}')

