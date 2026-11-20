# Name   : Ujwal Kumar
# Roll No: 2610997675
# Course : BCA (AI & ML) - 1st Semester

with open('q1.txt', 'w') as f:
    f.write('Python makes file handling very simple\nPractice daily to improve')

count = 0
with open('q1.txt', 'r') as f:
    for w in f.read().split():
        if len(w) >= 5:
            count += 1
print('Q1: words with length >= 5 :', count)

with open('q2.txt', 'w') as f:
    f.write('Hello world\nPython is a great language\nShort line\nI like writing code daily\n')

print('Q2:')
with open('q2.txt', 'r') as f:
    for line_no, line in enumerate(f, 1):
        if len(line.split()) > 3:
            print(f'Line {line_no}: {line.strip()}')

with open('q3.txt', 'w') as f:
    f.write('Hello World From BCA AI ML')

upper = 0
lower = 0
with open('q3.txt', 'r') as f:
    text = f.read()
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print('Q3: Uppercase =', upper, ' Lowercase =', lower)

with open('q4.txt', 'w') as f:
    f.write('the cat and the dog and the bird')

freq = {}
with open('q4.txt', 'r') as f:
    for w in f.read().lower().split():
        freq[w] = freq.get(w, 0) + 1

best_word = ''
best_count = 0
for w in freq:
    if freq[w] > best_count:
        best_word = w
        best_count = freq[w]
print('Q4: most frequent word:', best_word, '(', best_count, 'times )')

with open('chat.txt', 'w') as f:
    f.write('my password is 1234\nnever share your password\n')

with open('chat.txt', 'r') as f:
    text = f.read()

text = text.replace('password', '********')

with open('chat.txt', 'w') as f:
    f.write(text)

print('Q5: chat.txt after redacting:')
print(text)

with open('marks.txt', 'w') as f:
    f.write('Aman 85\nRiya 92\nKaran 70\nNeha 60\n')

data = []
total = 0
with open('marks.txt', 'r') as f:
    for line in f:
        name, marks = line.split()
        marks = int(marks)
        data.append((name, marks))
        total += marks

avg = total / len(data)
print('Q6: class average =', avg)
for name, marks in data:
    if marks > avg:
        print('   above average:', name, marks)
