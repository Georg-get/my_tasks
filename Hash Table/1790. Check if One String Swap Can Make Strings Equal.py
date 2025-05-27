### Условие задачи:
# Вам даны две строки s1 одинаковой s2 длины. Замена строки — это операция,
# при которой вы выбираете два индекса в строке (не обязательно разные) и меняете местами символы в этих индексах.
# Возвращает значение true, если можно сделать обе строки равными,
# выполнив не более одной замены строк ровно на одной из строк. В противном случае вернитесь false.

# Example 1:
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

# Example 2:
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.

# Example 3:
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.

### Краткое условие:
# Вернуть "true", если можно сделать строки: s1 и s2 равными, выполнив не более одного обмена символов в одной из строк,
# иначе вернуть "false".

###                         С хэшом таблицы
# Краткое объяснение решение задачи:
# 1. Создаются два словаря для подсчета символов в каждой строке.
# 2. Сравниваются символы на соответствующих позициях, чтобы определить количество различий.
# 3. Если строки идентичны или различаются ровно в двух местах и имеют одинаковый набор символов, то возвращает True.
# В противном случае — False.

# Полное объяснение решение задачи:
# 0) Создаем два пустых словаря dictS1 и dictS2, и переменную count со значением 0.
# 1) Проходимся циклом по стороке s1,
# 1.1) Если ключ i есть в словаре dictS1, то увеличь значение ключа i на 1.
# 1.2) Иначе, добавь ключ i со значением 1 в словарь dictS1.
# 2) Проходимся циклом по стороке s2,
# 2.1) Если ключ j есть в словаре dictS2, то увеличь значение ключа j на 1.
# 2.2) Иначе, добавь ключ j со значением 1 в словарь dictS2.
# 3) Проходимся циклом по диапазону от 0 до длины строки s1,
# 3.1) Если i в строке s1 не равна i в строке s2, то увеличь значение переменной count на 1.
# 4) Верни рано ли значение переменной count 0 или count равен 2 и словарь dictS1 равен словарю dictS2.

# Сложность:
# 1) Время O(n)
# 2) Память O(k) (n)

s1 = "attack"
s2 = "defend"

def areAlmostEqual(s1, s2):
    dictS1 = {}
    dictS2 = {}
    count = 0

    for i in s1:
        if i in dictS1:
            dictS1[i] += 1
        else:
            dictS1[i] = 1
    # {'a': 2, 't': 2, 'c': 1, 'k': 1}
    for j in s2:
        if j in dictS2:
            dictS2[j] += 1
        else:
            dictS2[j] = 1
    # {'d': 2, 'e': 2, 'f': 1, 'n': 1}
    for k in range(len(s1)):
        if s1[k] != s2[k]:
            count += 1
    # count = 6
    if count == 0 or count == 2 and dictS1 == dictS2:
        return True
    else:
        return False
    # return count == 0 or count == 2 and dictS1 == dictS2

areAlmostEqual(s1, s2)

assert areAlmostEqual(s1="bank", s2="kanb") == True
assert areAlmostEqual(s1="attack", s2="defend") == False
assert areAlmostEqual(s1="kelb", s2="kelb") == True  # Строки равны
assert areAlmostEqual(s1="adcd", s2="dcba") == False  # Этот тест ломает мое решение !!!
assert areAlmostEqual(s1="bankb", s2="kannb") == False
# Доп юнитесты для проверки некоторых условий:
assert areAlmostEqual(s1="mno", s2="nmo") == True  # Сложный случай
assert areAlmostEqual(s1="ab", s2="cd") == False  # Обмен не приводит к равенству
# assert areAlmostEqual( s1 = "abc", s2 = "ab") == False # Разные длины строк

###                         Без хэша таблицы
# Полное объяснение решение задачи:
# 0) Создаем переменную result равную 0.
# 1) Проходимся циклом по диапазону длины строки s1,
# 1.1) Если i из строки s1 не равна i из строки s2, то увеличь переменную result на 1.
# 2) Если отсортированая строка s1 не равна отсортированой строке s2, то верни False.
# 3) Если переменная result равна 2 или переменная result равна 0, то верни True.

# Сложность:
# 1) Время O(n*log(n))
# 2) Память O(n)

# s1 = "attack"
# s2 = "defend"
#
# def areAlmostEqual(s1, s2):
#     result = 0
#
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             result += 1
#     # 6
#     if sorted(s1) != sorted(s2):
#         return False
#
#     elif (result == 2 or result == 0):
#         return True
#
# areAlmostEqual(s1, s2)

### Не проходят все тесты 107 / 132
# Полное объяснение решение задачи:

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

# s1 = "attack"
# s2 = "defend"
#
# def areAlmostEqual(s1, s2):
#     dictS1 = {}
#     dictS2 = {}
#
#     for i in s1:
#         if i in dictS1:
#             dictS1[i] += 1
#         else:
#             dictS1[i] = 1
#     # {'a': 2, 't': 2, 'c': 1, 'k': 1}
#     for j in s2:
#         if j in dictS2:
#             dictS2[j] += 1
#         else:
#             dictS2[j] = 1
#     # {'d': 2, 'e': 2, 'f': 1, 'n': 1}
#     if dictS1 == dictS2:
#         return True
#     else:
#         return False
#
# areAlmostEqual(s1, s2)