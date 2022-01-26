#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    lst = [*args]
    for i in range(len(lst)):
        if lst[i] == max(lst):
            m1 = lst.pop(i)
            break
    return m1+max(lst)

print(my_func(9,1,2,-8,3,5))