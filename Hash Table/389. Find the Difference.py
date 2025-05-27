### Условие задачи:
# Вам даны две строки s и t.
# Строка t генерируется путем случайного перетасовывания строки s с последующим добавлением еще одной буквы в случайную позицию.
# Верните букву, которая была добавлена в t.

# Example 1:
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.

# Example 2:
# Input: s = "", t = "y"
# Output: "y"

### Краткое условие:
# Надо найти символ, который есть только в строке t и нету в строке s.

# Алгоритм решение задачи:
# 0) Создаем два пустых словаря dictS и dictT.
# 1) Проходимся циклом по страке s,
# 1.1) Если ключ i есть в словаре dictS, то увеличь значние ключа i на 1.
# 1.2) Если ключ i НЕТу в словаре dictS, то добавь ключь i со значением 1 в словарь dictS.
# 2) Проходимся циклом по страке t,
# 2.1) Если ключ j есть в словаре dictT, то увеличь значние ключа j на 1.
# 2.2) Если ключ j НЕТу в словаре dictT, то добавь ключь j со значением 1 в словарь dictT.
# 3) Проходимся циклом по словарю dictT,
# 3.1) Если ключа k нету в словаре dictS или значение ключа k в словаре dictT больше чем значение ключа k в словаре dictS,
# 3.2) Верни k.

# Сложность:
# 1) Время O(n)
# 2) Память O(n) (k)

s = "abcd"
t = "abcde"

def findTheDifference(s, t):
    dictS = {}
    dictT = {}

    for i in s:
        if i in dictS:
            dictS[i] += 1
        else:
            dictS[i] = 1
    # {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    for j in t:
        if j in dictT:
            dictT[j] += 1
        else:
            dictT[j] = 1
    # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
    for k in dictT:
        if k not in dictS or dictT[k] > dictS[k]:
            return k  # e

findTheDifference(s, t)

assert findTheDifference(s="abcd", t="abcde") == "e"
assert findTheDifference(s="", t="y") == "y"