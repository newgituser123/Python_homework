"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь."""

class Warehouse:
    def __init__(self, printers, scanners, xeroxes):
        self.printers = printers
        self.scanners = scanners
        self.xeroxes = xeroxes

    def to_warehouse(self, type, qty):
        if type == 'printer':
            self.printers = self.printers + qty
            print(f'Принимаем на склад {qty} принтеров')
        elif type == 'scanner':
            self.scanners = self.scanners + qty
            print(f'Принимаем на склад {qty} сканеров')
        elif type == 'xerox':
            self.xeroxes = self.xeroxes + qty
            print(f'Принимаем на склад {qty} ксероксов')
        else:
            print('Такое на склад мы не примем!')

    def to_dep(self, dep, qty):
        pass

my_wh = Warehouse(10, 8, 21)

print(my_wh.printers, my_wh.scanners, my_wh.xeroxes)

my_wh.to_warehouse('printer', 200)
my_wh.to_warehouse('scanner', 500)
my_wh.to_warehouse('xerox', 1000)

print(my_wh.printers, my_wh.scanners, my_wh.xeroxes)