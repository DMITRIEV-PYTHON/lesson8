# Задача "План перехват":
# Напишите 2 функции:
# Функция personal_sum(numbers):
# Должна принимать коллекцию numbers.
# Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
# Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError,
# увеличив счётчик incorrect_data на 1.
# В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во
# некорректных данных.
# Функция calculate_average(numbers)
# Среднее арифметическое - сумма всех данных делённая на их количество.
# Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
# Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
# Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0
# и верните 0.
# Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение
# TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.

def personal_sum(numbers):
    result = 0  # сумма чисел колекции numbers
    incorrect_data = 0  # счетчик некорректных данных
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1  # несоответствие типов данных
            print(f'Присутствует некорректный тип данных для подсчёта суммы - "{number}" - {type(number).__name__}')
    return result, incorrect_data


def calculate_average(numbers):
    average = 0  # результат выполнения функции
    try:
        numbers_size = len(numbers)  # Коллекция позволяет определить размер
        result, incorrect_data = personal_sum(numbers)  # функция personal_sum возвращает кортеж из двух значений
        average = result / (numbers_size - incorrect_data)  # Вычислим среднее арифметическое всех чисел
    except ZeroDivisionError:
        print(f'В коллекции отсутствуют данные для вычислений')
        average = 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных "{numbers}" - {type(numbers).__name__}'
              f' (не является коллекцией)')
        average = None
    finally:
        return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3

print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция

print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
