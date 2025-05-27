### Условие задачи:
# Отдельная строка — это строка, которая присутствует в массиве только один раз.
# Учитывая массив строк arr и целое число k, верните отдельную строку, присутствующую в.
# Если имеется меньше различных строк, верните пустую строку .kth arrk""
# Обратите внимание, что строки рассматриваются в том порядке, в котором они появляются в массиве.

# Example 1:
# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned.

# Example 2:
# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.

# Example 3:
# Input: arr = ["a","b","a"], k = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".

### Краткое условие:
# Вернуть строку, которая соответствует k в массиве arr.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по массиву arr,
# 1.1) Если i есть в словаре dict, то увели значение ключа на 1.
# 1.2) Если i НЕТу в словаре dict, то добавь i как ключ со значение 1.
# 2) Проходимся циклом по массиву arr,
# 2.1) Если значение ключа j равно 1, то уменьшаем значение переменной k на 1,
# 2.2) Если переменная k равна 0, верни j.
# 3) Верни пустую строку.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

arr = ["d", "b", "c", "b", "c", "a"]
k = 2

def kthDistinct(arr, k):
    dict = {}

    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {'d': 1, 'b': 2, 'c': 2, 'a': 1}
    for j in arr:  # {'d': 1}
        if dict[j] == 1:
            k -= 1  # k=2
            if k == 0:
                # k стало равно нулю когда дошло до ключа 'a': 1
                return j

    return ""

kthDistinct(arr, k)

assert kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2) == "a"
assert kthDistinct(arr=["aaa", "aa", "a"], k=1) == "aaa"
assert kthDistinct(arr=["a", "b", "a"], k=3) == ""