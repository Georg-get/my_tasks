### Условие задачи:
# Вам дан двумерный целочисленный массив ranges, два целых числа left и right.
# Каждый представляет собой инклюзивный интервал между и .ranges[i] = [starti, endi]startiendi
# Возвращает значение true , если каждое целое число во включенном диапазоне [left, right] покрыто хотя бы одним интервалом в ranges .
# Возврат false в противном случае . Целое число xпокрывается интервалом, если .ranges[i] = [starti, endi]starti <= x <= endi

# Example 1:
# Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
# Output: true
# Explanation: Every integer between 2 and 5 is covered:
# - 2 is covered by the first range.
# - 3 and 4 are covered by the second range.
# - 5 is covered by the third range.

# Example 2:
# Input: ranges = [[1,10],[10,20]], left = 21, right = 21
# Output: false
# Explanation: 21 is not covered by any range.

### Краткое условие:
# Надо вернуть True если числа left и right есть в матрице ranges, если этих чисел нету в матрице ranges то вернуть False.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по матрице ranges,
# 1.1) Проходимся циклом по элементам матрицы ranges с диапазоном (от i[0] до i[1]+1), добавляем ключ j со значением 1 в словарь dict.
# 2) Проходимся циклом по диапазону от left до right+1,
# 2.1) Если i НЕТу в словаре dict, то вернуть False.
# 3) Вернуть True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

ranges = [[25, 42], [7, 14], [2, 32], [25, 28], [39, 49], [1, 50], [29, 45], [18, 47]]
left = 15
right = 38

def isCovered(ranges, left, right):
    dict = {}

    for i in ranges:
        for j in range(i[0], i[1] + 1):
            dict[j] = 1
    # {25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 1: 1, 50: 1}
    for i in range(left, right + 1):  # range(15, 39)
        if i not in dict:
            return False

    return True

isCovered(ranges, left, right)