"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Data:

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data.split("-")

    def check_data(self):
        if int(self.get_data()[0]) > 0 and int(self.get_data()[0]) < 32:
            if int(self.get_data()[1]) > 0 and int(self.get_data()[1]) < 13:
                if int(self.get_data()[2]) > 0 and int(self.get_data()[2]) < 2050:
                    print('+ Дата введена корректно +')
        else:
            print('- Дата введена некорректно -')

birthday = Data('90-04-1988')

print(birthday.get_data())

birthday.check_data()