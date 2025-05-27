### Условие задачи:
# Учитывая a pattern и строку s, найдите, s следует ли этому шаблону.
# Здесь следовать означает полное совпадение, такое, что существует биекция между буквой в pattern и непустым словом в s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

### Краткое условие:
# Вернуть "true" если количество одинаковых букв в строке pattern, совпадает c количество повторяющихся слов в строке s.
# Иначе вернуть "false".

# Краткое объяснение решение задачи:
# 1. Разбиваем строку s на слова.
# 2. Создаем множество пар (символ, слово) с помощью zip.
# 3. Проверяем, что:
#    - Равно длине Количество уникальных символов в pattern равно количеству уникальных слов в s.
#    - Длина pattern равна количеству слов в s.
# Если все условия выполняются, то возвращает True, иначе — False.

# Полное объяснение решение задачи:
# 0) Создаем массив listS со значением строки s и кортедж zippedSet со значениеми из pattern и listS.
# 1) Если длина множества pattern равна длине множество listS == длине zippedSet и длина pattern равна listS, то вернуть True.
# 2) Иначе, верни False.

# Сложность:
# 1) Время O (m + n)
# 2) Память O (1) (k + n)

pattern = "abba"
s = "dog cat cat dog"

def wordPattern(pattern, s):
    listS = s.split() # ['dog', 'cat', 'cat', 'dog']
    zippedSet = set(zip(pattern, listS))  # {('b', 'cat'), ('a', 'dog')}

    if len(set(pattern)) == len(set(listS)) == len(zippedSet) and len(pattern) == len(listS):
        return True
    else:
        return False
    #return len(set(pattern)) == len(set(s.split())) == len(set(zip(pattern, s.split()))) and len(pattern) == len(s.split())

wordPattern(pattern, s)

assert wordPattern(pattern="abba", s="dog cat cat dog") == True
assert wordPattern(pattern="abba", s="dog cat cat fish") == False
assert wordPattern(pattern="aaaa", s="dog cat cat dog") == False
assert wordPattern(pattern="aba", s="dog cat cat") == False
assert wordPattern(pattern="aba", s="cat cat cat dog") == False
# Доп юнитесты для проверки некоторых условий:
assert wordPattern(pattern="a", s="dog") == True  # Тест с одним словом
assert wordPattern(pattern="aaaa", s="dog dog dog dog") == True  # Тест с одинаковыми символами
assert wordPattern(pattern="a", s="") == False  # Тест с пробелами
assert wordPattern(pattern="", s="") == True  # Тест с пустыми строками

    ### Старое рабочие решение через хэш таблицу !!! ###
# Полное объяснение решение задачи:
# 0) Создаем пустой словарь dict и массив listS со значением слова из строки s, и переменную lenListS со значением длины массива listS.
# 1) Если длина строки pattern не равна lenListS или длина множеств строки pattern не равна длине множеств listS, то верни False.
# 2) Проходимся циклом по диапазону длины массива listS,
# 2.1) Если буква из строки pattern нету в словаре dict, то добавь ключ pattern[i] со значением listS[i] в словарь dict.
# 2.2) Если ключ [pattern[i]] из словаря dict не равен listS[i], то верни False.
# 3) Верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

# pattern = "abba"
# s = "dog cat cat dog"
#
# def wordPattern(pattern, s):
#     dict = {}
#     listS = s.split()  # ['dog', 'cat', 'cat', 'dog']
#     lenListS = len(listS)  # 4
#
#     if len(pattern) != lenListS or len(set(pattern)) != len(set(listS)):
#         # тут упало pattern="aaaa", s="dog cat cat dog"
#         return False
#
#     for i in range(lenListS):
#         if pattern[i] not in dict:
#             dict[pattern[i]] = listS[i]
#
#         elif dict[pattern[i]] != listS[i]:
#             return False
#     # {'a': 'dog', 'b': 'cat'}
#     return True
#
# wordPattern(pattern, s)

### Не проходят все тесты 36 / 42
# pattern = "aba"
# s = "dog cat cat"
#
# def wordPattern(pattern,s):
#         dict1 = {}
#         dict2 = {}
#         t=s.split(" ")
#
#         for i in pattern:
#             if i in dict1:
#                 dict1[i] += 1
#             else:
#                 dict1[i] = 1
#         # {'a': 2, 'b': 1}
#         for j in t:
#             if j in dict2:
#                 dict2[j] += 1
#             else:
#                 dict2[j] = 1
#         # {'dog': 1, 'cat': 2}
#         if set(dict1.values()) == set(dict2.values()):
#             return True
#         else:
#             return False
#
# wordPattern(pattern,s)