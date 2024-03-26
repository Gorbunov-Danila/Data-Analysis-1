#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

def count_letter_frequency(file_name):
    # Словарь для хранения частоты появления каждой буквы
    letter_frequency = {}

    try:
        with open(file_name, 'r') as file:
            # Чтение файла и обработка каждой строки
            for line in file:
                # Приведение к нижнему регистру и удаление пробелов
                line = line.lower().strip()
                # Удаление знаков препинания и цифр
                line = ''.join(char for char in line if char.isalpha())

                # Обновление частоты появления каждой буквы
                for char in line:
                    letter_frequency[char] = letter_frequency.get(char, 0) + 1

    except FileNotFoundError:
        print("Ошибка: Файл '{}' не найден.".format(file_name))
        return None

    return letter_frequency

def print_letter_frequency(letter_frequency):
    if letter_frequency is None:
        return

    # Сортировка словаря по частоте появления букв
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

    # Вывод частоты появления букв на экран
    print("Частота появления букв:")
    for letter, frequency in sorted_frequency:
        print("{}: {}".format(letter, frequency))

if __name__ == "__main__":
    file_name = "1.txt"  # Указываем имя файла "1"
    letter_frequency = count_letter_frequency(file_name)
    if letter_frequency:
        print_letter_frequency(letter_frequency)


