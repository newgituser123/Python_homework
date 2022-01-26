#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
#При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class Zerodivide:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def divide(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return "Деление на ноль прошло успешно"


x = Zerodivide(100, 0)

print(x.divide)