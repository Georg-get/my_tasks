### Условие задачи:
# Вам дана строка, number представляющая положительное целое число, и символ digit.
# Верните результирующую строку после удаления ровно одного вхождения из таким образом digit,
# number чтобы значение результирующей строки в десятичной форме было максимальным.
# Тестовые случаи генерируются таким образом, чтобы digit встречалось по крайней мере один раз в number.

# Example 1:
# Input: number = "123", digit = "3"
# result: "12"
# Explanation: There is only one '3' in "123". After removing '3', the result is "12".

# Example 2:
# Input: number = "1231", digit = "1"
# result: "231"
# Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
# Since 231 > 123, we return "231".

# Example 3:
# Input: number = "551", digit = "5"
# result: "51"
# Explanation: We can remove either the first or second '5' from "551".
# Both result in the string "51".

### Краткое условие:
# Тестовые случаи генерируются таким образом, чтобы digit встречалось по крайней мере один раз в number.

# Полное объяснение решение задачи:
# 0) Создаем пустой массив result.
# 1) Проходимся циклом по индексам строки number,
# 1.1) Если число из строки number равно числу digit, то в массив result добавляем все числа из массива number ????
# 2) Вернуть максимальное число из массива result.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

number = "123"
digit = "3"

def removeDigit(number, digit):
    result = []

    for i in range(len(number)):
        if number[i] == digit:
            result.append(number[:i] + number[i + 1:])

    return max(result)

removeDigit(number, digit)

assert removeDigit(number="123", digit="3") == "12"
assert removeDigit(number="1231", digit="1") == "231"
assert removeDigit(number="551", digit="5") == "51"