import csv
import os

FILENAME = "students_data.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["RollNo", "Name", "Subject", "Marks"])
        writer.writerow([101, "Aman", "Python", 85])
        writer.writerow([102, "Riya", "Python", 92])
        writer.writerow([103, "Karan", "Python", 45])
        writer.writerow([104, "Neha", "Python", 78])
        writer.writerow([105, "Rohit", "Python", 38])
        writer.writerow([106, "Pooja", "Python", 62])


def print_header(title):
    print(f"{' ' + title + ' ':=^50}")
    print(f"{'Roll No':<11}{'Name':<17}{'Subject':<12}{'Marks'}")
    print("-" * 44)


def read_all_students(filename):
    print_header("ALL ENROLLED STUDENTS")
    count = 0
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['RollNo']:<11}{row['Name']:<17}{row['Subject']:<12}{row['Marks']}")
            count += 1
    print("=" * 44)
    print("Total Records:", count)


def filter_students_above_threshold(filename, threshold=50):
    print_header(f"STUDENTS WITH MARKS > {threshold}")
    count = 0
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["Marks"]) > threshold:
                print(f"{row['RollNo']:<11}{row['Name']:<17}{row['Subject']:<12}{row['Marks']}")
                count += 1
    print("=" * 44)
    print("Qualified Students Count:", count)


print("=" * 50)
print("STUDENT RESULT ANALYSIS SYSTEM".center(50))
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. Display All Students from CSV")
    print("2. Filter Students (Marks > 50)")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        read_all_students(FILENAME)

    elif choice == "2":
        filter_students_above_threshold(FILENAME)

    elif choice == "3":
        print("\nThank you for using Student Result Analysis System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 3.")
