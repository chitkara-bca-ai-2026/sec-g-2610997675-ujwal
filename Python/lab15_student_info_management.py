students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": 2, "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": 1, "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": 1, "Marks": [74, 80, 82]},
}


def show_student(roll, s):
    print(f"Roll No: {roll}  | Name: {s['Name']:<10} | Branch: {s['Branch']} | Sem: {s['Semester']} | Marks: {s['Marks']}")


def view_all():
    print("\n--- Enrolled Student Records ---")
    for roll, s in students.items():
        show_student(roll, s)
    print("Total Enrolled Students:", len(students))


def search_student():
    roll = input("Enter Roll Number to search: ")
    s = students.get(roll)
    if s:
        print("[RECORD FOUND]")
        show_student(roll, s)
    else:
        print(f"[ERROR] No student found with Roll Number '{roll}'.")


def register_student():
    print("\n--- Register New Student ---")
    roll = input("Enter Roll Number: ")
    if roll in students:
        print(f"[ERROR] Roll Number '{roll}' already exists.")
        return
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    sem = int(input("Enter Semester: "))
    print("Enter marks for 3 subjects:")
    marks = []
    for i in range(1, 4):
        marks.append(int(input(f"  Subject {i}: ")))
    students[roll] = {"Name": name, "Branch": branch, "Semester": sem, "Marks": marks}
    print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")


def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll not in students:
        print(f"[ERROR] No student found with Roll Number '{roll}'.")
        return
    print("Select field to update:")
    print("1. Branch")
    print("2. Semester")
    field = input("Enter choice (1-2): ")
    if field == "1":
        students[roll]["Branch"] = input("Enter new Branch: ")
        print("[SUCCESS] Branch updated successfully.")
    elif field == "2":
        students[roll]["Semester"] = int(input("Enter new Semester: "))
        print("[SUCCESS] Semester updated successfully.")
    else:
        print("[ERROR] Invalid field choice.")


def academic_performance():
    roll = input("Enter Roll Number for Academic Performance: ")
    student = students.get(roll)
    if student is None:
        print(f"[ERROR] No student found with Roll Number '{roll}'.")
        return
    total = sum(student["Marks"])
    maximum = len(student["Marks"]) * 100
    average = total / len(student["Marks"])
    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"
    print()
    print("=" * 16, "ACADEMIC REPORT", "=" * 16)
    print(f"Student Name : {student['Name']} (Roll: {roll})")
    print(f"Subject Marks: {student['Marks']}")
    print(f"Total Marks  : {total} / {maximum}")
    print(f"Average Marks: {average:.2f}%")
    print(f"Final Result : {result}")
    print("=" * 48)


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    removed = students.pop(roll, None)
    if removed:
        print(f"\n[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
    else:
        print(f"\n[ERROR] No student found with Roll Number '{roll}'.")


print("=" * 50)
print("STUDENT INFORMATION SYSTEM".center(50))
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        view_all()
    elif choice == "2":
        search_student()
    elif choice == "3":
        register_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        academic_performance()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        print("\nThank you for using Student Information System. Goodbye!")
        break
    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 7.")
