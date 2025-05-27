### Условие задачи:
# Строка s хороша, если каждая содержащаяся в ней буква алфавита отображается как в верхнем, так и в нижнем регистре.
# Например, приятно потому, что и появляются, и появляются.
# Однако не потому, что появляется, а не появляется.s"abABB"'A''a''B''b'"abA"'b''B'
# Учитывая строку s, верните самую длинную ее подстроку. Если их несколько, верните подстроку самого раннего вхождения.
# Если их нет, верните пустую строку s.

# Example 1:
# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.

# Example 2:
# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

# Example 3:
# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.

                                                ### Добавить в список !

### Краткое условие:
# Вернуть строку из строки s с одинаковыми большими буквами.

###                         С хэшом таблицы
# Алгоритм решение задачи:
# 0) Созданем: пустую строку result и переменную lenStringS в которой будет храниться длина строки s.
# 1) Проверяем если длина строки s равна 1 или 0, то верни пустую строку.
# 2) Проходимся циклом по диапазону от 2 до длины строки s+1,
# 2.1) Проходимся циклом по диапазону (от 0 до длины строки - i+1) ,
# 2.2) Создаем строку string со значением строки s c первыми двумя буквами ее,
# 2.3) Создаем словарь setDict1 с сетом в котором находится строка string,
# 2.4) Создаем словарь setDict2 c сетом в котором находится строка string, где маленькие буквы стали большими, а большие маленькими.
# 2.5) Уменьшаем словарь setDict1 на setDict2.
# 2.6) Если длина словаря setDict1 равна 0 и длина строки result меньше чем длина строки string, то result = string.
# 3) Верни строку result.

# Сложность:
# 1) Время O (n^2) (n^3)
# 2) Память O(1)   (n)

### Сложная задача !!!

s = "YazaAay"

def longestNiceSubstring(s):
    lenStringS = len(s) # 7
    result = ""

    if lenStringS == 1 or lenStringS == 0:
        return ""

    for i in range(2, lenStringS + 1): # range(2, 8)
        for j in range(lenStringS - i + 1): # range(0, 6) range(0, 5) range(0, 4) range(0, 3) range(0, 2) range(0, 1)
            string = s[j:i + j]  # Ya
            setDict1 = set(string)  # {'a', 'Y'}
            setDict2 = set(string.swapcase())  # {'A', 'y'}
            setDict1 -= setDict2  # {'Y', 'a'}

            if len(setDict1) == 0 and len(result) < len(string):
                result = string

    return result # aAa

longestNiceSubstring(s)

assert longestNiceSubstring(s="YazaAay") == "aAa"
assert longestNiceSubstring(s="Bb") == "Bb"
assert longestNiceSubstring(s="c") == ""

###                         Без хэша таблицы
# Алгоритм решение задачи:
# 0) Создаем пустую строку result и переменную lenStringS со значением длины строки s.
# 1) Проходимся циклом по диапазону длины строки,
# 1.1) Проходимся циклом по диапазону (от i до длины строки),
# 1.1.1) Если все выражение есть ли похожая буква в другом регистре,
# 1.1.1.1) Если ли длина текущей подстроки больше длины строки result, то текущая подстрока становится новым значением result.
# 2) Верни строку result.

# Сложность:
# 1) Время O(n^3)
# 2) Память O(n^2)

# s = "YazaAay"
#
# def longestNiceSubstring(s):
#     result = ""
#     lenStringS = len(s)
#
#     for i in range(lenStringS):
#         for j in range(i, lenStringS):
#             if all(ch.swapcase() in s[i:j + 1] for ch in s[i:j + 1]):
#                 if len(s[i:j + 1]) > len(result):
#                     result = s[i:j + 1]
#
#     return result
#
# longestNiceSubstring(s)
