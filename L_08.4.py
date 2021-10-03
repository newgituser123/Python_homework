"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники."""


class Warehouse:
    pass


class Orgtech:
    def __init__(self, color, price, age):
        self.color = color
        self.price = price
        self.age = age


class Printer(Orgtech):
    def __init__(self, color, price, age, size):
        self.color = color
        self.price = price
        self.age = age
        self.size = size


class Scaner(Orgtech):
    def __init__(self, color, price, age, type):
        self.color = color
        self.price = price
        self.age = age
        self.type = type


class Xerox(Orgtech):
    def __init__(self, color, price, age, speed):
        self.color = color
        self.price = price
        self.age = age
        self.speed = speed


my_printer = Printer('black', 500, 12, 50)

print(my_printer.color, my_printer.price, my_printer.age, my_printer.size)