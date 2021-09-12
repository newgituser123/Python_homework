#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.
#print('incorrect input')
season = ['winter','spring','summer','fall','winter']
try:
    month = int(input('Введите номер месяца (от 1 до 12): '))
except ValueError:
    print('incorrect input #1')
    exit()

if month<1 or month>12 :
    print('incorrect input #2')
else:
    print(season[month//3]) # подсмотрел в твоём видео: Простое и красивое решение!


