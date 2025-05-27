### Условие задачи:
# Вам дано целое число n.
# Каждое число от 1 до n группируется по сумме его цифр.
# Возвращает количество групп с наибольшим размером.

# Example 1:
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.

# Example 2:
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.

### Краткое условие:
# Вернуть число количество групп с наибольшим размером.

# Алгоритм решение задачи:
# 0) Создаем: две переменные maxValueInDict и count со значением 0, и пустой словарь dict.
# 1) Проходимся циклом по диапазону ( от 1 до n+1),
# 1.1) Создаем строку stringI со значением i.
# 1.1) Создаем переменную sumI со значением 0.
# 1.2) Проходимся циклом по строке stringI, увеличиваем переменную sumI на число j.
# 1.3) Если ключа sumI нету в словаре dict, то добавь ключ sumI со значением 1 в словарь dict.
# 1.4) Иначе, увеличь значение ключа sumI на 1.
# 2) Проходимся циклом по словарю dict, увеличиваем переменную maxValueInDict на самую большое значение ключа в словаре dict.
# 3) Проходимся циклом по словарю dict, если значение ключа i равно переменой maxValueInDict, то увеличь значение переменой count на 1.
# 4) Вернуть переменную count.

# Сложность:
# 1) Время O(n) O(n*log(n))
# 2) Память O(n)

n = 13

def countLargestGroup(n):
    maxValueInDict = 0
    count = 0
    dict = {}

    for i in range(1, n + 1, 1):  # range(1, 14)
        stringI = str(i)
        sumI = 0

        for j in stringI:
            sumI += int(j)

        if sumI not in dict.keys():
            dict[sumI] = 1
        else:
            dict[sumI] += 1
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    for i in dict:
        maxValueInDict = max(maxValueInDict, dict[i])
    # maxValueInDict = 2
    for i in dict:
        if dict[i] == maxValueInDict:
            count += 1
    #       4       (в словаре dict всего четыре ключа со значением 2)
    return count

countLargestGroup(n)

assert countLargestGroup(n=13) == 4
assert countLargestGroup(n=2) == 2