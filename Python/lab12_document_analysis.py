sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

letters = vowels + consonants
if letters > 0:
    vowel_percentage = (vowels / letters) * 100
else:
    vowel_percentage = 0.0

print("=" * 44)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 44)
print("Sentence:", sentence)
print("Total characters:", len(sentence))

print()
print("--- Character Breakdown ---")
print(f"{'Words:':<20}{words}")
print(f"{'Vowels:':<20}{vowels}")
print(f"{'Consonants:':<20}{consonants}")
print(f"{'Digits:':<20}{digits}")
print(f"{'Spaces:':<20}{spaces}")
print(f"{'Special characters:':<20}{special}")

print()
print("--- Summary ---")
print("Total letters:", letters)
print(f"Vowel percentage: {round(vowel_percentage, 1)}%")

print()
print("=" * 44)
print("Analysis Complete!")
print("=" * 44)
