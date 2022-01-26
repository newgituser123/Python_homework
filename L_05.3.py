#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('income.txt', 'r') as f:
    lines = f.readlines()

d = {}

for line in lines:
    d[line.split()[0]] = int(line.split()[1])

for key, val in d.items():
    if val == max(d.values()):
        print(f'Максимальный оклад {val} у сотрудника {key}')
        break
print(f'Средний оклад составляет: {sum(d.values())/len(d.values())}')