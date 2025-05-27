### Условие задачи:
# Дан массив целых чисел nums, вернуть третье отличное максимальное число в этом массиве.
# Если третьего максимума не существует, вернуть максимальное число.

# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

### Краткое условие:
# Дан массив целых чисел nums, вернуть третье отличное максимальное число в этом массиве.
# Если третьего максимума не существует, вернуть максимальное число.

# Полное объяснение решение задачи:
# 0) Убираем дубликаты из массива nums и сортируем массив по возростанию nums.
# 1) Если длина массива nums больше или равна 3, то верни число третье с конца массива nums.
# 2) Иначе, то верни число последнее число в массиве nums.

# Сложность:
# 1) Время O(n + m)
# 2) Память O(n)

nums = [3, 2, 1]

def thirdMax(nums):
    nums = sorted(list(set(nums)))  # [1, 2, 3]

    if len(nums) >= 3:
        return nums[-3] # от 4 юнитеста защита !!!
    else:
        return nums[-1]

thirdMax(nums)

assert thirdMax(nums=[3, 2, 1]) == 1
assert thirdMax(nums=[1, 2]) == 2
assert thirdMax(nums=[2, 2, 3, 1]) == 1
assert thirdMax(nums=[1, 2, 2, 5, 3, 5]) == 2 # этот тест !!!