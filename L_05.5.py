#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("several_nums.txt", "w") as n:
    n.write('1 2 3 4 5 6 7 8 9 10')
    n.flush()

with open('several_nums.txt', 'r') as c:
    text = c.read()

print(sum([int(x) for x in text.split()]))
