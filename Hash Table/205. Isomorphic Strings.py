### Условие задачи:
# Учитывая две строки s и t, определите, изоморфны ли они.
# Две строки s и t являются изоморфными, если символы в них s можно заменить, чтобы получить t.
# Все вхождения символа должны быть заменены другим символом с сохранением порядка символов.
# Никакие два символа не могут сопоставляться одному и тому же символу, но символ может сопоставляться сам с собой.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

### Краткое условие:
# Надо проверить являются ли две строи s и t изоморфными, если да то вернуть true иначе false.
# Это значит, что одинаковым символам в одной строке соответствуют одинаковые символы в другой строке.


                                ### Хэш сет !!! ###
# Краткое объяснение решение задачи:
# Проверяем, равны ли длины множество пар символов из строк s и t, и длина множеств уникальных символов в обеих строках.

# Полное объяснение решение задачи:
# 0) Создаем кортеж zippedSet в котором будет буква из строки s и буква из строки t и убираем дубликаты кортеджей.
# 1) Если длина zippedSet равна длине строки s без дублей и равна строке t без дублей, то верни True.
# 2) Иначе, то верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1) n

s = "egg"
t = "add"

def isIsomorphic(s, t):
    zippedSet = set(zip(s, t)) # {('g', 'd'), ('e', 'a')}

        # 2                 # 2           # 2
    if len(zippedSet) == len(set(s)) == len(set(t)):
        return True
    else:
        return False
    # return len(set(zip(s, t))) == len(set(s)) == len(set(t))
isIsomorphic(s, t)

assert isIsomorphic(s="egg", t="add") == True # Тест с изоморфными строками
assert isIsomorphic(s="foo", t="bar") == False # Тест с не изоморфными строками
assert isIsomorphic(s="paper", t="title") == True # Тест с одинаковыми строками
assert isIsomorphic(s="bbbaaaba", t="aaabbbba") == False # !!! этот тест ломает последний код !!! # Тест с разной длиной строк
# Доп юнитесты для проверки некоторых условий:
assert isIsomorphic(s="", t="") == True # Тест с пустыми строками
assert isIsomorphic(s="a", t="") == False # Тест с одной пустой строкой !
assert isIsomorphic(s="abc", t="ab") == False # Тест с разной длиной строк
assert isIsomorphic(s="aa", t="bb") == True # Тест с дубликатами
assert isIsomorphic(s="abca", t="zbxz") == True # Тест с различными символами
assert isIsomorphic(s="a", t="b") == True # Тест с одним символом

                                                    ### Хэш таблицы !!!
# Полное объяснение решение задачи:
# 0) Создаем два пустых словаря dictS и dictT.
# 1) Проходимся циклом по диапазону от 0 до длины строки s,
# 1.1) Если (элемент строки s есть в как ключ в словаре dictS и значение ключа не равно элементу из строки t) или
# (элемент строки t есть в как ключ в словаре dictT и значение ключа не равно элементу из строки s), то верни False.
# 1.2) Добавь в словарь dictS ключ букву из массива s со значением буквы из строки t.
# 1.3) Добавь в словарь dictT ключ букву из массива t со значением буквы из строки s.
# 2) Верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)
#
# s = "egg"
# t = "add"
#
# def isIsomorphic(s, t):
#     dictS = {}
#     dictT = {}
#
#     for i in range(len(s)):
#         if (s[i] in dictS and dictS[s[i]] != t[i]) or (t[i] in dictT and dictT[t[i]] != s[i]):
#             return False
#
#         dictS[s[i]] = t[i]
#         dictT[t[i]] = s[i]
#     # dictS = {'e': 'a', 'g': 'd'}
#     # dictT = {'a': 'e', 'd': 'g'}
#     return True
# isIsomorphic(s, t)

### Не проходят все тесты 35 / 47
# s = "egg"
# t = "add"
#
# def isIsomorphic(s, t):
#     dict1 = {}
#     dict2 = {}
#
#     for i in s:
#         if i in dict1:
#             dict1[i] += 1
#         else:
#             dict1[i] = 1
#     # {'e': 1, 'g': 2}
#     for j in t:
#         if j in dict2:
#             dict2[j] += 1
#         else:
#             dict2[j] = 1
#     # {'a': 1, 'd': 2}
#     if set(dict1.values()) == set(dict2.values()):
#         return True
#     else:
#         return False
#
# isIsomorphic(s, t)
