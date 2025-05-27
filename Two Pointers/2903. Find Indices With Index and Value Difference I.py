### Условие задачи:
# Вам дан целочисленный массив с нулевым индексом, nums имеющий длину n,
# целое число indexDifference и целое число valueDifference.
# Ваша задача — найти два индекса i и j оба в диапазоне [0, n - 1], которые удовлетворяют следующим условиям:
# abs(i - j) >= indexDifference, и
# abs(nums[i] - nums[j]) >= valueDifference
# Возвращает целочисленный массив answer , где answer = [i, j] таких индексов два , и answer = [-1, -1] в противном случае .
# Если для двух индексов есть несколько вариантов, верните любой из них .
# Примечание: i и j может быть равно .

# Example 1:
# Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
# Output: [0,3]
# Explanation: In this example, i = 0 and j = 3 can be selected. abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
# Hence, a valid answer is [0,3]. [3,0] is also a valid answer.

# Example 2:
# Input: nums = [2,1], indexDifference = 0, valueDifference = 0
# Output: [0,0]
# Explanation: In this example, i = 0 and j = 0 can be selected. abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
# Hence, a valid answer is [0,0]. Other valid answers are [0,1], [1,0], and [1,1].

# Example 3:
# Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
# Output: [-1,-1]
# Explanation: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
# Hence, [-1,-1] is returned.

                                        ### Добавить в список !

### Краткое условие:
# Найти два индекса i и j оба в диапазоне [0, n - 1], которые удовлетворяют.

# Алгоритм решение задачи:
# 0) Создаем переменные left со значением 0 и right со значением indexDifference.
# 1) Проходимся циклом ваид пока left не станет меньше длины массива nums - indexDifference,
# 1.1) Если абсолютное значение вырожение nums[right] - nums[left] больше или равно valueDifference, то верни [left, right].
# 1.2) Если НЕТ абсолютное значение вырожение nums[right] - nums[left] больше или равно valueDifference, то увеличь переменную right на 1.
# 1.3) Если right равно длине массива nums -1, то увеличь переменную left на 1, и присвой переменой right значение left + indexDifference.
# 2) Верни [-1,1].

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

nums = [5, 1, 4, 1]
indexDifference = 2
valueDifference = 4

def findIndices(nums, indexDifference, valueDifference):
    left = 0
    right = indexDifference # 2
    # valueDifference = 4

    while left < len(nums) - indexDifference:

        if abs(nums[right] - nums[left]) >= valueDifference:
            #      [0   ,     3]
            return [left, right]

        elif not (abs(nums[right] - nums[left]) >= valueDifference) and right < len(nums) - 1:
            right += 1

        elif right == len(nums) - 1:
            left += 1
            right = left + indexDifference

    return [-1, -1]

findIndices(nums, indexDifference, valueDifference)

assert findIndices(nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4) == [0, 3]
assert findIndices(nums=[2, 1], indexDifference=0, valueDifference=0) == [0, 0]
assert findIndices(nums=[1, 2, 3], indexDifference=2, valueDifference=4) == [-1, -1]