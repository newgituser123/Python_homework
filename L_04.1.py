"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

accountant = {'worked_hours': 40*21, 'pay_for_hour': 1000, 'bonus': 50000}
manager = {'worked_hours': 60*21, 'pay_for_hour': 2000, 'bonus': 150000}


def salary(worked_hours, pay_for_hour, bonus):
    return worked_hours * pay_for_hour + bonus


print(f'accountant: {salary(**accountant)},\nmanager: {salary(**manager)}')