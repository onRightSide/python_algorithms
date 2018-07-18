# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько
# между ними находится букв.

letter_dict = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
    "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
}

first_letter = input("Введите первую букву: ")
second_letter = input("Введите вторую букву: ")

first_place = letter_dict.get(first_letter)
print("Позиция первой буквы: {}".format(first_place))
second_place = letter_dict.get(second_letter)
print("Позиция второй буквы: {}".format(second_place))
if first_place <= second_place:
    print("Между введенными буквами {} букв".format(second_place - first_place - 1))
else:
    print("Между введенными буквами {} букв".format(first_place - second_place - 1))