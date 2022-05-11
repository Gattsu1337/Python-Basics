people_in_jury = int(input())
name_of_presentation = input()
current_average = 0
final_grade = 0
current_grade = 0
total_grades = 0
while name_of_presentation != "Finish":
    for grades in range(1, people_in_jury + 1):
        current_grade = float(input())
        total_grades += 1
        current_average += current_grade
        final_grade += current_grade
    current_average /= people_in_jury
    print(f"{name_of_presentation} - {current_average:.2f}.")
    current_average = 0
    name_of_presentation = input()
final_grade /= total_grades
print(f"Student's final assessment is {final_grade:.2f}.")