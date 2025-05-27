### Условие задачи:
# Если задано целое число n, верните строку с n такими символами,
# что каждый символ в такой строке встречается нечетное количество раз .
# Возвращаемая строка должна содержать только строчные буквы английского языка.
# Если допустимых строк несколько, верните любую из них.

# Example 1:
# Input: n = 4
# Output: "pppz"
# Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

# Example 2:
# Input: n = 2
# Output: "xy"
# Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".

# Example 3:
# Input: n = 7
# Output: "holasss"

### Краткое условие:
# Возвращаемая строка должна содержать только строчные буквы английского языка.
# Если допустимых строк несколько, верните любую из них.

# Алгоритм решение задачи:
# 0) Если n делется на 2 без остатка, то верни (n-1) умноженая на а + b.
# 1) Если n НЕ делется на 2 без остатка, то верни (n-1) умноженая на а.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

n = 4

def generateTheString(n):
    if n % 2 == 0:
        return (n - 1) * 'a' + 'b'
    else:
        return (n) * "a"

generateTheString(n)

                                ### Тут все автотесты не проходят !!!
# assert generateTheString(n=4) == "pppz"       # "aaab"
# assert generateTheString(n=2) == "xy"         # "ab"
# assert generateTheString(n=7) == "holasss"    # "aaaaaaa"