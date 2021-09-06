#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
def timer(start):
    hours = start//3600
    remain1= start-3600*hours
    minutes = remain1//60
    remain2= remain1-60*minutes
    print(f'{hours}:{minutes}:{remain2}')

timer(int(input('Введите время в секундах: ')))