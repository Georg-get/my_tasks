### Условие задачи:
# Дан массив целых чисел nums, найти три числа, произведение которых максимально, и вернуть максимальное произведение.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24

# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6

### Краткое условие:
# Вернуть максимальное произведение.

# Полное объяснение решение задачи:
# 0) Сортируем массив nums.
# 1) Считаем left из умножение последнего и предпоследнего и пред последнего элемента массива nums.
# 2) Считаем right из умножение первного и второго и последнего элемента массива nums.
# 3) Вернуть максимум из left или right.

# Сложность:
# 1) Время O(n log n)
# 2) Память O(n)

nums = [1, 2, 3]

def maximumProduct(nums):
    nums = sorted(nums) # от 4 юнитеста
    left = nums[-1] * nums[-2] * nums[-3]
    right = nums[0] * nums[1] * nums[-1]
                # 6  # 6
    return max(left, right)

maximumProduct(nums)

assert maximumProduct(nums=[1, 2, 3]) == 6
assert maximumProduct(nums=[1, 2, 3, 4]) == 24
assert maximumProduct(nums=[-1, -2, -3]) == -6
assert maximumProduct(nums=[-100, -98, -1, 2, 3, 4]) == 39200
assert maximumProduct(nums=[-100, -2, -3, 1]) == 300
