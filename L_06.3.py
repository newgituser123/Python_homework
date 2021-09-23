"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""

incoms = [{'position': "бухгалтер", "wage": 100, "bonus": 15},
          {'position': "менеджер", "wage": 500, "bonus": 200}]


class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def get_total_income(self):
        for i in range(len(incoms)):
            if incoms[i]['position'] == self.position:
                print(f"Доход сотрудника: {incoms[i]['wage'] + incoms[i]['bonus']}")


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)


manager = Position("Владимир", "Ленин", "менеджер")
account = Position("Василиса", "Прекрасная", "бухгалтер")

manager.get_full_name()
manager.get_total_income()
print("_"*20)
account.get_full_name()
account.get_total_income()
