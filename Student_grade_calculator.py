# 1. Student Grade Calculator

def grade_calculator(subject_marks):
    total = sum(subject_marks)
    print(f"The total marks you get in 5 subjects: {total}/500.")
    perc = (total / 500) * 100
    print(f"The percentage you get: {perc}%.")
    if perc > 90:
        print("Your Grade: O")
    elif perc <= 90 and perc > 80:
        print("Your Grade: A+")
    elif perc <= 80 and perc > 70:
        print("Your Grade: A")
    elif perc <= 70 and perc > 60:
        print("Your Grade: B+")
    elif perc <= 60 and perc > 50:
        print("Your Grade: B")
    elif perc <= 50 and perc >= 40:
        print("Your Grade: C+")
    elif perc <= 40 and perc > 33:
        print("Your Grade: C")
    else:
        print("Your Grade: F")

student_name = input("Enter the student name:")
subject_marks = []

try:
    for i in range(1, 6):
        sub_mark = float(input(f"Enter subject {i} marks:"))
        if sub_mark < 0 or sub_mark > 100:
            raise ValueError("\"Marks must lie between 0 - 100\"")
        subject_marks.append(sub_mark)

    print(f"Student Name: {student_name}")
    grade_calculator(subject_marks)
except ValueError as e:
    print(f"An error occured: {e}.")
