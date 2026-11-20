import math

print("=" * 40)
print("ENGINEERING CALCULATION TOOL".center(40))
print("=" * 40)

value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal = float(input("Enter a decimal measurement: "))

power = math.pow(value, exponent)
root = math.sqrt(value)
upper = math.ceil(decimal)
lower = math.floor(decimal)

print()
print("--- Results ---")
print(f"  {'Value':<19}: {value}")
print(f"  {'Exponent':<19}: {exponent}")
print(f"  {'Power (pow)':<19}: {power}")
print(f"  {'Square Root (sqrt)':<19}: {root:.4f}")
print(f"  {'Decimal Value':<19}: {decimal}")
print(f"  {'Ceil Value':<19}: {upper}")
print(f"  {'Floor Value':<19}: {lower}")
print("=" * 40)
