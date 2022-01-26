"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров."""

DB = []
quant = int(input("Сколько записей добавить в DataBase: "))

for x in range(1,quant+1):
    print(f"Ввод характеристик элемента №{x}")
    x1 = input('Введите название: ')            # компьютер
    x2 = int(input('Введите цену: '))           # 20000
    x3 = int(input('Введите количество: '))     # 5
    x4 = input('Введите единицы измерения: ')   # шт
    print("_"*40)
    record = {"название": x1, "цена": x2, "количество": x3, "ед.изм": x4}
    DB.append(record)

print('"название":',    [ DB[x]["название"] for x in range(quant)]      )
print('"цена":',        [ DB[x]["цена"] for x in range(quant)]          )
print('"количество":',  [ DB[x]["количество"] for x in range(quant)]    )
print('"ед.изм":',      [ DB[x]["ед.изм"] for x in range(quant)]        )