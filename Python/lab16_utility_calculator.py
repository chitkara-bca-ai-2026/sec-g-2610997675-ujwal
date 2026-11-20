def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    return base ** exp


def format_number(n):
    if n == int(n):
        return int(n)
    return n


def is_number(text):
    text = text.strip()
    if text.startswith("-"):
        text = text[1:]
    parts = text.split(".")
    if len(parts) > 2:
        return False
    for p in parts:
        if p != "" and not p.isdigit():
            return False
    return text.replace(".", "") != ""


def get_number(prompt):
    while True:
        text = input(prompt)
        if is_number(text):
            return float(text)
        print("[ERROR] Please enter a valid number.")


history = []

print("=" * 40)
print("ENTERPRISE MODULAR UTILITY CALCULATOR".center(40))
print("=" * 40)

while True:
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice in ["1", "2", "3", "4", "5"]:
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        if choice == "1":
            result = add(a, b)
            symbol = "+"
        elif choice == "2":
            result = subtract(a, b)
            symbol = "-"
        elif choice == "3":
            result = multiply(a, b)
            symbol = "*"
        elif choice == "4":
            result = divide(a, b)
            symbol = "/"
        else:
            result = modulus(a, b)
            symbol = "%"

        if result is None:
            print("[ERROR] Cannot divide by zero.")
        else:
            record = f"{format_number(a)} {symbol} {format_number(b)} = {format_number(result)}"
            history.append(record)
            print("[RESULT]", record)

    elif choice == "6":
        base = get_number("Enter base: ")
        exp_text = input("Enter exponent (press Enter for default 2): ")
        if exp_text.strip() == "":
            result = power(base)
            exp = 2
        elif is_number(exp_text):
            exp = float(exp_text)
            result = power(base, exp)
        else:
            print("[ERROR] Please enter a valid number.")
            continue
        record = f"{format_number(base)} ^ {format_number(exp)} = {format_number(result)}"
        history.append(record)
        print("[RESULT]", record)

    elif choice == "7":
        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            print("\n--- Calculation History ---")
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")

    elif choice == "8":
        print("\nThank you for using the Utility Calculator. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 8.")
