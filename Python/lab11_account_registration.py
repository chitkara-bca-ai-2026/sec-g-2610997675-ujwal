username = input("Enter your username: ")
password = input("Enter your password: ")

length = len(password)
has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

long_enough = length >= 8

print("=" * 40)
print("PASSWORD VALIDATION REPORT")
print("=" * 40)
print("Username:", username)
print("Password:", "*" * length)

print()
print("--- Validation Rules ---")

if long_enough:
    print(f"[PASS] Minimum 8 characters ({length} characters)")
else:
    print(f"[FAIL] Minimum 8 characters ({length} characters)")

if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if has_upper:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print()
print("--- Result ---")

if long_enough and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print()
print("=" * 40)
