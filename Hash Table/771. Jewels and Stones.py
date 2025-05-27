### Условие задачи:
# Вам даны строки jewels, представляющие типы камней,
# которые являются драгоценными камнями, и stones камни, которые у вас есть.
# Каждый персонаж stones — это тип камня, который у вас есть.
# Вы хотите знать, сколько камней у вас тоже являются драгоценностями.
# Буквы чувствительны к регистру, поэтому "a" считается камнем, отличным от "A".

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

### Краткое условие:
# Надо найти пары двух одинаковых букв в двух строках jewels и stones. Вернуть число похожих пар букв.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по строке jewels.
# 1.1) Если ключ НЕ совпадает с i в словаре dict, то добавь его как ключ со значением 0.
# 2) Проходимся циклом по строке stones.
# 2.1) Если ключ совпадает с j в словаре dict, то увеличь его значение на 1.
# 3) верни сумму всех значений в словаре dict.

# Сложность:
# 1) Время O(m) (m + n)
# 2) Память O(m)

jewels = "aA"
stones = "aAAbbbb"

def numJewelsInStones(jewels, stones):
    dict = {}

    for i in jewels:
        if i not in dict:
            dict[i] = 0
    # {a:0, A:0}

    for j in stones:
        if j in dict:
            dict[j] += 1
    # {a:1, A:2}

    return sum(dict.values())

numJewelsInStones(jewels, stones)

assert numJewelsInStones(jewels="aA", stones="aAAbbbb") == 3
assert numJewelsInStones(jewels="z", stones="ZZ") == 0