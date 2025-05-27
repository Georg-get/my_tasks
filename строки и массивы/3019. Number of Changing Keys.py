### Условие задачи:
# Вам предоставляется строка с индексом 0,s набранная пользователем. Изменение ключа определяется как использование ключа,
# отличного от последнего использованного ключа. Например, s = "ab"есть смена ключа, а s = "bBBb"ее нет.
# Возвращает количество раз, когда пользователю пришлось сменить ключ.
# Примечание. Модификаторы типа shift или caps lock не будут учитываться при смене ключа, то есть,
# если пользователь набрал букву 'a', а затем букву 'A', то это не будет рассматриваться как смена ключа.

# Example 1:
# Input: s = "aAbBcC"
# Output: 2
# Explanation:
# From s[0] = 'a' to s[1] = 'A', there is no change of key as caps lock or shift is not counted.
# From s[1] = 'A' to s[2] = 'b', there is a change of key.
# From s[2] = 'b' to s[3] = 'B', there is no change of key as caps lock or shift is not counted.
# From s[3] = 'B' to s[4] = 'c', there is a change of key.
# From s[4] = 'c' to s[5] = 'C', there is no change of key as caps lock or shift is not counted.

# Example 2:
# Input: s = "AaAaAaaA"
# Output: 0
# Explanation: There is no change of key since only the letters 'a' and 'A' are pressed which does not require change of key.

### Краткое условие:
# Возвращает количество раз, когда пользователю пришлось сменить ключ.

# Алгоритм решение задачи:
# 0) Создаем строку lowerS со значением маленьких букв из строки s и переменную result со значением 0.
# 1) Проходимся циклом по диапазону от 1 до длины строки lowerS,
# 1.1) Если буква где стоит i не равна букве которая перед i, то увеличиваем переменную result на 1.
# 2) Вернуть число result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "aAbBcC"

def countKeyChanges(s):
    lowerS = s.lower() # aabbcc
    result = 0

    for i in range(1, len(lowerS)): # range(1, 6)
        if lowerS[i] != lowerS[i - 1]: # a b # b c
            result += 1

    return result

countKeyChanges(s)

assert countKeyChanges(s="aAbBcC") == 2
assert countKeyChanges(s="AaAaAaaA") == 0