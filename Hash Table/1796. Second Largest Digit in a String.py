### Условие задачи:
# Учитывая буквенно-цифровую строку s, верните вторую по величине числовую цифру, которая встречается в s,
# или -1 если она не существует.
# Буквенно - цифровая строка — это строка, состоящая из строчных английских букв и цифр.

# Example 1:
# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

# Example 2:
# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit.

### Краткое условие:
# Необходимо вернуть вторую по величине числовую цифру, которая встречается в строке,
# или -1, если такой цифры не существует.

### Хэш сет !!! ###

# Краткое объяснение решение задачи:
# Добавляем только числа из строки s в множество,
# если в множестве больше одного числа, возвращает второе по величине число;
# иначе возвращает -1.

# Полное объяснение решение задачи:
# 0) Создаем пустой словарь dictSet.
# 1) Проходимся циклом по строке s,
# 1.1) Если i это число, то добавь это число в словарь dictSet.
# 2) Если длина словаря dictSet больше 1, то верни пред последний элемент массива dictSet.
# 3) Иначе, верни -1.

# Сложность:
# 1) Время O(n)  (n + k log k)
# 2) Память O(1) (k)

s = "dfa12321afd"

def secondHighest(s):
    dictSet = set()

    for i in s:
        if i.isdigit():
            dictSet.add(int(i))
    # {1, 2, 3}
    if len(dictSet) > 1:
        return sorted(list(dictSet))[-2]  # {1, 2, 3} - > [1,2,3] -> 2
    else:
        return -1

secondHighest(s)

assert secondHighest(s="dfa12321afd") == 2
assert secondHighest(s="abc1111") == -1
# Доп юнитесты для проверки некоторых условий:
assert secondHighest(s="11111") == -1  # Все цифры одинаковые
assert secondHighest(s="a1b2c3") == 2  # Две разные цифры
assert secondHighest(s="9abc8def7") == 8  # Цифры в начале и конце строки
assert secondHighest(s="!@#456*()") == 5  # Смешанные символы
assert secondHighest(s="a5") == -1  # Только одна цифра:

### Хэш таблицы ###

# Полное объяснение решение задачи:
# 0) Создаем пустой массив result.
# 1) Проходимся циклом по строке s,
# 1.1) Если i число, то добавь его в массив result.
# 2) Если длина массива result равна 0, то верни -1.
# 3) Создаем словарь dict с set(result).
# 4) Убираем максимально число из словаря dict.
# 5) Преобразовываем словарь dict в массив.
# 6) Если длина массива dict больше 0, то верни максимальный элемент из массива dict.
# 7) Если длина массива dict НЕ больше 0, то верни -1.
#
# Сложность:
# 1) Время O(n)
# 2) Память O(1)
#
# s = "dfa12321afd"
#
# def secondHighest(s):
#     result = []
#
#     for i in s:  # Избавляемся в строке s от букв и добавляем числа из строки s в массив result
#         if i.isdigit():
#             result.append(int(i))
#     # [1, 2, 3, 2, 1]
#     if len(result) == 0:
#         return -1
#
#     dict = set(result)  # {1, 2, 3}
#     dict.remove(max(dict))  # {1, 2}
#     dict = list(dict)  # [1, 2]
#
#     if len(dict) > 0:
#         return max(dict)  # 2
#     else:
#         return -1
#
# secondHighest(s)
