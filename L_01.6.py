"""6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня."""

def runner(start,target,increase):
    counter = 0
    while target>start:
        start = start*(1+increase)
        counter+=1
    print(f'При темпе роста 10% в день, для достижения цели вам понадобится {counter} дней')

start = int(input('Введите стартовый результат (км): '))
target = int(input('Введите целевой результат (км): '))
increase = 0.1

runner(start,target,increase)