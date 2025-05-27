### Условие задачи:
# Вам дан массив строк words и строка s, где words[i] и s состоят только из строчных английских букв.
# Возвращает количество строк с words префиксом s.
# Префикс строки — это подстрока, которая находится в начале строки.
# Подстрока — это непрерывная последовательность символов внутри строки.

# Example 1:
# Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
# Output: 3
# Explanation:
# The strings in words which are a prefix of s = "abc" are:
# "a", "ab", and "abc".
# Thus the number of strings in words which are a prefix of s is 3.

# Example 2:
# Input: words = ["a","a"], s = "aa"
# Output: 2
# Explanation:
# Both of the strings are a prefix of s.
# Note that the same string can occur multiple times in words, and it should be counted each time.

### Краткое условие:
# Надо вернуть колличестов сколько раз строка с может быть суфиксом в словах из массива words.

# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 0.
# 1) Проходимся циклом по массиву words,
# 1.1) Если первый символ строки s есть в слове i, то увеличь переменную result на 1.
# 2) Верни переменую result.

# Сложность:
# 1) Время O(n*m)
# 2) Память O(1)

words = ["a", "b", "c", "ab", "bc", "abc"]
s = "abc"

def countPrefixes(words, s):
    result = 0

    for i in words:
        if s[:len(i)] == i:
            result += 1

    return result

countPrefixes(words, s)

assert countPrefixes(words=["a", "b", "c", "ab", "bc", "abc"], s="abc") == 3
assert countPrefixes(words=["a", "a"], s="aa") == 2
assert countPrefixes(
    words=["feh", "w", "w", "lwd", "c", "s", "vk", "zwlv", "n", "w", "sw", "qrd", "w", "w", "mqe", "w", "w", "w", "gb",
           "w", "qy", "xs", "br", "w", "rypg", "wh", "g", "w", "w", "fh", "w", "w", "sccy"], s="w") == 14