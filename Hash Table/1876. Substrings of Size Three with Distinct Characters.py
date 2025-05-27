### Условие задачи:
# Строка хороша, если в ней нет повторяющихся символов.
# Учитывая строку s, верните количество хороших подстрок длиной три в s.
# Обратите внимание: если одна и та же подстрока встречается несколько раз, каждое вхождение должно учитываться.
# Подстрока — это непрерывная последовательность символов в строке.

# Example 1:
# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
# The only good substring of length 3 is "xyz".

# Example 2:
# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".

                                            ### Добавить в список !

### Краткое условие:
# Вернуть число уникальных подстрок (без повторяющеся букв в подстроке).

# Алгоритм решение задачи:
# 0) Создаем переменные l =0 и result = 0, пустой словарь dict.
# 1) Проходимся циклом по диапазону строки s,
# 1.1) Если i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Если i НЕТу в словаре dict, то добавь ключ i со значением 1.
# 1.3) Если i - l +1=3,
# 1.3.1) Если размер словаря равен 3, то увеличь значение переменной result на 1.
# 1.3.2) Уменьшаем значение первого ключа в словаре dict.
# 1.3.3) Если значение первого ключа =0, удали ключ со значением из словаря dict.
# 1.3.4) Увеличь значение переменной l на 1.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1) (n)

### Сложная задача !!!

s = "aababcabc"

def countGoodSubstrings(s):
    l = 0
    dict = {}
    result = 0

    for i in range(len(s)):
        if s[i] in dict:
            dict[s[i]] += 1
        else:
            dict[s[i]] = 1
        # {'a': 1, 'b': 1, 'c': 1}

        if i - l + 1 == 3:
            if len(dict) == 3:
                result += 1
            # {'a': 1, 'b': 1, 'c': 1}
            dict[s[l]] -= 1
            # {'a': 0, 'b': 1, 'c': 1}
            if dict[s[l]] == 0:
                del dict[s[l]]
            # {'b': 1, 'c': 1}
            l += 1
    return result # 4

countGoodSubstrings(s)

assert countGoodSubstrings(s="xyzzaz") == 1
assert countGoodSubstrings(s="aababcabc") == 4