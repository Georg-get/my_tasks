### Условие задачи:
# Вам дан целочисленный массив с индексом 0 nums и целое число threshold.
# Найдите длину самого длинного подмассива , nums начинающегося с индекса l и заканчивающегося индексом r (0 <= l <= r < nums.length), который удовлетворяет следующим условиям:
# nums[l] % 2 == 0
# Для всех индексов i в диапазоне [l, r - 1],nums[i] % 2 != nums[i + 1] % 2
# Для всех индексов i в диапазоне [l, r],nums[i] <= threshold.
# Верните целое число, обозначающее длину самого длинного такого подмассива.
# Примечание: Подмассив — это непрерывная непустая последовательность элементов внутри массива.

# Example 1:
# Input: nums = [3,2,5,4], threshold = 5
# Output: 3
# Explanation: In this example, we can select the subarray that starts at l = 1 and ends at r = 3 => [2,5,4]. This subarray satisfies the conditions.
# Hence, the answer is the length of the subarray, 3. We can show that 3 is the maximum possible achievable length.

# Example 2:
# Input: nums = [1,2], threshold = 2
# Output: 1
# Explanation: In this example, we can select the subarray that starts at l = 1 and ends at r = 1 => [2].
# It satisfies all the conditions and we can show that 1 is the maximum possible achievable length.

# Example 3:
# Input: nums = [2,3,4,5], threshold = 4
# Output: 3
# Explanation: In this example, we can select the subarray that starts at l = 0 and ends at r = 2 => [2,3,4].
# It satisfies all the conditions.
# Hence, the answer is the length of the subarray, 3. We can show that 3 is the maximum possible achievable length.

### Краткое условие:
# Верните целое число, обозначающее длину самого длинного такого подмассива.

# Полное объяснение решение задачи:
# 0) Создаем переменные maxStreak и streak со значнеим 0.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если i меньше или равно threshold и streak деленное на 2 равно i деленное на 2,
# 1.1.1) Увеличь streak на 1.
# 1.2) Иначе, maxStreak равно максимуму из streak и maxStreak.
# 1.2.1) Если i больше threshold или i делется на 2, то streak равно 0.
# 1.2.2) Иначе, streak равно 1.
# 2) Верни максимальное число из streak или maxStreak.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [3, 2, 5, 4]
threshold = 5

def longestAlternatingSubarray(nums, threshold):
    maxStreak = 0
    streak = 0

    for i in nums:

        if i <= threshold and streak % 2 == i % 2:
            streak += 1

        else:
            maxStreak = max(streak, maxStreak)

            if i > threshold or i % 2: #  or i % 2 нужно для 4 юнитеста
                streak = 0
            else:
                streak = 1

    return max(streak, maxStreak)

longestAlternatingSubarray(nums, threshold)

assert longestAlternatingSubarray(nums=[3, 2, 5, 4], threshold=5) == 3
assert longestAlternatingSubarray(nums=[1, 2], threshold=2) == 1
assert longestAlternatingSubarray(nums=[2, 3, 4, 5], threshold=4) == 3
assert longestAlternatingSubarray(nums=[1], threshold=1) == 0 # этот тест валит код