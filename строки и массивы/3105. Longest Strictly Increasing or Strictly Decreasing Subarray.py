### Условие задачи:
# Вам дан массив целых чисел nums.
# Верните длину самого длинного подмассив из nums которых либо строго увеличивается или строго убывающий.

# Example 1:
# Input: nums = [1,4,3,3,2]
# Output: 2
# Explanation:
# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
# Hence, we return 2.

# Example 2:
# Input: nums = [3,3,3,3]
# Output: 1
# Explanation:
# The strictly increasing subarrays of nums are [3], [3], [3], and [3].
# The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
# Hence, we return 1.

# Example 3:
# Input: nums = [3,2,1]
# Output: 3
# Explanation:
# The strictly increasing subarrays of nums are [3], [2], and [1].
# The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
# Hence, we return 3.

### Краткое условие:
# Верните длину самого длинного подмассив из nums которых либо строго увеличивается или строго убывающий.

# Алгоритм решение задачи:
# 0) Создаем переменные: incr, decr, result со значением 1 , и firstElementOfArrayNums со значнеием первый элемент массива nums.
# 1) Проходимся циклом по массиву nums,
# 1.1) incr = incr * (i > firstElementOfArrayNums) + 1 ,
# 1.2) decr = decr * (i < firstElementOfArrayNums) + 1 ,
# 1.3) firstElementOfArrayNums = i ,
# 1.4) result = максимальному числу из result, incr, decr.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [1, 4, 3, 3, 2]

def longestMonotonicSubarray(nums):
    incr = 1
    decr = 1
    result = 1
    firstElementOfArrayNums = nums.pop(0)  # 1

    for i in nums:
        incr = incr * (i > firstElementOfArrayNums) + 1
        decr = decr * (i < firstElementOfArrayNums) + 1
        firstElementOfArrayNums = i

        result = max(result, incr, decr)

    return result

longestMonotonicSubarray(nums)

assert longestMonotonicSubarray(nums=[1, 4, 3, 3, 2]) == 2
assert longestMonotonicSubarray(nums=[3, 3, 3, 3]) == 1
assert longestMonotonicSubarray(nums=[3, 2, 1]) == 3