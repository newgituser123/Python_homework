#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.

mon = int(input('Введите месяц: '))
ss = [
        {'month': 12, 'season': 'winter'},  {'month': 1, 'season': 'winter'},   {'month': 2, 'season': 'winter'},
        {'month': 3, 'season': 'spring'},   {'month': 4, 'season': 'spring'},   {'month': 5, 'season': 'spring'},
        {'month': 6, 'season': 'summer'},   {'month': 7, 'season': 'summer'},   {'month': 8, 'season': 'summer'},
        {'month': 9, 'season': 'fall'},     {'month': 10, 'season': 'fall'},    {'month': 11, 'season': 'fall'}
        ]

for x in range(len(ss)):
    if ss[x]['month']==mon:
        print(ss[x]['season'])