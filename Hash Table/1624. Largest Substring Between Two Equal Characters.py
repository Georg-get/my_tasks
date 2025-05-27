### Условие задачи:
# Учитывая строку s, верните длину самой длинной подстроки между двумя одинаковыми символами, исключая эти два символа.
# Если такой подстроки нет, return -1.
# Подстрока — это непрерывная последовательность символов внутри строки.

# Example 1:
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.

# Example 2:
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".

# Example 3:
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.

### Краткое условие:
# Учитывая строку s, верните длину самой длинной подстроки между двумя одинаковыми символами, исключая эти два символа.
# Если такой подстроки нет, return -1

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result со значением -1.
# 1) Проходимся циклом по диапазону длинны строки s,
# 1.1) Если ключ i есть в словаре dict, то обновляем переменную result,
# присваивая ей максимальное значение между текущим значением result и результатом i - dict[s[i]] - 1. .
# 1.2) Если i НЕТу в словаре dict, то добавить i как ключ со значением i в словарь dict.
# 2) Вернуть переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "abca"

def maxLengthBetweenEqualCharacters(s):
    dict = {}
    result = -1

    for i in range(len(s)):
        if s[i] in dict:
            result = max(result, i - dict[s[i]] - 1)
        else:
            dict[s[i]] = i
    # {'a': 0, 'b': 1, 'c': 2}
    return result # 2

maxLengthBetweenEqualCharacters(s)

assert maxLengthBetweenEqualCharacters(s="aa") == 0
assert maxLengthBetweenEqualCharacters(s="abca") == 2
assert maxLengthBetweenEqualCharacters(s="cbzxy") == -1