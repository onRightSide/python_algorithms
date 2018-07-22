# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


from random import random


ROW_N = 2
COL_N = 6


matrix = []

for col in range(COL_N):
    matrix.append([])
    for row in range(ROW_N):
        matrix[col].append(int(random() * 100))

min_arr = []
index = 0

for index in range(ROW_N):
    for col in matrix:
        print(f"{col[index]:3}", end=" ")
    print()

for col in matrix:
    min_num = col[0]
    for index in col:
        if min_num > index:
            min_num = index
    min_arr.append(min_num)

for i in range(COL_N):
    print("----", end="")
print()

print(f"{max(min_arr):3}")
