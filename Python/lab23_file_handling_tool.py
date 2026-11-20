import os

FILENAME = "student_marks.txt"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("Aman,85\n")
        f.write("Riya,92\n")
        f.write("Karan,78\n")


def store_student(filename, name, marks):
    with open(filename, "a") as f:
        f.write(f"{name},{marks}\n")
    print(f"[SUCCESS] Record for '{name}' ({marks} marks) stored successfully.")


def display_and_calculate_average(filename):
    if not os.path.exists(filename):
        print("[ERROR] No records file found yet.")
        return

    names = []
    marks_list = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            parts = line.strip().split(",")
            names.append(parts[0])
            marks_list.append(int(parts[1]))

    if len(marks_list) == 0:
        print("[INFO] No student records stored yet.")
        return

    total_marks = sum(marks_list)
    avg = total_marks / len(marks_list)

    print("=" * 9, "STUDENT MARKS LEDGER", "=" * 9)
    print(f"{'No.':<6}{'Student Name':<20}{'Marks Obtained'}")
    print("-" * 44)
    for i in range(len(names)):
        print(f"{i + 1:<6}{names[i]:<20}{marks_list[i]}")
    print("=" * 40)
    print("Total Students :", len(marks_list))
    print("Total Marks    :", total_marks)
    print(f"Class Average  : {avg:.2f}")
    print("=" * 40)


print("=" * 50)
print("STUDENT MARKS FILE HANDLING TOOL".center(50))
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. Display Records & Class Average")
    print("2. Add & Store Student Marks")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        display_and_calculate_average(FILENAME)

    elif choice == "2":
        name = input("Enter Student Name: ")
        marks = int(input("Enter Marks (0-100): "))
        if marks < 0 or marks > 100:
            print("[ERROR] Marks must be between 0 and 100.")
        else:
            store_student(FILENAME, name, marks)

    elif choice == "3":
        print("\nThank you for using Student Marks Tool. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 3.")
