print("=" * 40)
print("CALENDAR VERIFICATION SYSTEM".center(40))
print("=" * 40)

year = int(input("Enter year: "))

if year <= 0:
    print("Error: year must be a positive integer greater than 0.")
    exit()

if year % 100 == 0:
    if year % 400 == 0:
        leap = True
        reason = "Century year divisible by 400"
    else:
        leap = False
        reason = "Century year not divisible by 400"
elif year % 4 == 0:
    leap = True
    reason = "Divisible by 4 and not a century year"
else:
    leap = False
    reason = "Not divisible by 4"

if leap:
    status = "LEAP YEAR"
    days_in_year = 366
    days_in_feb = 29
else:
    status = "COMMON YEAR"
    days_in_year = 365
    days_in_feb = 28

print()
print("-" * 40)
print("Year:", year)
print("Status:", status)
print("Days in Year:", days_in_year, "days")
print("Days in February:", days_in_feb, "days")
print("Reason:", reason)
print("-" * 40)
