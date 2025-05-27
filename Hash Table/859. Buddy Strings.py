### Условие задачи:
# Учитывая две строки s и goal, верните true, если вы можете поменять местами две буквы, s чтобы результат был равен goal,
# в противном случае верните false.
# Замена букв определяется как взятие двух индексов i и j(с индексом 0) так, что i != j и замена символов на s[i]и s[j].
# Например, замена индексов 0и результатов 2в ."abcd""cbad"

# Example 1:
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

# Example 2:
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

# Example 3:
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

### Краткое условие:
# Необходимо вернуть true, если можно поменять местами две буквы в строке s, чтобы она стала равной строке goal,
# в противном случае вернуть false.

# Краткое объяснение решение задачи:
# 1. Проверка длины: Если длины строк s и goal не равны, то возвращаем False.
# 2. Проверка на равенство: Если строки равны, то проверяем, есть ли в строке s повторяющиеся символы.
# Если есть, возвращает True, иначе — False.
# 3. Сравнение различий: Если строки не равны, то находим позиции, где символы отличаются, и сохраняет их в список diffs.
# 4. Проверка различий: Если в списке diffs ровно два элемента и они являются обратными парами (например, ('a', 'b') и ('b', 'a')),
# то возвращаем True. В противном случае — False.

# Полное объяснение решение задачи:
# 0) Если длина строки s не равна длине строки goal, то верни False.
# 1) Если строка s такая же как строка goal,
# 1.1) Если длина множества s меньше длины строки s, то верни True
# 1.2) Иначе, верни False.
# 2) Иначе,
# 2.1) Создаем пустой массив diffs,
# 2.2) Проходимся циклом по диапазону от 0 до длины строки s,
# 2.2.1) Если элемент i из строки s не равен элементу i из строки goal, в массив diffs добавь кортедж из (s[i], goal[i]).
# 2.3) Если длина массива diffs равна 2 и 0 элемент массива diffs равен перевернутому элементу 1 из массива diffs,
# 2.3.1) Вернуть True.
# 2.4) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1) (n)

s = "ab"
goal = "ba"

def buddyStrings(s, goal):

    if len(s) != len(goal):
        return False # это пятый юнитест !!!

    elif s == goal:
        if len(set(s)) < len(s):
            return True
        else:
            return False
    else:
        diffs = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append((s[i], goal[i]))
        # diffs = [('a', 'b'), ('b', 'a')]
        #       2              ('a', 'b')    ('a', 'b')
        if len(diffs) == 2 and diffs[0] == diffs[1][::-1]:
            return True
        else:
            return False

buddyStrings(s, goal)

assert buddyStrings(s="ab", goal="ba") == True
assert buddyStrings(s="ab", goal="ab") == False
assert buddyStrings(s="aa", goal="aa") == True
assert buddyStrings(s="aaaaaaabc", goal="aaaaaaacb") == True
assert buddyStrings(s="ab", goal="babbb") == False
assert buddyStrings(s="abcd", goal="badc") == False
# Доп юнитесты для проверки некоторых условий:
assert buddyStrings("abcd", goal="abc") == False  # Случаи с разными длинами

### Старая версия хэша таблицы !!! ###
# Полное объяснение решение задачи:
# 0) Создаем два пустых словаря dict1 и dict2, и переменную result равную 0.
# 1) Если длина строки s не равна длине строки goal, верни False.
# 2) Если строка s равна строке goal,
# 2.1) Пройдись циклом по строке s, запиши ключ i со значением i увеличеным на 1 в словарь dict1.
# 2.1.1) Если значение ключа i больше или равно 2, то верни True.
# 3) Если строка s НЕ равна строке goal,
# 3.1) Пройдись циклом по диапазону длины строки s, запиши ключ i со значением i увеличеным на 1 в словарь dict2.
# 3.2) Пройдись циклом по диапазону длины строки goal,
# 3.2.1) Если ключ goal[i] есть в словаре dict2,
# 3.2.1.1) То уменьшь значение ключа goal[i] на 1.
# 3.2.1.2) Если значение ключа goal[i] из словаря dict2 равно 0, то удали этот ключ из словаря dict2.
# 3.3) Если словарь dict2 не пустой, то верни False.
# 3.4) Проходимся циклом по диапазону длины строки s,
# 3.4.1) Если i из строки s не равна i из строки goal, то увеличь значение переменой result на 1.
# 3.5) Верни равна ли переменная result =2

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

# s = "ab"
# goal = "ba"
#
# def buddyStrings(s, goal):
#     dict1 = {}
#     dict2 = {}
#     result = 0
#
#     if len(s) != len(goal):
#         return False
#
#     elif s == goal:
#         for i in s:
#             dict1[i] = dict1.get(i, 0) + 1
#             if dict1[i] >= 2:
#                 # {'a': 2}
#                 return True
#
#     elif s != goal:
#         for i in range(len(s)):
#             dict2[s[i]] = dict2.get(s[i], 0) + 1
#
#         for i in range(len(goal)):
#             if goal[i] in dict2:
#                 dict2[goal[i]] -= 1
#                 if dict2[goal[i]] == 0:
#                     del dict2[goal[i]]
#
#         if dict2 != {}:
#             return False
#
#         for i in range(len(s)):
#             if s[i] != goal[i]:
#                 result += 1
#
#         return result == 2
#
# buddyStrings(s, goal)


### Без  хэша таблицы (Не рабочие !!!)!!! ###

# Сложность:
# 1) Время O(n)
# 2) Память O(1)
#
# s = "ab"
# goal = "ba"
#
# def buddyStrings(s, goal):
#     result = []
#
#     for a, b in zip(s, goal):
#         if a != b:
#             result.append(a + b)
#
#         if len(result) > 2:
#             return False
#
#     if len(result) == 2 and result[0] == result[1][::-1]:
#         return True
#     else:
#         return False
#
# buddyStrings(s, goal)
