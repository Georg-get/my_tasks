### Условие задачи:
# Дана строка s, найдите в ней первый неповторяющийся символ и верните его индекс. Если он не существует, верните -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1


### Краткое условие:
# В строке s, найдите в ней первый неповторяющийся символ и верните его индекс.
# Если все буквы повторяются в строке, то вернуть -1.

# Алгоритм решение задачи:
# 0) Создаем словарь dict.
# 1) Проходимся циклом по стороке s,
# 1.1) Если ключ i есть в словаре dict, то увеличь значние ключа i на 1.
# 1.2) Если ключ i НЕТу в словаре dict, то добавь ключ i со значением 1 в словарь dict.
# 2) Проходимся циклом по стороке s,
# 2.1) Если значение ключа j равно 1, то верни индекс j в строке s.
# 3) Верни -1.

# Сложность:
# 1) Время O(n)
# 2) Память O(n) (k)

s = "loveleetcode"

def firstUniqChar(s):
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1}
    for j in s:
        if dict[j] == 1:
            # v
            return s.index(j)  # v под индексом 2 в строке s

    return -1

firstUniqChar(s)

assert firstUniqChar(s="leetcode") == 0
assert firstUniqChar(s="loveleetcode") == 2
assert firstUniqChar(s="aabb") == -1