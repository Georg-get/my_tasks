### Условие задачи:
# Для двух строк sи tмы говорим «t делится s» тогда и только тогда, когда s = t + t + t + ... + t + t
# (т.е. t конкатенируется сама с собой один или более раз).
# Для двух строк str1 и str2 вернуть наибольшую строку, x которая x делит str1 и str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

### Краткое условие:
# Для двух строк str1 и str2 вернуть наибольшую строку, x которая x делит str1 и str2.

# Полное объяснение решение задачи:
# 0) Создаем функцию gcd,
# 0.1) Проходим циклом вайл пока строка str2 не станет пустой,
# 0.1.1) Переменная temp равна str2 и str2 равна str1 % str2 и str1 равна temp, вернуть str1.
# 2) Если str1 + str2 равно str2 + str1,
# 2.1) Вернуть результат фунцкии gcd с параметрами длины строки str1 и str2.
# 3) Иначе, вернуть пустую строку.

# Сложность:
# 1) Время O(n + m)
# 2) Память O(1)

str1 = "ABCABC"
str2 = "ABC"

def gcdOfStrings(str1, str2):

    def gcd(str1, str2):

        while str2:
            temp = str2
            str2 = str1 % str2
            str1 = temp

        return str1

    if str1 + str2 == str2 + str1:
        return str1[:gcd(len(str1), len(str2))]
    else:
        return ""

gcdOfStrings(str1, str2)

assert gcdOfStrings(str1="ABCABC", str2="ABC") == "ABC"
assert gcdOfStrings(str1="ABABAB", str2="ABAB") == "AB"
assert gcdOfStrings(str1="LEET", str2="CODE") == ""

# from math import gcd
#
# str1 = "ABCABC"
# str2 = "ABC"
#
# def gcdOfStrings(str1, str2):
#     if str1 + str2 != str2 + str1:
#         return ""
#
#     return str1[:gcd(len(str1), len(str2))]
