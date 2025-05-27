### Условие задачи:
# Вам дан массив целых чисел с индексом 0 nums.
# Тройка индексов (i, j, k) является горой , если:
# 1) i < j < k
# 2) nums[i] < nums[j] и nums[k] < nums[j]
# Верните минимально возможную сумму горного триплета nums. Если такого триплета не существует, верните -1 .

# Example 1:
# Input: nums = [8,6,1,5,3]
# Output: 9
# Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since:
# - 2 < 3 < 4
# - nums[2] < nums[3] and nums[4] < nums[3]
# And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

# Example 2:
# Input: nums = [5,4,8,7,10,2]
# Output: 13
# Explanation: Triplet (1, 3, 5) is a mountain triplet of sum 13 since:
# - 1 < 3 < 5
# - nums[1] < nums[3] and nums[5] < nums[3]
# And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.

# Example 3:
# Input: nums = [6,5,4,3,4,5]
# Output: -1
# Explanation: It can be shown that there are no mountain triplets in nums.

### Краткое условие:
# Верните минимально возможную сумму горного триплета nums. Если такого триплета не существует, верните -1 .

# Алгоритм решение задачи:
# 0) Создаем пустой массив result.
# 1) Проходимся циклом по диапазону от 0 до длины массива nums,
# 1.1) Проходимся циклом по диапазону от i + 1 до длины массива nums,
# 1.1.1) Проходимся циклом по диапазону от j + 1 до длины массива nums,
# 1.1.1.1) Если число i меньше числа j и число j больше числа k, то сложи их все и результат добавь в массив result.
# 2) Если длина массива result равна 0, то верни -1.
# 3) Если длина массива result Не равна 0, то верни минимальный элемент массива result.

# Сложность:
# 1) Время O(n^3)
# 2) Память O(1)

nums = [8, 6, 1, 5, 3]

def minimumSum(nums):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] < nums[j] and nums[j] > nums[k]:
                    result.append(nums[i] + nums[j] + nums[k])
    # [9]
    if len(result) == 0:
        return -1
    else:
        return min(result)

minimumSum(nums)

assert minimumSum(nums=[8, 6, 1, 5, 3]) == 9 # [9]
assert minimumSum(nums=[5, 4, 8, 7, 10, 2]) == 13 # [20, 15, 14, 17, 19, 14, 13, 16, 20, 19]
assert minimumSum(nums=[6, 5, 4, 3, 4, 5]) == -1 # []