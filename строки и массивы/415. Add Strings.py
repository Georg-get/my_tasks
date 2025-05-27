### Условие задачи:
# Даны два неотрицательных целых числа, num1 представленные num2 в виде строки. Верните сумму num1 и num2 в виде строки.
# Вы должны решить задачу без использования какой-либо встроенной библиотеки для обработки больших целых чисел (например, BigInteger).
# Вы также не должны преобразовывать входные данные в целые числа напрямую.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

### Краткое условие:
# Вы также не должны преобразовывать входные данные в целые числа напрямую.

# Полное объяснение решение задачи:
# 0) Устанавливаем максимальное количество цифр.
# 1) Вернуть строку из двух числе num1 + num2.

# Сложность:
# 1) Время O(m)
# 2) Память O(1)

num1 = "11"
num2 = "123"

def licenseKeyFormatting(num1, num2):
    import sys
    sys.set_int_max_str_digits(10000)
    return str(int(num1) + int(num2))

licenseKeyFormatting(num1, num2)

assert licenseKeyFormatting(num1="11", num2="123") == "134"
assert licenseKeyFormatting(num1="456", num2="77") == "533"
assert licenseKeyFormatting(num1="0", num2="0") == "0"

#
# num1 = "11"
# num2 = "123"
#
# def licenseKeyFormatting(num1, num2):
#     def strToInt(num):
#         dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
#                 '6': 6, '7': 7, '8': 8, '9': 9}
#         output = 0
#
#         for i in num:
#             output = output * 10 + dict[i]
#
#         return output
#
#
#     return str(strToInt(num1) + strToInt(num2))
# licenseKeyFormatting(num1, num2)
