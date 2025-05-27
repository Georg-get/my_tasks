### Условие задачи:
# Учитывая целочисленный массив nums размера n, вернуть число со значением, наиболее близким к 0.nums
# Если существует несколько ответов, вернуть число с наибольшим значением.

# Example 1:
# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.

# Example 2:
# Input: nums = [2,-1,1]
# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

### Краткое условие:
# Учитывая целочисленный массив nums размера n, вернуть число со значением, наиболее близким к 0 nums.

# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 999999999.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если i меньше result или i равна result, то result равна i.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [-4, -2, 1, 4, 8]

def findClosestNumber(nums):
    result = 999999999

    for i in nums:
        if abs(i) < abs(result) or i == abs(result): # abs используется для вычисления абсолютного значения числа, то есть его значения без учета знака.
            result = i

    return result

findClosestNumber(nums)

assert findClosestNumber(nums=[-4, -2, 1, 4, 8]) == 1
assert findClosestNumber(nums=[2, -1, 1]) == 1