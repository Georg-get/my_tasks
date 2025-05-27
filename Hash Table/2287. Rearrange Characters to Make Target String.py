### Условие задачи:
# Вам даны две строки с индексом 0 s и target.
# Вы можете взять несколько букв s и переставить их так, чтобы образовались новые строки.
# Верните максимальное количество копий, target которые можно получить, взяв буквы sи переставив их.

# Example 1:
# Input: s = "ilovecodingonleetcode", target = "code"
# Output: 2
# Explanation:
# For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
# For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
# The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
# We can make at most two copies of "code", so we return 2.

# Example 2:
# Input: s = "abcba", target = "abc"
# Output: 1
# Explanation:
# We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
# We can make at most one copy of "abc", so we return 1.
# Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".

# Example 3:
# Input: s = "abbaccaddaeea", target = "aaaaa"
# Output: 1
# Explanation:
# We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
# We can make at most one copy of "aaaaa", so we return 1.

                                                ### Добавить в список !

### Краткое условие:
# Надо посчитать сколько раз можно из слова в строке target собрать из строки s.

# Алгоритм решение задачи:
# 0) Создаем два пустых словаря dictS и dictTarget, и два пустых массива x и y.
# 1) Проходимся циклом по строке s,
# 1.1) Если ключ i есть в словаре dictS, то увеличь значение ключа i на 1.
# 1.2) Если ключ i есть в словаре dictS, то добавь ключ i со значением 1.
# 2) Проходимся циклом по строке target,
# 2.1) Если ключ j есть в словаре dictTarget, то увеличь значение ключа j на 1.
# 2.2) Если ключ j есть в словаре dictTarget, то добавь ключ j со значением 1.
# 3) Проходимся циклом по преобразованому словарю dictTarget в кортедж,
# 3.1) Если ключп i НЕТу в словаре dictS, то добавь в массив x i.
# 3.2) Если ключ i есть в словаре dictS, то добавь в массив y значение ключа i деленное на j.
# 4) Если длина массива x больше 0, то верни 0.
# 5) Если длина массива x НЕ больше 0, то верни минимальный элемент массива y.

# Сложность:
# 1) Время O(n) (n + m)
# 2) Память O(n)

### Сложная задача !!!

from collections import Counter

s = "ilovecodingonleetcode"
target = "code"

def rearrangeCharacters(s, target):
    dictS = {}
    dictTarget = {}
    x = []
    y = []

    for i in s:
        if i in dictS:
            dictS[i] += 1
        else:
            dictS[i] = 1
    # {'i': 2, 'l': 2, 'o': 4, 'v': 1, 'e': 4, 'c': 2, 'd': 2, 'n': 2, 'g': 1, 't': 1}
    for j in target:
        if j in dictTarget:
            dictTarget[j] += 1
        else:
            dictTarget[j] = 1
    # {'c': 1, 'o': 1, 'd': 1, 'e': 1}
    for i, j in Counter(dictTarget).items(): # dict_items([('c', 1), ('o', 1), ('d', 1), ('e', 1)])
        if i not in dictS:
            x.append(i)
        else:
            y.append(dictS[i] // j)
    # x = []
    # y = [2, 4, 2, 4]
    if len(x) > 0:
        return 0
    else:
        return min(y)  # 2

rearrangeCharacters(s, target)

assert rearrangeCharacters(s="ilovecodingonleetcode", target="code") == 2
assert rearrangeCharacters(s="abcba", target="abc") == 1
assert rearrangeCharacters(s="abbaccaddaeea", target="aaaaa") == 1