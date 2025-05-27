### Условие задачи:
# Вам дана строка с индексом 0 word, состоящая из строчных английских букв.
# Вам нужно выбрать один индекс и удалить букву в этом индексе word, чтобы частота появления каждой буквы word была одинаковой.
# Возвращает, если можно удалить одну букву, чтобы частота всех букв была одинаковой, и в противном случае . true word false
# Примечание:
# Частота буквы — это количество раз, когда она встречается в строке .x
# Вы должны удалить ровно одну букву и не можете ничего не делать.

# Example 1:
# Input: word = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

# Example 2:
# Input: word = "aazz"
# Output: false
# Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2,
# or vice versa. It is impossible to make all present is have equal frequency.

### Краткое условие:
# Необходимо определить, возможно ли удалить одну букву из строки word так, чтобы частота всех оставшихся букв стала равной.
# Верните true, если такое возможно, и false в противном случае.

# Краткое объяснение решение задачи:
# 1. Создается словарь (dict), который хранит количество вхождений каждого символа в строке.
# 2. Извлекаются значения (частоты) из словаря и помещаются в список (listValues).
# 3. Обработка частот:
#    - Если в listValues есть только одно значение 1, оно уменьшается на 1.
#    - В противном случае уменьшается максимальное значение в списке на 1.
# 4. Проверка условий:
#    - Если после изменений в listSet (уникальные частоты) длина равна 2 и одно из значений равно 0,
#    или если длина равна 1, то возвращаем True.
#    - В противном случае возвращает False.

# Полное объяснение решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Пройтись циклом по массиву word,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение этого ключа на 1.
# 1.2) Если ключа i НЕТу в словаре dict, то добавь его со значением 1.
# 2) Создаем массив listValues со значениями из словаря dict.
# 3) Если в массиве listValues есть только один элемент со значением 1, уменьшаем его на 1.
# 4) Иначе, уменьшаем первое максивальное число на 1.
# 5) Создаем массив listSet без дубликатов массива listValues.
# 6) Если (длина массива listValues равна 2 и первый элемент массива listValues равен 0) или (длина массива listValues равна 1),
# 6.1) То верни True.
# 7) Иначе, верни False.

# Сложность:
# 1) Время O (n)
# 2) Память O (n)

word = "ddaccb"

def equalFrequency(word):
    dict = {}

    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {'d': 2, 'a': 1, 'c': 2, 'b': 1}
    listValues = list(dict.values())  # [2, 1, 2, 1]
    if listValues.count(1) == 1:  # Если в массиве listValues есть только один элемент со значением 1
        listValues[listValues.index(1)] -= 1
    else:
        listValues[listValues.index(max(listValues))] -= 1  # уменьши первое максивальное число на 1
    # [1, 1, 2, 1]
    listSet = list(set(listValues))  # [1,2]

    if (len(listSet) == 2 and listSet[0] == 0) or (len(listSet) == 1):
        return True
    else:
        return False

equalFrequency(word)

assert equalFrequency(word="abcc") == True
assert equalFrequency(word="aazz") == False  # len(listSet) == 2 and listSet[0] == 0
assert equalFrequency(word="bac") == True  # len(listSet) == 2 and listSet[0] == 0
assert equalFrequency(word="ddaccb") == False
assert equalFrequency(word="zz") == True  # len(listSet) == 1
assert equalFrequency(word="abbcc") == True  # if listValues.count(1) == 1
# Доп юнитесты для проверки некоторых условий:
assert equalFrequency(word="a") == True # Тест с одной буквой
assert equalFrequency(word="aabbc") == True # Тест с частотой 1 и 2
# assert equalFrequency(word="") == True

### Старое рабочие решение, через хэш таблицу !!! ###

# Полное объяснение решение задачи:
# 0) Создаем словарь dict с ключами состоящий из букв строки word и со значением колличество повторений букв из строки word.
# 1) Проходимся циклом по строке word,
# 1.1) Уменьшаем значение ключа j на 1.
# 1.2) Если значение ключа j равно 0, то удали ключ и значение j из словаря dict.
# 1.3) Если длина множества значенией ключей из словаря dict равно 1, то верни True.
# 1.4) Увеличь значение ключа j на 1.
# 2) Верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

# from collections import Counter
#
# word = "abcc"
#
# def equalFrequency(word):
#     dict = Counter(word)
#     # Counter({'c': 2, 'a': 1, 'b': 1})
#
#     for j in word:
#         dict[j] -= 1
#
#         if dict[j] == 0:
#             del dict[j] # Counter({'c': 2, 'b': 1, 'a': 0})
#                         # Counter({'c': 2, 'a': 1, 'b': 0})
#
#         if len(set(dict.values())) == 1:
#             # Counter({'c': 1, 'a': 1, 'b': 1})
#             return True
#         dict[j] += 1
#
#     return False
#
# equalFrequency(word)

### Рабочие решение, но долгое !!!
# Сложность:
# 1) Время O (n log n)
# 2) Память O (n)
#
# word = "ddaccb"
#
# def equalFrequency(word):
#     dict = {}
#
#     for i in word:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     # dict = {'d': 2, 'a': 1, 'c': 2, 'b': 1}
#     listSortedValues = list(sorted(dict.values())) # [2, 1, 2, 1] -> [1, 1, 2, 2]
#     # listSortedValues= [1, 1, 2, 2]
#     if (len(listSortedValues) == 1) or (listSortedValues[0] == 1 and listSortedValues[1] == listSortedValues[-1]) or (
#             listSortedValues[-1] - listSortedValues[-2] == 1 and listSortedValues[-2] == listSortedValues[0]):
#         return True
#     else:
#         return False
#
# equalFrequency(word)
# assert equalFrequency(
#     word="abcc") == True  # (listSortedValues[-1] - listSortedValues[-2] == 1 and listSortedValues[-2] == listSortedValues[0])
# assert equalFrequency(word="aazz") == False
# assert equalFrequency(word="bac") == True  # (listSortedValues[0] == 1 and listSortedValues[1] == listSortedValues[-1])
# assert equalFrequency(word="ddaccb") == False
# assert equalFrequency(word="zz") == True # (len(listSortedValues) == 1)

# # Не проходят все юнитесты 26 / 50 (4 юнитест не проходит !!!)
#
# word = "ddaccb"
#
# def equalFrequency(word):
#     dict = {}
#
#     for i in word:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#
#     # {'d': 2, 'a': 1, 'c': 2, 'b': 1}
#
#     if len(dict.values()) == len(word): # защита от третьего юнитеста !!!
#         return True
#
#     if len(set(dict.values())) <= 1:
#         return False
#     else:
#         return True
#
# equalFrequency(word)