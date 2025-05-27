### Условие задачи:
# Учитывая целочисленный массив nums и целое число k, верните количество пар,
# (i, j) где i < j такое, что |nums[i] - nums[j]| == k.
# Значение |x|определяется как:
# x если x >= 0.
# -x если x < 0.

# Example 1:
# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]

# Example 2:
# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.

# Example 3:
# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]

### Краткое условие:
# Надо вернуть количество пар разница, которых будет равна k.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result = 0 для подсчета хороших пар.
# 1) Пройтись циклом по массиву nums.
# 1.1) Если ключ со значением i есть в словаре dict, то увеличь значение ключа на 1.
# 1.2) Если такого ключа нету, то добавь ключ i со значением 1.
# 2) Пройтись циклом по массиву nums.
# 2.1) Если такой ключ (j-k) в словаре dict, то увеличь переменную result на значение этого ключа.
# 3) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 2, 2, 1]
k = 1

def countKDifference(nums, k):
    result = 0
    dict = {}

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {1: 2, 2: 2}
    for j in nums:
        if j - k in dict:
            result += dict[j - k]
            # 2
            # 4
    return result  # 4

countKDifference(nums, k)

assert countKDifference(nums=[1, 2, 2, 1], k=1) == 4
assert countKDifference(nums=[1, 3], k=3) == 0
assert countKDifference(nums=[3, 2, 1, 5, 4], k=2) == 3