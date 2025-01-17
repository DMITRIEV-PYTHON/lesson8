# Домашнее задание по уроку "Try и Except".
# Задание "Программистам всё можно":
# Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем сложить число(int)
# и строку(str)? Давайте исправим это недоразумение!
# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление
# этих двух данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.

def add_everything_up(a, b):
    resault = 0
    try:
        resault = (a + b)
        return resault
    except TypeError:
        if type(a) == int or type(a) == float and type(b) == str:  # a - число, b - строка
            resault = str(a) + b
        elif type(a) == str and type(b) == int or type(b) == float:  # a - строка, b - число
            resault = a + str(b)
    return resault


print(add_everything_up(123.456, "строка"))

print(add_everything_up("яблоко", 4215))

print(add_everything_up(123.456, 7))

print(add_everything_up("яблоко", "строка"))
