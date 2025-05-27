### Условие задачи:
# Вам дан массив строк words (с индексом 0).
# За одну операцию выберите два разных индекса i и j, где words[i]— непустая строка,
# и переместите любой символ из words[i]в любую позицию в words[j].
# Возвращает результат true, если вы можете сделать все строки равными,
# используя любое количество операций, и в противном случае. words false

# Example 1:
# Input: words = ["abc","aabc","bc"]
# Output: true
# Explanation: Move the first 'a' in words[1] to the front of words[2],
# to make words[1] = "abc" and words[2] = "abc".
# All the strings are now equal to "abc", so return true.

# Example 2:
# Input: words = ["ab","a"]
# Output: false
# Explanation: It is impossible to make all the strings equal using the operation.

### Краткое условие:
# Надо вернуть true если все буквы из 0 элемнет массива words есть в другом элементе массива words.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную lenArryWords со значением длины массива words.
# 1) Проходимся циклом по массиву words,
# 1.1) Проходимся циклом по каждому слову внутри массива words,
# 1.1.1) Если ключ j есть в словаре dict, то увеличь значние ключа j на 1.
# 1.1.2) Если ключа j НЕТу в словаре dict, то добавь ключ j в словарь dict со значением 1.
# 2) Проходимся циклом по словарю dict,
# 2.1) Значение ключа j делеться без остатка на переменную lenArryWords, то верни False.
# 3) Верни True.

# Сложность:
# 1) Время O(n) (m)
# 2) Память O(n) (m)

words = ["aabbccdde", "e"]

def makeEqual(words):
    dict = {}

    for i in words:
        for j in i:
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
    # {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}
    for k in dict:      # 2
        if dict[k] % len(words):
            return False

    return True

makeEqual(words)

assert makeEqual(words=["abc", "aabc", "bc"]) == True
assert makeEqual(words=["ab", "a"]) == False
assert makeEqual(words=["aabbccdde", "e"]) == True

#  Не проходят 144 автотест
# words = ["aabbccdde", "e"]
#
# def makeEqual(words):
#
#     if len(words) == 1:
#         return True
#     else:
#         dict = set(words[0])
#         # {'e', 'c', 'd', 'b', 'a'}
#         for j in range(1, len(words)):  # range(1, 2)
#             wordsDict = set(words[j])
#             #     {'e'}     {'e'}
#             if wordsDict == dict:
#                 return True
#             else:
#                 return False
#
# makeEqual(words)
