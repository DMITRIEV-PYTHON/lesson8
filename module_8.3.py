# Задача "Некорректность":
# Создайте 3 класса (2 из которых будут исключениями):
# Класс Car должен обладать следующими свойствами:
# Атрибут объекта model - название автомобиля (строка).
# Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
# Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
# Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# Атрибут __numbers - номера автомобиля (строка).
# Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True,
# если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают (атрибутом
# (message - сообщение,)) которое будет выводиться при выбрасывании исключения.

class Car:
    def __init__(self, model: str, __vin: int, __numbers: str):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.__vin = __vin
        if self.__is_valid_numbers(__numbers):
            self.__numbers = __numbers

    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип VIN номера (передано не целое число)")
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber("Неверный диапазон для VIN номера")
        return True

    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номера автомобиля (передана не строка.")
        if not len(numbers) == 6:
            raise IncorrectCarNumbers("Неверная длина номера автомобиля (в строке должно быть ровно 6 символов).")
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:

    first = Car('Model1', 1000000, 'f123dj')

except IncorrectVinNumber as exc:

    print(exc.message)

except IncorrectCarNumbers as exc:

    print(exc.message)

else:

    print(f'{first.model} успешно создан')

try:

    second = Car('Model2', 300, 'т001тр')

except IncorrectVinNumber as exc:

    print(exc.message)

except IncorrectCarNumbers as exc:

    print(exc.message)

else:

    print(f'{second.model} успешно создан')

try:

    third = Car('Model3', 2020202, 'нет номера')

except IncorrectVinNumber as exc:

    print(exc.message)

except IncorrectCarNumbers as exc:

    print(exc.message)

else:

    print(f'{third.model} успешно создан')
