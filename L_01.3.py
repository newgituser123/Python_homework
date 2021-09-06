#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
num = 99
while True:
    num = input('Введите число от 1 до 9: ')
    if int(num)<1 or int(num)>9:
        print('Не корректное число! Попробуйте снова.')
    else:
        break

quant = 99
while True:
    quant = input('Сколько раз его повторить от 1 до 9?: ')
    if int(quant)<1 or int(quant)>9:
        print('Не корректное число! Попробуйте снова.')
    else:
        break

expr= []

print(num, end = "")
for i in range(2,int(quant)+1):
    print(f' + {num * i}', end = "")
    expr.append(int(num*i))

print(f' = {sum(expr)}')