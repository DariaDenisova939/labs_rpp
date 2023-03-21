from random import randint


def input_validation(tmp_list):  # функция необходима для проверки корректности ввода списков
    flag = True
    for j in range(len(tmp_list)):
        if not tmp_list[j].isdigit():  # проверяем, является ли элемент списка числом
            flag = False
            break
    if not flag:
        print("Список введён некорректно")


def my_count(tmp_list, tmp_x):  # функция нужна для определения количества вхождений определнного элемента в список
    count = 0
    for j in range(len(tmp_list)):
        if tmp_list[j] == tmp_x:
            count += 1  # подсчитываем количество вхождений переданного элемента в список
    return count


def my_remove(tmp_list, tmp_x):  # функция нужна для удаления элемента из списка
    res_list = []
    for j in range(len(tmp_list)):
        if tmp_list[j] != tmp_x:
            res_list.append(tmp_list[j])  # добавляем в новый список все элементы, не равные переданному элементу
    return res_list


def result_without_func(tmp_list_A,
                        tmp_list_B):  # функция нужна для решения поставленной задачи без использования стандартных функций
    i = 0
    while i < len(tmp_list_A):
        x = tmp_list_A[i]
        if my_count(tmp_list_A, x) >= 2 and my_count(tmp_list_B,
                                                     x) >= 2:  # проверяем встречается ли элемент в списке хотябы 2 раза
            i -= 1  # так как, удалив элемент под i-тым индексом, на следующей итеррации пропустим элемент под индексом i + 1
            tmp_list_A = my_remove(tmp_list_A, x)  # удаляем из списка все элементы, имеющие значение x
        i += 1
    print("Результат:" + "\n" + ' '.join(tmp_list_A))


def result(tmp_list_A,
           tmp_list_B):  # функция нужна для решения поставленной задачи c использованием стандартных функций
    i = 0
    while i < len(tmp_list_A):
        x = tmp_list_A[i]
        if tmp_list_A.count(x) >= 2 and tmp_list_B.count(
                x) >= 2:  # проверяем встречается ли элемент в списке хотябы 2 раза
            i -= 1  # так как, удалив элемент под i-тым индексом, на следующей итеррации пропустим элемент под индексом i + 1
            while tmp_list_A.count(x) != 0:  # удаляем из списка все элементы, имеющие значение x
                tmp_list_A.remove(x)
        i += 1
    print("Результат:" + "\n" + ' '.join(tmp_list_A))


def do_manual_input():
    print("Введите список А:")
    listA = input().split()
    input_validation(listA)  # вызываем функцию для проверки корректности ввода
    print("Введите список B:")
    listB = input().split()
    input_validation(listB)  # вызываем функцию для проверки корректности ввода
    print("0 - не использовать стандартные функции" + "\n" + "1 - использовать стандартные функции")
    func_op = input()
    if func_op == "0":
        result_without_func(listA, listB)
    elif func_op == "1":
        result(listA, listB)
    else:
        print("Номер введен некорректно")


def do_auto_gen():
    list_gen_A = [str(randint(0, 10)) for i in range(20)]
    list_gen_B = [str(randint(0, 10)) for i in range(20)]
    print("Сгенерированный список A: " + "\n" + ' '.join(list_gen_A))
    print("Сгенерированный список B: " + "\n" + ' '.join(list_gen_B))
    print("0 - не использовать стандартные функции" + "\n" + "1 - использовать стандартные функции")
    func_op = input()
    if func_op == "0":
        result_without_func(list_gen_A,
                            list_gen_B)  # вызываем функцию для решения задачи без использования стандартных функций
    elif func_op == "1":
        result(list_gen_A, list_gen_B)  # вызываем функцию для решения задачи с использованием стандартных функций
    else:
        print("Номер введен некорректно")


flag_operation = input("0 - ввести свои списки" + "\n" + "1 - использовать автоматическую генерацию" + "\n")
if flag_operation == "0":
    do_manual_input()
elif flag_operation == "1":
    do_auto_gen()
else:
    print("Номер введен некорректно")
