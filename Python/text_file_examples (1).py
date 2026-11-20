# Name   : Ujwal Kumar
# Roll No: 2610997675
# Course : BCA (AI & ML) - 1st Semester

with open('sample.txt', 'w') as f:
    f.write(' Hello Python World \n')
    f.write(' File handling is easy\n')

with open('sample.txt', 'r') as f:
    for line in f:
        clean = line.strip()
        words = clean.split()
        print(clean, '->', len(words), 'words')

with open('words.txt', 'w') as f:
    f.write('Programming in Python builds logical thinking')

with open('words.txt', 'r') as f:
    word_list = f.read().split()

longest = ''
for w in word_list:
    if len(w) > len(longest):
        longest = w

print('Longest word:', longest)
print('Length      :', len(longest))

with open('poem.txt', 'w') as f:
    f.write('code learn code build learn code')

freq = {}
with open('poem.txt', 'r') as f:
    words = f.read().lower().split()

for w in words:
    freq[w] = freq.get(w, 0) + 1

for word in sorted(freq.keys()):
    print(f'{word}: {freq[word]}')

with open('course.txt', 'w') as f:
    f.write('Java is easy.\nWe love Java!')

with open('course.txt', 'r') as f:
    content = f.read()

updated = content.replace('Java', 'Python')

with open('course.txt', 'w') as f:
    f.write(updated)

print(updated)

with open('server.log', 'w') as f:
    f.write('INFO: Server started\n')
    f.write('ERROR: Disk full\n')
    f.write('INFO: User connected\n')
    f.write('ERROR: Timeout occurred\n')

err_count = 0
with open('server.log', 'r') as f:
    for line in f:
        if 'ERROR' in line:
            print(line.strip())
            err_count += 1

print('Total Errors:', err_count)
