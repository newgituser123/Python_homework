#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('sometext.txt', 'r') as f:
    lines = f.readlines()

print(f'Всего в файле {len(lines)} строк')

for num, line in enumerate(lines, 1):
    print(f'В строке №{num} - {len(line.split())} слов')