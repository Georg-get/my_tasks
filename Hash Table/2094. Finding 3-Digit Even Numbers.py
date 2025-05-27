### Условие задачи:
# Вам дан целочисленный массив digits, где каждый элемент представляет собой цифру.
# Массив может содержать дубликаты.
# Вам нужно найти все уникальные целые числа, соответствующие заданным требованиям:
# Целое число состоит из объединения трех элементов из в любом произвольном порядке.digits
# Целое число не имеет ведущих нулей.
# Целое число четное.
# Например, если заданы digits целые [1, 2, 3]числа 132 и 312 соответствуют требованиям.
# Возвращает отсортированный массив уникальных целых чисел.

# Example 1:
# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]
# Explanation: All the possible integers that follow the requirements are in the output array.
# Notice that there are no odd integers or integers with leading zeros.

# Example 2:
# Input: digits = [2,2,8,8,2]
# Output: [222,228,282,288,822,828,882]
# Explanation: The same digit can be used as many times as it appears in digits.
# In this example, the digit 8 is used twice each time in 288, 828, and 882.

# Example 3:
# Input: digits = [3,7,5]
# Output: []
# Explanation: No even integers can be formed using the given digits.

                                                ### Добавить в список !

### Краткое условие:
# Надо взять число из массива digits и собрать массив трезначных числел из массива digits.

# Алгоритм решение задачи:
# 0) Создаем словарь setDigits с set.
# 1) Затем происходит перебор всех возможных упорядоченных троек из цифр списка digits
# с помощью метода permutations() из модуля itertools.
# 1.1) Если x не равен 0 и z является четным, о трехзначное число, составленное из этих цифр, добавляется в множество setDigits.
# 2) Вернуть отсортированый словарь setDigits.

# Сложность:
# 1) Время O(n^3)) (n!)
# 2) Память O(n)

### Сложная задача !!!

from itertools import permutations

digits = [2, 1, 3, 0]

def findEvenNumbers(digits):
    setDigits = set()

    for x, y, z in permutations(digits, 3):
        if x != 0 and z & 1 == 0:
            setDigits.add(100 * x + 10 * y + z)
    # {320, 130, 312, 132, 230, 102, 302, 210, 310, 120}
    return sorted(setDigits)

findEvenNumbers(digits)

assert findEvenNumbers(digits=[2, 1, 3, 0]) == [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
assert findEvenNumbers(digits=[2, 2, 8, 8, 2]) == [222, 228, 282, 288, 822, 828, 882]
assert findEvenNumbers(digits=[3, 7, 5]) == []