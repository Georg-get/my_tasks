### Условие задачи:
# Для заданного двоичного массива nums вернуть максимальное количество последовательных элементов 1 в массиве.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

### Краткое условие:
# Для заданного двоичного массива nums вернуть максимальное количество последовательных элементов 1 в массиве.

# Алгоритм решение задачи:
# 0) Создаем переменные count и result со значением 0.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если i равно 1, то увеличь count на 1 и увеличь result на максивальное число из count и result.
# 1.2) Если i НЕ равно 1, то count равно 0.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [1, 1, 0, 1, 1, 1]

def findMaxConsecutiveOnes(nums):
    count = 0
    result = 0

    for i in nums:
        if i == 1:
            count += 1
            result = max(count, result)
        else:
            count = 0

    return result

findMaxConsecutiveOnes(nums)

assert findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]) == 3
assert findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]) == 2