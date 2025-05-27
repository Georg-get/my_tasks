### Условие задачи:
# Учитывая массив строк patterns и строку word, верните количество строк, которые
# patterns существуют в виде подстроки в word.
# Подстрока — это непрерывная последовательность символов внутри строки.

# Example 1:
# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3
# Explanation:
# - "a" appears as a substring in "abc".
# - "abc" appears as a substring in "abc".
# - "bc" appears as a substring in "abc".
# - "d" does not appear as a substring in "abc".
# 3 of the strings in patterns appear as a substring in word.

# Example 2:
# Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
# Output: 2
# Explanation:
# - "a" appears as a substring in "aaaaabbbbb".
# - "b" appears as a substring in "aaaaabbbbb".
# - "c" does not appear as a substring in "aaaaabbbbb".
# 2 of the strings in patterns appear as a substring in word.

# Example 3:
# Input: patterns = ["a","a","a"], word = "ab"
# Output: 3
# Explanation: Each of the patterns appears as a substring in word "ab".

### Краткое условие:
# Вернуть колличестов раз сколько повторяет строка word в словах из массива patterns.

# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 0.
# 1) Проходимся циклом по строке patterns,
# 1.1) Если i есть в строке word, то увеличь значение переменной result на 1.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n*m)
# 2) Память O(1)

patterns = ["a", "abc", "bc", "d"]
word = "abc"

def numOfStrings(patterns, word):
    result = 0

    for i in patterns:
        if i in word:
            result += 1

    return result

numOfStrings(patterns, word)

assert numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc") == 3
assert numOfStrings(patterns=["a", "b", "c"], word="aaaaabbbbb") == 2
assert numOfStrings(patterns=["a", "a", "a"], word="ab") == 3