### Условие задачи:
# Учитывая две строки needle и haystack, верните индекс первого вхождения needle in haystack или,
# -1 если needle он не является частью haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

### Краткое условие:
# Нужно вернуть индекс первого вхождения needle в haystack, или -1, если needle не содержится в haystack.

# Краткое объяснение решение задачи:
# Ставим левый указатель на начало строки haystack и правый указатьль на длину слова needle в строке haystack
# Проходимся циклом пока правый указатель не дойдет до конца строки,
# Если подсрака из строки haystack совпадает с строкой needle, возвращаем left.
# Иначе двигаем левый и правый указатели.
# Вернуть -1.

# Полное объяснение решение задачи:
# 0) Левый указатель равен 0, а правый указатель равен длине строки needle.
# 1) Проходимся циклом ваилд пока правый указатель не дойдет до конца строки haystack,
# 1.1) Если строка needle похожа на подстраку из строки haystack которая задана левым и правым указателем, то верни left.
# 1.2) Иначе, увеличь левый и правый указатель на 1.
# 2) Верни -1

# Сложность:
# 1) Время O(n ⋅ m)
# 2) Память O(1)
#           | |
haystack = "sadbutsad"
needle = "sad"

def strStr(haystack, needle):
    left = 0
    right = len(needle)

    while right <= len(haystack):
        #  sad    ==        sad
        if needle == haystack[left:right]:
            return left

        else:
            left += 1
            right += 1

    return -1

strStr(haystack, needle)

assert strStr(haystack="sadbutsad", needle="sad") == 0
assert strStr(haystack="leetcode", needle="leeto") == -1
# Доп юнитесты для проверки некоторых условий:
assert strStr(haystack="", needle="a") == -1 # Пустая строка
assert strStr(haystack="hello", needle="") == 0 # Пустая подстрока
assert strStr(haystack="hello", needle="hello") == 0 # Одинаковые строки

### Решение без алгоса !!!

# Сложность:
# 1) Время O(n ⋅ m)
# 2) Память O(1)

# haystack = "sadbutsad"
# needle = "sad"
#
# def strStr(haystack, needle):
#
#     if needle in haystack:
#         return haystack.find(needle)
#     else:
#         return -1
#
# strStr(haystack, needle)

### Два указателя ### Старое решение !!!!

# Краткое объяснение решение задачи:
# 1. Устанавливаем левый указатель на начало строки haystack и правый указатель на начало строки needle.
# 2. Проходимся циклом пока левый указатель не дойдет до конца строки haystack:
#    - Если указатель right достиг конца needle, это означает, что подстрока найдена, и возвращается индекс начала вхождения (left - lenNeedle).
#    - Если текущие символы haystack[left] и needle[right] совпадают, увеличивается указатель right.
#    - Если символы не совпадают, указатель left откатывается на количество совпадений (значение right), а right сбрасывается на 0 для начала нового поиска.
# 3. Если после завершения цикла right равен длине needle, это значит, что подстрока найдена, и возвращается индекс.
# Если нет, возвращается -1, что указывает на отсутствие подстроки.

# Полное объяснение решение задачи:
# 0) Создаем переменные: lenHaystack со значением длины строки haystack и lenNeedle со значением длины строки needle,
# и left и right со значением 0.
# 1) Проходимся циклома ваилд пока left не станет меньше right,
# 1.1) Если right равна lenNeedle, то верни left - lenNeedle.
# 1.2) Если буква на которой установлен левый указатель из строки haystack равна букве на которой установлен правой указатель из строки needle,
# 1.2.1) То увеличь значение переменной right на 1.
# 1.3) Если буква на которой установлен левый указатель из строки haystack НЕ равна букве на которой установлен правой указатель из строки needle,
# 1.3.1) Присвой переменной left значение left - right,
# 1.3.2) Присвой переменной right значение 0.
# 1.4) Увеличь значение переменной left на 1.
# 2) Если right рано lenNeedle, то верни lenHaystack - lenNeedle.
# 3) Верни -1.

# Сложность:
# 1) Время O(n ⋅ m)
# 2) Память O(1)

# haystack = "sadbutsad"
# needle = "sad"
#
# def strStr(haystack, needle):
#     lenHaystack = len(haystack)  # 9
#     lenNeedle = len(needle)  # 3
#     left = 0
#     right = 0
#
#     while left < lenHaystack:
#
#         if right == lenNeedle:  # когда у нас правый указатель установлены в слове needle дошел до конца слова
#             return left - lenNeedle  # мы возращаем 3 - длина слова needle (3) = 0. ЭТО ПЕРВЫЙ КЕЙС
#
#         elif haystack[left] == needle[right]:
#             right += 1
#
#         else:                   # это второй тесткейс
#             left -= right
#             right = 0
#
#         left += 1
#     #    0       5 - это второй тесткейс
#     if right == lenNeedle:
#         return lenHaystack - lenNeedle
#     else:
#         return -1
#
# strStr(haystack, needle)

                        ### Решение без алгоритма !!! ###

# Сложность:
# 1) Время O(n * m)
# 2) Память O(1)

# haystack = "sadbutsad"
# needle = "sad"
#
# def strStr(haystack, needle):
#     return haystack.find(needle)

###                         КМП
# Полное объяснение решение задачи:
# Сложность:
# 1) времени O(n)
# 2) памяти O(n)

# haystack = "sadbutsad"
# needle = "sad"
#
# def strStr(haystack, needle):
#     def computePiArray(string):
#         n = len(string)
#         piArry = [0] * n
#         i = 1
#         length = 0
#
#         while i < n:
#             if string[i] == string[length]:
#                 length += 1
#                 piArry[i] = length
#                 i += 1
#             else:
#                 if length != 0:
#                     length = piArry[length - 1]
#                 else:
#                     piArry[i] = 0
#                     i += 1
#
#         return piArry  # [0, 0, 0]
#     piArry = computePiArray(needle)
#
#     # Основное решение
#     n = 0  # needle index
#     for h in range(len(haystack)): # range(0, 9)
#         while n > 0 and needle[n] != haystack[h]:
#             n = piArry[n - 1]
#
#         if needle[n] == haystack[h]:
#             n += 1
#
#         if n == len(needle):
#             return h - n + 1
#
#     return -1
# strStr(haystack, needle)