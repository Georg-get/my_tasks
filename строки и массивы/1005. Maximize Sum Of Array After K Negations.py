### Условие задачи:
# Дан массив целых чисел nums и целое число k. Измените массив следующим образом:
# выберите индекс i и замените nums[i] на -nums[i].
# Вы должны применить этот процесс ровно k раз. Вы можете выбрать один и тот же индекс i несколько раз.
# Верните максимально возможную сумму массива после его модификации таким образом.

# Example 1:
# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose index 1 and nums becomes [4,-2,3].

# Example 2:
# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

# Example 3:
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

### Краткое условие:
# Верните максимально возможную сумму массива после его модификации таким образом .

# Полное объяснение решение задачи:
# 0) Создаем кучу с элементами массива nums.
# 1) Проходимся циклом по диапазону от 0 до k,
# 1.1) Меняем знак самого минимального числа в куче nums.
# 2) Складываем все числа из кучи и возврашаем результат.

# Сложность:
# 1) Время O(n + k log n)
# 2) Память O(n)

import heapq

nums = [4, 2, 3]
k = 1

def largestSumAfterKNegations(nums, k):
    heapq.heapify(nums) # преобразует список в кучу
    # [2, 4, 3]

    for i in range(k): # 1
        heapq.heappush(nums, -heapq.heappop(nums))
    # [-2, 4, 3]
    return sum(nums)

largestSumAfterKNegations(nums, k)

assert largestSumAfterKNegations(nums=[4, 2, 3], k=1) == 5
assert largestSumAfterKNegations(nums=[3, -1, 0, 2], k=3) == 6
assert largestSumAfterKNegations(nums=[2, -3, -1, 5, -4], k=2) == 13