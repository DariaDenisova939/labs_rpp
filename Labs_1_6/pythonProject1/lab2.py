import numpy as np

m = np.random.randint(1, 15)  # генерируем количество столбцов
n = np.random.randint(1, 15)  # генерируем количество строк
arr = np.array([[np.random.randint(1, 10) for j in range(m)] for i in range(n)])  # генерируем матрицу(массив)
res = np.amin(np.mean(arr, axis=1))  # получаем массив из средних значений и находим минимальное
file = open("output.txt", "w")  # создаем и открываем файл на запись
file.write(
    "N: " + str(n) + " M: " + str(m) + "\n" + "Matrix: "+ "\n" + np.array2string(arr) + "\n" + "Result: " + "\n" + str(
        res))  # выводим результат и исходные данные в файл
file.close()  # закрываем файл
print("Программа завершила свою работу")