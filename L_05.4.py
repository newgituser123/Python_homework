"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

with open('numbers.txt', 'r') as f:
    lines = f.readlines()

def tr(word):
    if word == 'One':
        return 'Один'
    if word == 'Two':
        return 'Два'
    if word == 'Three':
        return 'Три'
    if word == 'Four':
        return 'Четыре'

m = {}
for line in lines:
    m[tr(line.split()[0])] = line.split()[2]

with open("numbers_translated.txt", "w") as w:
    for key, val in m.items():
        w.write(f'{key} - {val}\n')

