### Условие задачи:
# Учитывая строку s и символ c, который встречается в s, верните массив целых чисел answer,
# где answer.length == s.length и answer[i]— расстояние от индекса i до ближайшего вхождения символа c вs.
# Расстояние между двумя индексами i и j равно abs(i - j), где abs– функция абсолютного значения.

# Example 1:
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

# Example 2:
# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]

                                                    ### Добавить в список !

### Краткое условие:
# Вернуть массив с расстоянием между двумя индексами i и j равно abs(i - j), где abs– функция абсолютного значения.

# Алгоритм решение задачи:
# 0) Создаем переменные left со значением 0 и right со значением 0, и массив "*" колличество длины строки s.
# 1) Проходимся циклом ваил пока left не станет меньше длины строки s и right не станет меньше длины строки s,
# 1.1) Если буква где находиться левый указатель равна букве где находиться правый указатель равна строке c,
# 1.1.1) То result[left] равно 0, и увеличь переменную left на 1 и увеличь переменную right на 1.
# 1.2) Если буква где находиться левый указатель НЕ равна букве где находиться правый указатель равна строке c,
# 1.2.1) То result[left] равно абсолютное значение числа left - right, и увеличь переменную left на 1.
# 1.3) Если буква где находиться левый указатель НЕ равна букве где находиться правый указатель НЕ равна строке c,
# 1.3.1) То увеличь переменную right на 1.
# 2) Создаем переменные left со значением длины строки s-1 и right со значением длины строки s-1.
# 3) Проходимся циклом ваил пока left не станет больше или рано 0 и right не станет больше или рано 0,
# 3.1) Если буква где находиться левый указатель равна букве где находиться правый указатель равна строке c,
# 3.1.1) То result[left] равно 0, и уменьши переменную left на 1 и уменьши переменную right на 1.
# 3.2) Если буква где находиться левый указатель НЕ равна букве где находиться правый указатель равна строке c,
# 3.2.1) Если result[left] это число, то result[left] ранво мигнимальному значениею из (result[left], abs(left - right)).
# 3.2.2) Если result[left] это НЕ число,то result[left] равно абсолютное значение числа left - right.
# 3.2.3) Уменьши значение переменой left на 1.
# 3.3) Если буква где находиться левый указатель НЕ равна букве где находиться правый указатель НЕ равна строке c, то уменьши значение переменой right на 1.
# 4) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

s = "loveleetcode"
c = "e"

def shortestToChar(s, c):
    left = 0
    right = 0
    result = ["*"] * len(s)

    while left < len(s) and right < len(s):
        if s[left] == s[right] == c:
            result[left] = 0
            left += 1
            right += 1

        elif s[left] != c and s[right] == c:
            result[left] = abs(left - right)
            left += 1

        elif s[left] != c and s[right] != c:
            right += 1
    # [3, 2, 1, 0, 1, 0, 0, 4, 3, 2, 1, 0]
    left = len(s) - 1
    right = len(s) - 1

    while left >= 0 and right >= 0:
        if s[left] == s[right] == c:
            result[left] = 0
            left -= 1
            right -= 1

        elif s[left] != c and s[right] == c:
            if type(result[left]) == int:
                result[left] = min(result[left], abs(left - right))

            else:
                result[left] = abs(left - right)
            left -= 1

        elif s[left] != c and s[right] != c:
            right -= 1
    # [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    return result

shortestToChar(s, c)

assert shortestToChar(s="loveleetcode", c="e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
assert shortestToChar(s="aaab", c="b") == [3, 2, 1, 0]


# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         a=[]
#         b=[]
#         for i in range(len(s)):
#             if s[i]==c:
#                 a.append(i)
#         for i in range(len(s)):
#             c=[]
#             for j in a:
#                 c.append(abs(i-j))
#             b.append(min(c))
#         return b