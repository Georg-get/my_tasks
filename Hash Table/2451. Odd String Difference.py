### Условие задачи:
# Вам дан массив строк одинаковой длины words. Предположим, что длина каждой строки равна n.
# Каждую строку words[i]можно преобразовать в разностный целочисленный массив difference[i]
# длины n - 1где difference[i][j] = words[i][j+1] - words[i][j]где 0 <= j <= n - 2.
# Обратите внимание, что разница между двумя буквами — это разница между их позициями в алфавите, то есть позициями 'a'is 0, 'b'is 1и 'z'is 25.
# Например, для строки "acb"массив целочисленных разностей равен [2 - 0, 1 - 2] = [2, -1].
# Все строки в словах имеют одинаковый массив разностных целых чисел, кроме одной . Вы должны найти эту строку.
# Возвращает строку, в words которой имеется массив различных целых чисел .

# Example 1:
# Input: words = ["adc","wzy","abc"]
# Output: "abc"
# Explanation:
# - The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
# - The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
# - The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
# The odd array out is [1, 1], so we return the corresponding string, "abc".

# Example 2:
# Input: words = ["aaa","bob","ccc","ddd"]
# Output: "bob"
# Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].

                                            ### Добавить в список !
### Краткое условие:
# Возвращает строку, в words которой имеется массив различных целых чисел.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по массиву words,
# 1.1) Создаем пустой массив diff,
# 1.2) Продимся циклом по диапазону от 1 до длины i, добавляем в массив diff число уникод (i[j]) - уникод ord(i[j - 1]).
# 1.3) Преобразовываем переменную diff в кортедж.
# 1.4) Если diff нету в словаре dict, то добавь diff как ключ со значением i.
# 1.5) Если diff есть в словаре dict, то добавь diff как ключ со значением None.
# 2) Проходимся циклом по словарю dict, если v не равно None, то верни v.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

words = ["adc", "wzy", "abc"]

def oddString(words):
    dict = {}

    for i in words:
        diff = []
        for j in range(1, len(i)):
            #               100   -  97
            diff.append(ord(i[j]) - ord(i[j - 1]))
        # [3, -1]
        diff = tuple(diff)
        # (3, -1)
        if diff not in dict:
            dict[diff] = i
        else:
            dict[diff] = None  # {(3, -1): 'adc'}
    # {(3, -1): None, (1, 1): 'abc'}
    for k, v in dict.items():
        if v is not None:
            return v  # abc

oddString(words)

assert oddString(words=["adc", "wzy", "abc"]) == "abc"
assert oddString(words=["aaa", "bob", "ccc", "ddd"]) == "bob"