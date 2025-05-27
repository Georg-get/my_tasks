### Условие задачи:
# Вам дан массив nums неотрицательных целых чисел и целое число k. Массив называется специальным,
# если разрядность OR всех его элементов не менее k.
# Верните длину самого короткого специального непустого подмассив или возврат nums,
# если специального подмассива не существует. -1

# Example 1:
# Input: nums = [1,2,3], k = 2
# Output: 1
# Explanation:
# The subarray [3] has OR value of 3. Hence, we return 1.
# Note that [2] is also a special subarray.

# Example 2:
# Input: nums = [2,1,8], k = 10
# Output: 3
# Explanation:
# The subarray [2,1,8] has OR value of 11. Hence, we return 3.

# Example 3:
# Input: nums = [1,2], k = 0
# Output: 1
# Explanation:
# The subarray [1] has OR value of 1. Hence, we return 1.


                                                        ### Добавить в список !


### Краткое условие:
# Верните длину самого короткого специального непустого подмассив или возврат nums, если специального подмассива не существует. -1

# Полное объяснение решение задачи:
# 0) Если k равно 0, то верки 1.
# 1) Создаем переменные: sum_val, left, right со значением 0 и min_length со значением бесконечность.
# 2) Проходим циклом вайлд пока правый указатель не дойдет до конца строки nums,
# 2.1) Увеличиваем sum_val по битова на nums[right],
# 2.1.1) Проходим циклом вайлд пока sum_val не пересекутся,
# 2.1.1.1) size = right - left + 1,
# 2.1.1.2) Увеличиваем min_length на минимум из min_length и size,
# 2.1.1.3) sum_val = 0,
# 2.1.1.4) Проходимся циклом по диапазону от left + 1 до right + 1 и sum_val увеличиваем побитова на nums[i].
# 2.1.1.5) Увеличиваем left на 1.
# 2.1.2) Увеличиваем right на 1.
# 3) Если min_length равно бесконечности, то верни -1,
# 3.1) Иначе, верни min_length.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

### Сложная задача !!!

nums = [1, 2, 3]
k = 2

def minimumSubarrayLength(nums, k):
    if k == 0:
        return 1

    sum_val = 0
    left = 0
    right = 0
    min_length = float('inf') # бесконечность

    while right < len(nums):
        sum_val |= nums[right]

        while sum_val >= k:
            size = right - left + 1
            min_length = min(min_length, size)

            sum_val = 0
            for i in range(left + 1, right + 1):
                sum_val |= nums[i]
            left += 1

        right += 1

    if min_length == float('inf'):
        return -1
    else:
        return min_length

minimumSubarrayLength(nums, k)

assert minimumSubarrayLength(nums=[1, 2, 3], k=2) == 1
assert minimumSubarrayLength(nums=[2, 1, 8], k=10) == 3
assert minimumSubarrayLength(nums=[1, 2], k=0) == 1