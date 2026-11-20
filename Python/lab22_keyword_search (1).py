# Name   : Ujwal Kumar
# Roll No: 2610997675
# Course : BCA (AI & ML) - 1st Semester

with open('notes.txt', 'w') as f:
    f.write('Python is easy to learn\n')
    f.write('Java and Python are popular\n')
    f.write('Practice coding daily\n')

target = 'python'
total_hits = 0

with open('notes.txt', 'r') as f:
    for line_no, line in enumerate(f, 1):
        words = line.lower().split()
        c = words.count(target.lower())
        if c > 0:
            total_hits += c
            print(f'Line {line_no}: {line.strip()}')

print('Total occurrences:', total_hits)

text = 'Python, python! We learn python.'

for p in '.,!?;:':
    text = text.replace(p, ' ')

words = text.lower().split()
print('Cleaned words:', words)
print('Count of python:', words.count('python'))
