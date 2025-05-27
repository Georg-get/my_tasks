### Условие задачи:
# Вам дан целочисленный массив с индексом 0 nums.
# Верните максимальное значение по всем тройкам индексов, (i, j, k) таким что i < j < k.
# Если все такие тройки имеют отрицательное значение, верните 0.
# Значение тройки индексов (i, j, k) равно (nums[i] - nums[j]) * nums[k].

# Example 1:
# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77.

# Example 2:
# Input: nums = [1,10,3,4,19]
# Output: 133
# Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
# It can be shown that there are no ordered triplets of indices with a value greater than 133.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0
# Explanation: The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3.
# Hence, the resultwer would be 0.

### Краткое условие:
# Верните максимальное значение по всем тройкам индексов, (i, j, k) таким что i < j < k.
# Если все такие тройки имеют отрицательное значение, верните 0.

# Алгоритм решение задачи:
# 0) Создаем переменные: result, diff, prefix со значением 0.
# 1) Проходимся циклом по массиву nums,
# 1.1) result равно максимальному значению из result или i умноженое на diff.
# 1.2) diff равно максимальному значению из diff или prefix-1.
# 1.3) prefix равно максимальному значению из prefix или i.
# 2) Вернуть result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [12, 6, 1, 2, 7]

def maximumTripletValue(nums):
    result = 0
    diff = 0
    prefix = 0
    
    for i in nums:
        result = max(result, i * diff)
        diff = max(diff, prefix - i)
        prefix = max(prefix, i)
        
    return result

maximumTripletValue(nums)

assert maximumTripletValue(nums=[12, 6, 1, 2, 7]) == 77
assert maximumTripletValue(nums=[1, 10, 3, 4, 19]) == 133
assert maximumTripletValue(nums=[1, 2, 3]) == 0