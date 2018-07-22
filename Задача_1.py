# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

num_arr = [x for x in range(2, 100)]
counter = 0
div_arr = [0, 0, 0, 0, 0, 0, 0, 0]

for div in range(2, 10):
    for each in num_arr:
        if each % div == 0:
            div_arr[div - 2] += 1

div = 2

for each in div_arr:
    print(f"В диапазоне натуральных чисел от 2 до 99 {each} из них кратны {div}")
    div += 1

