print("=" * 40)
print("CLOTHING STORE BILLING SYSTEM".center(40))
print("=" * 40)

customer = input("Enter Customer Name: ")
garment = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

total = price * quantity

print()
print("=" * 40)
print("BILL".center(40))
print("=" * 40)
print(f"  {'Customer Name':<15}: {customer}")
print(f"  {'Garment Name':<15}: {garment}")
print(f"  {'Price per Unit':<15}: Rs. {price}")
print(f"  {'Quantity':<15}: {quantity}")
print(f"  {'Total Amount':<15}: Rs. {total}")
print("=" * 40)
