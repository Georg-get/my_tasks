### Условие задачи:
# Вам дан массив положительных целых чисел с индексом 0 nums .
# Найдите количество троек (i, j, k), удовлетворяющих следующим условиям:
# 0 <= i < j < k < nums.length
# nums[i], nums[j], и попарно nums[k] различны .
# Другими словами, nums[i] != nums[j], nums[i] != nums[k], и nums[j] != nums[k].
# Возвращает количество троек, удовлетворяющих условиям.

# Example 1:
# Input: nums = [4,4,2,4,3]
# Output: 3
# Explanation: The following triplets meet the conditions:
# - (0, 2, 4) because 4 != 2 != 3
# - (1, 2, 4) because 4 != 2 != 3
# - (2, 3, 4) because 2 != 4 != 3
# Since there are 3 triplets, we return 3.
# Note that (2, 0, 4) is not a valid triplet because 2 > 0.

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: No triplets meet the conditions so we return 0.

### Краткое условие:
# Возвращает количество троек, удовлетворяющих условиям.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict, переменные: result и left со значением 0, и right созначением длины массива nums.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если i есть в словаре dict, то увеличь значение ключа на 1.
# 1.2) Если i НЕТу в словаре dict, то добавь i как ключ со значением 1.
# 2) Проходимся циклом по значению словаря dict,
# 2.1) Уменьшаем значение переменной right на j.
# 2.2) Увеличиваем значение переменой на right умножить на j и умножить на left.
# 2.3) Увеличиваем значение переменой на left на j.
# 3) Вернуть переменную result.

nums = [4, 4, 2, 4, 3]

def unequalTriplets(nums):
    result = 0
    dict = {}
    left = 0
    right = len(nums)

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {4: 3, 2: 1, 3: 1}
    for j in dict.values():  # dict_values([3, 1, 1])
        right -= j  # right=0-3=-3
        result += right * j * left  # result=-3* 3 * 0 =0
        left += j  # left=0+3=3
    return result  # 3

unequalTriplets(nums)

assert unequalTriplets(nums=[4, 4, 2, 4, 3]) == 3
assert unequalTriplets(nums=[1, 1, 1, 1, 1]) == 0