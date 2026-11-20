import os


def write_notes(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")


def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    return "No notes file exists yet. Please write some notes first."


print("=" * 50)
print("STUDENT NOTES MANAGEMENT SYSTEM".center(50))
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        text = input("Enter notes to save: ")
        write_notes("notes.txt", text)

    elif choice == "2":
        print("--- Notes Content (notes.txt) ---")
        print(read_notes("notes.txt"))

    elif choice == "3":
        print("\nThank you for using the Notes Management System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 3.")
