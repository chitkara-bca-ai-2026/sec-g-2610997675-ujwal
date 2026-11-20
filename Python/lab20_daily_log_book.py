import os

FILENAME = "daily_log.txt"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("09:00 AM - System server startup verified.\n")
        f.write("10:30 AM - Morning attendance synchronized.\n")
        f.write("02:15 PM - Network security patch applied.\n")


def append_entry(filename, entry):
    with open(filename, "a") as f:
        f.write(entry + "\n")
    print(f"[SUCCESS] New entry logged to '{filename}'.")


def display_log(filename):
    count = 0
    print("=" * 15, "DAILY LOG BOOK", "=" * 15)
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            count += 1
            print(f"[{count:02d}] {line.strip()}")
    print("\nTotal Logged Entries:", count)
    print("=" * 46)


print("=" * 50)
print("OFFICE DAILY LOG BOOK".center(50))
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        entry = input("Enter log entry: ")
        append_entry(FILENAME, entry)

    elif choice == "2":
        display_log(FILENAME)

    elif choice == "3":
        print("\nThank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 3.")
