import csv
import os


class FileUtil:
    read = {}
    result = []

    def __init__(self, file_name):  # конструктор класса
        self.file_name = file_name

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def writer(self, result):
        f = open(self.file_name, 'w', encoding='utf-8', newline='\n')
        writer_res = csv.writer(f)
        for i in range(len(result)):  # заходим в цикл для записи результата в файл
            if i == 0:
                writer_res.writerow(result[i])  # записываем в файл названия стобцов
            writer_res.writerow(
                [result[i]['number']] + [result[i]['date']] + [result[i]['time']] + [result[i]['transfer amount']] + [
                    result[i]['transaction description']])  # записываем в файл данные таблицы

    def reader(self, delim, quot):
        f = open(self.file_name, 'r', encoding='utf-8')
        self.read = csv.DictReader(f, delimiter=delim, quotechar=quot)

    @staticmethod
    def search_directory(direct):  # метод нужен для поиска кол-ва файлов в папке и переходу к основной части кода
        files = [file for file in os.listdir(direct) if os.path.isfile(f'{direct}/{file}')]  # ищем файлы
        return str(len(files))


class DataOperations:
    sort_result = []

    def __init__(self, read_result):  # конструктор класса
        self.read_result = read_result

    def __getitem__(self, key):
        return self.sort_result[key]

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def transaction_description_sort(self):
        self.sort_result = sorted(self.read_result,
                                  key=lambda f: str(f['transaction description']))  # сортируем данные файла

    def amount_sort(self):
        self.sort_result = sorted(self.read_result, key=lambda f: int(f['transfer amount']),
                                  reverse=True)  # сортируем данные файла

    def search_number(self, num):  # метод для поиска перевода по номеру
        for row in self.read_result:
            if row['number'] == num:  # проверяем равен ли i-тый номер нужному
                self.sort_result.append(row)  # добавляем в список строчку из таблицы с нужным номером


class DataOperationsOutput(DataOperations):
    p = 0

    def __iter__(self):
        return self

    def __getitem__(self, item):
        if 0 <= item < len(self.sort_result):
            return self.sort_result[item]
        else:
            raise IndexError("Неверный индекс")

    def __next__(self):
        if self.p >= len(self.sort_result):  # проверяем на выход за границы списка
            self.p = 0
            raise StopIteration
        else:
            tmp = self.sort_result[self.p]  # кладем в tmp элемент списка а затем возвращаем
            self.p += 1
            return tmp

    def generator(self):
        self.p = 0
        while self.p < len(self.sort_result):
            yield self.sort_result[self.p]
            self.p += 1


def output():
    print('Итератор: ' + "\n")
    for item in iter(objOperat):
        print(item)
    print('\nГенератор:' + "\n")
    for item in objOperat.generator():
        print(item)


obj = FileUtil('inputlab3.csv')
obj.reader(',', '"')
objOperat = DataOperationsOutput(obj.read)
operation_num = input(
    "0 - подсчитать количество файлов в дериктории" + "\n" + "1 - перейти к следущему шагу" + "\n")
if operation_num == "0":
    directory = input("Path:" + "\n")
    print("Файлов в папке: " + obj.search_directory(directory))
    operation_num = "1"
if operation_num == "1":
    operation_sort = input(
        "0 - сортировать по сумме" + "\n" + "1 - сортировать по описанию транзакции" + "\n" + "2 - найти по номеру" + "\n")
    if operation_sort == "0":
        objOperat.amount_sort()  # вызываем сортировку по сумме перервода в порядке убывания
        output()
    elif operation_sort == "1":
        objOperat.transaction_description_sort()  # вызываем сортировку по описанию транзакции в порядке убывания
        output()
    elif operation_sort == "2":
        number = input("Введите номер:" + "\n")
        objOperat.search_number(number)  # вызываем метод для поиска по номеру перевода
        output()
    else:
        operation_sort = False
        print("Вы неверно ввели номер операции")
    if operation_sort:
        operation_write = input("0 - не записывать результат" + "\n" + "1 - записать результат обратно в файл" + "\n")
        if operation_write == "1":
            obj.writer(objOperat.sort_result)  # передаем в получаенные данные в метод для записи обратно в файл
            print("Запись прошла успешно")
else:
    print("Операция введена неверно")
