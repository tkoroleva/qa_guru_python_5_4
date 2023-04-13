from math import pi
from random import randint


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f'Привет, {name}! Тебе {age} лет.'
    # Проверяем результат
    print(output)
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # TODO посчитайте периметр
    perimeter = (a + b) * 2
    print(perimeter)
    assert perimeter == 60

    # TODO посчитайте площадь
    area = a * b
    print(area)
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO посчитайте площадь
    area = pi * r ** 2
    print(f'Площадь круга равна: {area}')
    assert area == 1661.9025137490005

    # TODO посчитайте длину окружности
    length = 2 * pi * r
    print(f'Длина окружности равна: {length}')
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10-ти случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    random_list = sorted([randint(1, 100) for _ in range(10)])
    assert len(random_list) == 10
    assert random_list[0] < random_list[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    e = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    e = set(e)
    e = list(e)
    assert isinstance(e, list)
    assert len(e) == 10
    assert e == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))
    dict_length = len(d)
    print(f"Количество значений словаря равно {dict_length}: {str(list(d.values())).replace('[', '').replace(']', '')}")
    assert isinstance(d, dict)
    assert len(d) == 5
