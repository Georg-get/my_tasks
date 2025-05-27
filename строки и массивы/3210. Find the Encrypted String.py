### Условие задачи:
# Вам дана строка sи целое число k. Зашифруйте строку, используя следующий алгоритм:
# Замените каждый символ c в на символ s, следующий за ним в строке (циклическим образом). c k th c
# Верните зашифрованную строку.

# Example 1:
# Input: s = "dart", k = 3
# Output: "tdar"
# Explanation:
# For i = 0, the 3rd character after 'd' is 't'.
# For i = 1, the 3rd character after 'a' is 'd'.
# For i = 2, the 3rd character after 'r' is 'a'.
# For i = 3, the 3rd character after 't' is 'r'.

# Example 2:
# Input: s = "aaa", k = 1
# Output: "aaa"
# Explanation:
# As all the characters are the same, the encrypted string will also be the same.

### Краткое условие:
# Верните зашифрованную строку.


# Полное объяснение решение задачи:
# 0) Создаем пустой массив result.
# 1) Проходимся циклом по индексам строки s,
# 1.1) Увеличиваем массив result на (i + k) % len(s).
# 2) Преобразовываем массив result в строку.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "dart"
k = 3

def getEncryptedString(s, k):
    result = []

    for i in range(len(s)):             # ['t']
        result += s[(i + k) % len(s)]   # ['t', 'd']
                                        # ['t', 'd', 'a']
                                        # ['t', 'd', 'a', 'r']
    # ['t', 'd', 'a', 'r']
    return "".join(result) # tdar

getEncryptedString(s, k)

assert getEncryptedString(s="dart", k=3) == "tdar"
assert getEncryptedString(s="aaa", k=1) == "aaa"