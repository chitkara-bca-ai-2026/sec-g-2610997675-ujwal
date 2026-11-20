tuition = float(input("Enter Tuition Fee: "))
lab = float(input("Enter Lab Fee: "))
library = float(input("Enter Library Fee: "))
exam = float(input("Enter Exam Fee: "))
discount = float(input("Enter Discount Amount: "))

total_fee = tuition + lab + library + exam
fee_after_discount = total_fee - discount
annual_fee = fee_after_discount * 2
monthly = annual_fee / 12

print()
print("Tuition Fee:", tuition)
print("Lab Fee:", lab)
print("Library Fee:", library)
print("Exam Fee:", exam)
print("Total Fee:", total_fee)
print("Discount:", discount)
print("Fee after Discount:", fee_after_discount)
print("Annual Fee:", annual_fee)
print("Monthly Installment:", round(monthly, 2))
