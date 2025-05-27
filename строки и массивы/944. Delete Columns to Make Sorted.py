### Условие задачи:
# Вам дан массив n строк strs одинаковой длины.
# Строки можно расположить так, чтобы в каждой строке было по одной, образуя сетку.
#
# Например, strs = ["abc", "bce", "cae"]можно организовать следующим образом:
# абв
# до нашей эры
# ЦЕ
# Вы хотите удалить столбцы, которые не отсортированы лексикографически . В приведенном выше примере ( с индексом 0 )
# столбцы 0 ( 'a', 'b', 'c') и 2 ( 'c', 'e', 'e') сортируются, а столбец 1 ( 'b', 'c', 'a') — нет, поэтому вы должны удалить столбец 1.
# Возвращает количество столбцов, которые вы удалите .

# Example 1:
# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

# Example 2:
# Input: strs = ["a","b"]
# Output: 0
# Explanation: The grid looks as follows:
#   a
#   b
# Column 0 is the only column and is sorted, so you will not delete any columns.

# Example 3:
# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# Explanation: The grid looks as follows:
#   zyx
#   wvu
#   tsr
# All 3 columns are not sorted, so you will delete all 3.

### Краткое условие:
# Возвращает количество столбцов, которые вы удалите.

# Алгоритм решение задачи:
# 0) Создаем две переменные result и count, со значением 0.
# 1) Проходимся циклом по диапазону от 0 до длины первой строки из массив strs,
# 1.1) Создаем пустую строку string,
# 1.2) Проходимся циклом по диапазону от 0 до длины массива strs, добавляем в string первые буквы из слов массива strs.
# 1.3) Если массив string НЕ РАВЕН отсортированой строке string, то увелись result на 1.
# 1.4) Увелись переменную count на 1.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n * m)
# 2) Память O(n * m)

strs = ["cba", "daf", "ghi"]

def minDeletionSize(strs):
    result = 0
    count = 0

    for i in range(len(strs[0])): # range (0,3)
        string = ''
        for j in range(len(strs)): # range (0,3)
            string += strs[j][count] # cdg bah afi

        if list(string) != sorted(string):
            result += 1

        count += 1

    return result # 1

minDeletionSize(strs)

assert minDeletionSize(strs=["cba", "daf", "ghi"]) == 1
assert minDeletionSize(strs=["a", "b"]) == 0
assert minDeletionSize(strs=["zyx", "wvu", "tsr"]) == 3