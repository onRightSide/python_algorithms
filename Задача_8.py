# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа
# должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.


matrix = [[], [], [], []]

sum_ = 0

for row in matrix:
    for index in range(4):
        num = int(input("Введите значение элемента матрицы: "))
        sum_ += num
        row.append(num)
    row.append(sum_)
    index = 0
    sum_ = 0

for row in matrix:
    for index in row:
        print(f"{index:3}", end=" ")
    print()

