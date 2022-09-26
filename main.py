# Вариант 10, ограничение: От 2018 года

import csv

# Task 1: подсчитать количество записей.
rowcount = 0
for row in open("books.csv"):
    rowcount += 1
print('Kоличество записей:', rowcount)


# Task 2: Количество записей, у которых название длинее 30 символов.
row_1 = 0
with open('books.csv', newline = '') as f:
    reader = csv.DictReader(f, delimiter = ';')
    for row in reader:
        if len(row['Название']) > 30:
            row_1 += 1
    print('Количество записей, у которых название длинне 30 символов:', row_1)


# Task 3: Поиск книги по автору
search = input('Search for: ')
file = open('result.txt', 'w')
with open('books.csv', 'r', encoding = 'cp1251') as f:
    flag = 0
    table = csv.reader(f, delimiter = ';')
    for row in table:
        rowToLower = row[3].lower()
        index = rowToLower.find(search.lower())
        if (index != -1) and (int(row[6][:4]) >= 2018):
            print(int(row[6][:4]))
            flag = 1
            print('Название книги: ', row[1])
            file.write('Название: ' + row[1] + ' Артикул: ' + row[0] + '\n')
    if flag == 0:
        print('Ничего не нашли')
file.close()


# Task 4: Генератор ссылок
from random import randint
with open('books.csv', newline = '') as f:
    reader = csv.reader(f, delimiter = ';')
    numbers = []
    for i in range(20):
        numbers.append(randint(1, 9410))
    reader_list = list(reader)
    for i in numbers:
        row = reader_list[i]
        print(row[3], '.', row[1], '-', row[6][:4])

