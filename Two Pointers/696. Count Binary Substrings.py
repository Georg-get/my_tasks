### Условие задачи:
# Учитывая двоичную строку s, верните количество непустых подстрок, которые имеют одинаковое количество 0 «s» и 1 «s»,
# а все 0 «s» и все 1 «s» в этих подстроках группируются последовательно.
# Подстроки, встречающиеся несколько раз, учитываются столько раз, сколько они встречаются.

# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

# Example 2:
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

                                        ### Добавить в список !

### Краткое условие:
# Вернуть число подстрок, которых можно собрать в строке s.

# Алгоритм решение задачи:
# 0) Создаем переменные left, right, result со значением 0.
# 1) Проходимся циклом ваил пока left не станет меньше длины строки s,
# 1.1) Проходимся циклом ваил пока right не станет меньше длины строки s и буква где установлен левый указатель равна буква где установлен правый указатель,
# 1.1.1) Увеличиваем значенеие переменную right на 1.
# 1.2) Создаем переменную k со значением right.
# 1.3) Проходимся циклом ваил пока k не станет меньше длины строки s и буква где установлен левый указатель равна буква где установлен k указатель,
# 1.3.1) Увеличиваем значенеие переменную k на 1.
# 1.4) Увеличиваем значение переменной result на минимальное значение (right - left, k - right).
# 1.5) Присваеваем переменой left значение переменой right.
# 2) Вернуть переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

s = "00110011"

def countBinarySubstrings(s):
    left = 0
    right = 0
    result = 0

    while left < len(s):

        while right < len(s) and s[left] == s[right]:
            right += 1

        k = right

        while k < len(s) and s[right] == s[k]:
            k += 1

        result += min(right - left, k - right)
        left = right

    return result # 6

countBinarySubstrings(s)

assert countBinarySubstrings(s="00110011") == 6
assert countBinarySubstrings(s="10101") == 4