"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def get_spend(self):
        pass


class Coat(Clothes):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @property
    def get_spend(self):
        return self.param/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @property
    def get_spend(self):
        return 2*self.param + 0.3


my_coat = Coat('Моё_пальто', 50)
my_suit = Suit('Мой_костюм', 6)

print(my_suit.get_spend)
#print(my_suit.get_spend)

def Total_spend(Class1, Class2, Qty1, Qty2):
    print(f'Расход ткани на'
          f' [{Qty1} изделий {Class1.name} c параметром {Class1.param} ] +'
          f' [{Qty2} изделий {Class2.name} c параметром {Class2.param} ] ='
          f' {round(Class1.get_spend*Qty1 + Class2.get_spend*Qty2,0)} ед. ткани')

Total_spend(my_coat, my_suit, 5, 7)