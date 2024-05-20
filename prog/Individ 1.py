#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def has_odd_pair(numbers):
    """
    Проверяет наличие хотя бы одной пары соседних нечетных чисел в кортеже.
    Возвращает индексы первой найденной пары, если такая пара существует.
    """
    for i in range(len(numbers) - 1):
        if numbers[i] % 2 != 0 and numbers[i + 1] % 2 != 0:
            return i, i + 1
    return None

def save_to_file(numbers, filename):
    """
    Сохраняет кортеж чисел в файл формата JSON.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(numbers, f)

def load_from_file(filename):
    """
    Загружает кортеж чисел из файла формата JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return tuple(data)

def main():
    """
    Главная функция программы.
    """
    numbers = (1, 2, 3, 5, 6, 8, 7, 9, 10)

    # Сохранение кортежа в файл
    save_to_file(numbers, 'numbers.json')

    # Загрузка кортежа из файла
    loaded_numbers = load_from_file('numbers.json')

    # Проверка наличия пары нечетных чисел
    result = has_odd_pair(loaded_numbers)

    if result:
        print(f"Первая пара соседних нечетных чисел найдена на позициях: {result[0]} и {result[1]}")
    else:
        print("Пара соседних нечетных чисел не найдена")

    if __name__ == "__main__":
        main()