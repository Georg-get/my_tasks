### Условие задачи:
# Вам дан целочисленный массив deck, где deck[i] представляет собой число, написанное на карточке.ith
# Разделите карточки на одну или несколько групп таким образом, чтобы:
# В каждой группе есть ровно x карточки, где x > 1, и
# На всех карточках одной группы написано одно и то же целое число.
# Возврат true, если такое разделение возможно, или false в противном случае.

# Example 1:
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

# Example 2:
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.

### Краткое условие:
# Вернуть true если в массиве deck есть числа с одной парой, иначе false.

# Краткое объяснение решение задачи:
# 1. Создаем словарь для подсчета пар в колоде.
# 2. Для каждой карты в deck он увеличивает счетчик в словаре. В результате получается словарь,
# где ключи — это значения карт, а значения — их количество.
# 3. Затем используем функцию math.gcd для нахождения наибольшего общего делителя (НОД) всех значений в словаре.
# Если НОД больше 1, это означает, что карты можно разбить на группы одинакового размера (больше 1).
# 4. Если НОД больше 1, функция возвращает True, иначе — False.

# Полное объяснение решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по массиву deck,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Если ключ i НЕТу в словаре dict, то добавь ключа i со значением 1 в словарь dict.
# 2) Если все значение в словаре dict их НОД (наибольший общий делитель) не равен 1, то верни True.
# 3) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n) (k)

import math

deck = [1, 2, 3, 4, 4, 3, 2, 1]

def hasGroupsSizeX(deck):
    dict = {}

    for i in deck:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {1: 2, 2: 2, 3: 2, 4: 2}
            # 2                 != 1
    if math.gcd(*dict.values()) != 1: # {1: 2, 2: 2, 3: 2, 4: 2} -> ([2,2,2,2]) -> (2,2,2,2) -> 2
        return True
    else:
        return False

hasGroupsSizeX(deck)

assert hasGroupsSizeX(deck=[1, 2, 3, 4, 4, 3, 2, 1]) == True
assert hasGroupsSizeX(deck=[1, 1, 1, 2, 2, 2, 3, 3]) == False
# Доп юнитесты для проверки некоторых условий:
assert hasGroupsSizeX(deck=[1, 1]) == True # Тест с минимальным размером колоды
assert hasGroupsSizeX(deck = [1, 1, 1, 2, 2]) == False # Тест с разными значениями карт

### Решение без библиотеки math !!!

# deck = [1, 2, 3, 4, 4, 3, 2, 1]
#
# def hasGroupsSizeX(deck):
#     def gcd(a, b):
#         while b:
#             a, b = b, a % b
#         return a
#
#     dict = {}
#
#     for i in deck:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     # {1: 2, 2: 2, 3: 2, 4: 2}
#             # 2                 != 1
#     counts = list(dict.values()) # [2,2,2,2]
#
#     current_gcd = counts[0] # 2
#     for count in counts[1:]: # [2, 2, 2]
#         current_gcd = gcd(current_gcd, count)
#         if current_gcd == 1:
#             return False
#
#     if current_gcd != 1:
#         return True
#     else:
#         return False
#
# hasGroupsSizeX(deck)