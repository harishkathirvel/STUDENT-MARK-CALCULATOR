print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    try:
        mark = float(input(f"Enter marks for subject {i} (0-100): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        raise SystemExit

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        raise SystemExit

    marks.append(mark)

total = sum(marks)
percentage = total / 5

if any(mark < 35 for mark in marks):
    grade = "F"
    result = "FAIL"
elif percentage >= 90:
    grade = "A+"
    result = "PASS"
elif percentage >= 80:
    grade = "A"
    result = "PASS"
elif percentage >= 70:
    grade = "B"
    result = "PASS"
elif percentage >= 60:
    grade = "C"
    result = "PASS"
else:
    grade = "D"
    result = "PASS"

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)
