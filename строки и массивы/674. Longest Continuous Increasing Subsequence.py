### Условие задачи:
# Дан несортированный массив целых чисел nums, вернуть длину самой длинной непрерывной возрастающей подпоследовательности (т.е. подмассива) .
# Подпоследовательность должна быть строго возрастающей.
# Непрерывная возрастающая подпоследовательность определяется двумя индексами lи r( l < r), такими,
# что она равна [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]и для каждого l <= i < r, nums[i] < nums[i + 1].

# Example 1:
# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element 4.

# Example 2:
# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
# increasing.

### Краткое условие:
# Вернуть длину под массива.

# Алгоритм решение задачи:
# 0) Создаем массив stack с первым элементом массив nums, и result равное 1.
# 1) Проходимся циклом по диапазону от 1 до длины массива nums,
# 1.1) Если длина массива stack больше 0 и последний элемент массив stack равен или больше i, то очисти массив stack.
# 1.2) В массив stack добавляем i,
# 1.3) result делаем значнеие максивального числа из result и длины массива stack.
# 2) Вернуть result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 3, 5, 4, 7]

def findLengthOfLCIS(nums):
    stack = [nums[0]]
    result = 1

    for i in range(1, len(nums)):

        if len(stack) > 0 and stack[-1] >= nums[i]:
            stack.clear()

        stack.append(nums[i])
        result = max(result, len(stack))

    return result

findLengthOfLCIS(nums)

assert findLengthOfLCIS(nums=[1, 3, 5, 4, 7]) == 3
assert findLengthOfLCIS(nums=[2, 2, 2, 2, 2]) == 1
