# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования
# треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли
# он разносторонним, равнобедренным или равносторонним.

first_side = float(input("Введите длину первой стороны: "))
second_side = float(input("Введите длину второй стороны: "))
third_side = float(input("Введите длину третьей стороны: "))

if first_side < second_side:
    m = first_side
    first_side = second_side
    second_side = m

if second_side < third_side:
    if first_side < third_side:
        m = first_side
        first_side = third_side
        third_side = m

        m = second_side
        second_side = third_side
        third_side = m

    else:
        m = second_side
        second_side = third_side
        third_side = m

print(first_side, second_side, third_side)


if (first_side >= third_side) and (first_side < second_side + third_side):
    print("Треугольник существует")
    if first_side == second_side == third_side:
        print("Треугольник равносторнний")
    elif first_side == second_side or first_side == third_side or second_side == third_side:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")

