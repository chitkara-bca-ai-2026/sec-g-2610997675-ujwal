# Name   : Ujwal Kumar
# Roll No: 2610997675
# Course : BCA (AI & ML) - 1st Semester

with open('records.txt', 'w') as f:
    f.write('101 Aman 85\n102 Riya 92\n103 Karan 70\n')

total = 0
students = []

with open('records.txt', 'r') as f:
    for line in f:
        if line.strip() == '':
            continue
        parts = line.strip().split()
        roll = parts[0]
        name = parts[1]
        marks = int(parts[2])
        total += marks
        students.append((name, marks))
        print(f'{roll}: {name} scored {marks}')

average = total / len(students)
print('Class Total:', total)
print('Class Average:', round(average, 2))

print('Students scoring above average:')
for name, marks in students:
    if marks > average:
        print(name, marks)
