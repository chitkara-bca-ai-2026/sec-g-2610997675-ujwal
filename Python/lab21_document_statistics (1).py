# Name   : Ujwal Kumar
# Roll No: 2610997675
# Course : BCA (AI & ML) - 1st Semester

with open('article.txt', 'w') as f:
    f.write('Python is popular.\n')
    f.write('It is used in AI and ML.\n')

lines = 0
words = 0
chars = 0

with open('article.txt', 'r') as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line.strip())

print('Total Lines :', lines)
print('Total Words :', words)
print('Total Chars :', chars)

with open('data.txt', 'w') as f:
    f.write('BCA Batch 2026')

vowels = 0
consonants = 0
digits = 0

with open('data.txt', 'r') as f:
    text = f.read()

for ch in text:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1

print(f'Vowels:{vowels} Cons:{consonants} Digits:{digits}')
