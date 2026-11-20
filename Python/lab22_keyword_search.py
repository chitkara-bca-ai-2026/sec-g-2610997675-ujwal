import os

FILENAME = "report.txt"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("Annual Technology and AI Progress Report.\n")
        f.write("The adoption of Artificial Intelligence accelerated across business units.\n")
        f.write("AI algorithms improved diagnostic accuracy in healthcare operations.\n")
        f.write("Data engineering pipelines were upgraded to support real-time data streaming.\n")
        f.write("The company plans further investments in AI research and machine learning.\n")


def search_keyword(filename, keyword):
    total = 0
    print(f"--- Search Results for '{keyword}' ---")
    with open(filename, "r") as f:
        for line_no, line in enumerate(f, start=1):
            count = line.lower().count(keyword.lower())
            if count > 0:
                total += count
                word = "match" if count == 1 else "matches"
                print(f"Line {line_no:>2} ({count} {word}): {line.strip()}")
    print()
    if total > 0:
        print(f"[FOUND] Total occurrences of '{keyword}': {total}")
    else:
        print(f"[NOT FOUND] '{keyword}' does not appear in the document.")


def display_document(filename):
    print(f"--- Full Report Document ({filename}) ---")
    with open(filename, "r") as f:
        for number, line in enumerate(f, 1):
            print(f"{number:>2} | {line.rstrip()}")


print("=" * 50)
print("KEYWORD SEARCH UTILITY".center(50))
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. Search Keyword in Document")
    print("2. View Full Document")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        keyword = input("Enter keyword to search: ").strip()
        if keyword == "":
            print("[ERROR] Keyword cannot be empty.")
        else:
            search_keyword(FILENAME, keyword)

    elif choice == "2":
        display_document(FILENAME)

    elif choice == "3":
        print("\nThank you for using Keyword Search Utility. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 3.")
