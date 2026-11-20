print("=" * 50)
print("SCHOOL RESULT PROCESSING".center(50))
print("=" * 50)

name = input("Enter Student Name : ")
roll = input("Enter Roll Number  : ")

print()
print("--- Enter Marks for 5 Subjects (0-100) ---")

total = 0.0
failed = False

for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    if marks < 0 or marks > 100:
        print("Error: marks must be between 0 and 100.")
        exit()
    if marks < 40:
        failed = True
    total += marks

percentage = (total / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    else:
        grade = "E"
        remark = "Pass"

print()
print("=" * 50)
print("STUDENT REPORT CARD".center(50))
print("=" * 50)
print(f"  {'Student Name':<13}: {name}")
print(f"  {'Roll Number':<13}: {roll}")
print("-" * 50)
print(f"  {'Total Marks':<13}: {total} / 500.0")
print(f"  {'Percentage':<13}: {percentage:.2f}%")
print(f"  {'Result':<13}: {result}")
print(f"  {'Grade':<13}: {grade}")
print(f"  {'Remarks':<13}: {remark}")
print("=" * 50)
