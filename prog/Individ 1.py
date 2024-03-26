#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return ''

def get_sentences_without_commas(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    return [sentence for sentence in sentences if ',' not in sentence]

def main():
    filename = input("Введите имя файла: ")
    text = read_file(filename)
    if text:
        sentences = get_sentences_without_commas(text)
        if sentences:
            print("Предложения без запятых:")
            for sentence in sentences:
                print(sentence)
        else:
            print("В файле нет предложений без запятых.")

if __name__ == "__main__":
    main()
