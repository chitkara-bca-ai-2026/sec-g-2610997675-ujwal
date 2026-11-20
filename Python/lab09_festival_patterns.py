n = int(input("Enter the number of rows: "))

print()
print("Pattern 1: Star Triangle")
print("-" * 30)
for i in range(1, n + 1):
    print(" ".join("*" * i))

print()
print("Pattern 2: Number Triangle")
print("-" * 30)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" " if j < i else "")
    print()

print()
print("Pattern 3: Inverted Star Triangle")
print("-" * 30)
for i in range(n, 0, -1):
    print(" ".join("*" * i))

print()
print("Pattern 4: Pyramid")
print("-" * 30)
for i in range(1, n + 1):
    spaces = " " * ((n - i) * 2)
    stars = " ".join("*" * (2 * i - 1))
    print(spaces + stars)
