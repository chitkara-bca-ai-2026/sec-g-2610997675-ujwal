print("=" * 50)
print("DATA CONVERSION UTILITY".center(50))
print("=" * 50)

product_name = input("Enter Product Name : ")
price = float(input("Enter Price        : "))
quantity = int(input("Enter Quantity     : "))

total_price = price * quantity
amount_str = str(total_price)

print()
print("-" * 50)
print("TYPE CASTING SUMMARY".center(50))
print("-" * 50)
print(f"{'Variable':<17}{'Value':<17}{'Python Type'}")
print("-" * 50)

rows = [
    ("product_name", product_name),
    ("price", price),
    ("quantity", quantity),
    ("total_price", total_price),
    ("amount_str", amount_str),
]
for var, val in rows:
    print(f"{var:<17}{str(val):<17}{type(val)}")
print("-" * 50)

print()
print("-" * 50)
print("TAX INVOICE".center(50))
print("-" * 50)
print(f"  Product Name   : {product_name}")
print(f"  Price per Unit : Rs. {price:.2f}")
print(f"  Quantity       : {quantity}")
print("  " + "-" * 40)
print(f"  Invoice Total  : Rs. {amount_str}")
print("=" * 50)
