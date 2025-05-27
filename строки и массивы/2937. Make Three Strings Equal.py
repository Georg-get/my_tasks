### Условие задачи:
# Вам даны три строки: s1, s2, и s3.
# За одну операцию вы можете выбрать одну из этих строк и удалить ее самый правый символ.
# Обратите внимание, что вы не можете полностью очистить строку.
# Верните минимальное количество операций, необходимых для того, чтобы сделать строки равными.
# Если сделать их равными невозможно, верните -1.

# Example 1:
# Input: s1 = "abc", s2 = "abb", s3 = "ab"
# Output: 2
# Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal strings.

# Example 2:
# Input: s1 = "dac", s2 = "bac", s3 = "cac"
# Output: -1
# Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.

### Краткое условие:
# Верните минимальное количество операций, необходимых для того, чтобы сделать строки равными.
# Если сделать их равными невозможно, верните -1.

# Алгоритм решение задачи:
# 0) Если первая буква в стороках: s1 s2 s3 не одинаковые то верни -1.
# 1) Создаем переменные:
# 1.1) s1Len со значением длины строки s1.
# 1.2) s2Len со значением длины строки s2.
# 1.3) s3Len со значением длины строки s3.
# 1.4) minLen со значением минимальной длины строки из s1,s2,s3.
# 1.5) result со значением s1Len + s2Len + s3Len.
# 2) Проходимся циклом по диапазону от 0 до minLen,
# 2.1) Если i в строке s1 равна i в строке s2 равна i в строке s3, уменьши result на 3.
# 2.2) Если i в строке s1 НЕ равна i в строке s2 НЕ равна i в строке s3, то выйди из цикла.
# 3) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s1 = "abc"
s2 = "abb"
s3 = "ab"


def findMinimumOperations(s1, s2, s3):
    if not s1[0] == s2[0] == s3[0]:
        return -1

    s1Len = len(s1)
    s2Len = len(s2)
    s3Len = len(s3)
    minLen = min(s1Len, s2Len, s3Len)
    result = s1Len + s2Len + s3Len

    for i in range(minLen):

        if s1[i] == s2[i] == s3[i]:
            result -= 3
        else:
            break

    return result


findMinimumOperations(s1, s2, s3)

assert findMinimumOperations(s1="abc", s2="abb", s3="ab") == 2
assert findMinimumOperations(s1="dac", s2="bac", s3="cac") == -1
