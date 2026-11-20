import os

FILENAME = "document.txt"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("Artificial Intelligence is transforming modern industries.\n")
        f.write("Python provides powerful libraries for text processing and data analysis.\n")
        f.write("Developers use file handling to store and retrieve persistent records.\n")
        f.write("Modular programming ensures code is clean, reusable, and easy to maintain.\n")


def get_document_statistics(filename):
    with open(filename, "r") as f:
        content = f.read()
    line_count = len(content.splitlines())
    word_count = len(content.split())
    char_count = len(content)
    return line_count, word_count, char_count


def display_document(filename):
    print(f"--- Document Preview ({filename}) ---")
    with open(filename, "r") as f:
        for number, line in enumerate(f, 1):
            print(f"{number:>3} | {line.rstrip()}")


print("=" * 50)
print("DOCUMENT STATISTICS ANALYZER".center(50))
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        if not os.path.exists(FILENAME):
            print(f"[ERROR] File '{FILENAME}' not found.")
        else:
            lines, words, chars = get_document_statistics(FILENAME)
            print("=" * 15, "DOCUMENT REPORT", "=" * 15)
            print(f"Target File      : {FILENAME}")
            print(f"Total Lines      : {lines}")
            print(f"Total Words      : {words}")
            print(f"Total Characters : {chars}")
            print("=" * 46)

    elif choice == "2":
        if not os.path.exists(FILENAME):
            print(f"[ERROR] File '{FILENAME}' not found.")
        else:
            display_document(FILENAME)

    elif choice == "3":
        print("\nThank you for using Document Statistics Analyzer. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 3.")
