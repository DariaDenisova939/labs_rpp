import csv
from operator import itemgetter
from pathlib import Path
import os


def search_directory():  # функция нужна для поиска кол-ва файлов в папке и переходу к основной части кода
    operation_num = input(
        "0 - подсчитать количество файлов в дериктории" + "\n" + "1 - перейти к следущему шагу" + "\n")
    if operation_num == "0":
        directory = input("Path:" + "\n")  # принимаем путь директории для поиска
        files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]  # ищем файлы
        print("Файлов в папке: " + str(len(files)))
        operation_num = "1"
    if operation_num == "1":
        main()
    else:
        print("Операция введена неверно")


def main():  # функция содержащая главную часть кода
    f = open('inputlab3.csv', 'r', encoding='utf-8')
    reader = csv.DictReader(f, delimiter=',', quotechar='"')
    operation_sort = input(
        "0 - сортировать по сумме" + "\n" + "1 - сортировать по описанию транзакции" + "\n" + "2 - найти по номеру" + "\n")
    if operation_sort == "0":
        result_sort = amount_sort(reader)  # вызываем сортировку по сумме перервода в порядке убывания
    elif operation_sort == "1":
        result_sort = transaction_description_sort(
            reader)  # вызываем сортировку по описанию транзакции в порядке убывания
    elif operation_sort == "2":
        number = input("Введите номер:" + "\n")
        result_sort = search_number(reader, number)  # вызываем функцию для поиска по номеру перевода
    else:
        operation_sort = False
        print("Вы неверно ввели номер операции")
    if operation_sort:
        operation_write = input("0 - не записывать результат" + "\n" + "1 - записать результат обратно в файл" + "\n")
        if operation_write == "1":
            writer(result_sort)  # передаем в получаенные данные в функцию для записи обратно в файл
            print("Запись прошла успешно")


def writer(sort):
    f = open('inputlab3.csv', 'w', encoding='utf-8', newline='\n')
    writer_res = csv.writer(f)
    for i in range(len(sort)):  # заходим в цикл для записи результата в файл
        if i == 0:
            writer_res.writerow(sort[i])  # записываем в файл названия стобцов
        writer_res.writerow(
            [sort[i]['number']] + [sort[i]['date']] + [sort[i]['time']] + [sort[i]['transfer amount']] + [
                sort[i]['transaction description']])  # записываем в файл данные таблицы


def amount_sort(d):
    sort = sorted(d, key=lambda f: int(f['transfer amount']), reverse=True)  # сортируем данные файла
    for row in sort:
        print(row)
    return sort


def transaction_description_sort(d):
    sort = sorted(d, key=lambda f: str(f['transaction description']))  # сортируем данные файла
    for row in sort:
        print(row)
    return sort


def search_number(d, num):  # функция для поиска перевода по номеру
    res = []
    for row in d:
        if row['number'] == num:  # проверяем равен ли i-тый номер нужному
            res.append(row)  # добавляем в список строчку из таблицы с нужным номером
            print(row)
    return res


search_directory()  # вызываем функцию для поиска кол-ва файлов в папке
