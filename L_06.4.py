"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed}')
        if self.speed > 60:
            print(f'Скорость превышена!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed}')
        if self.speed > 40:
            print(f'Скорость превышена!')


class PoliceCar(Car):
    pass


TownGuy = TownCar(50, 'Green', 'TownGuy', False)
Speedster = SportCar(250, 'Red', 'Speedster', False)
Digger = WorkCar(100, 'Black', 'Digger', False)
Sheriff = PoliceCar(200, 'Blue', 'Sheriff', True)

print(f'Скорость {TownGuy.name} равна {TownGuy.speed}')
print(f'Цвет {Speedster.name} - {Speedster.color}')
print(f'Является ли {Sheriff.name} полицейской машиной - {Sheriff.is_police}')

print("_"*20)
Speedster.go()
Digger.stop()
Sheriff.turn('направо')

print("_"*20)
for car in [TownGuy, Speedster, Digger, Sheriff]:
    car.show_speed()
