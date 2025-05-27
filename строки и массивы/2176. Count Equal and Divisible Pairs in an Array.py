### Условие задачи:
# Дан целочисленный массив с индексом 0 nums длины n и целое число k, вернуть количество пар,
# (i, j) где 0 <= i < j < n , таких, что nums[i] == nums[j] и (i * j) делится на k .

# Example 1:
# Input: nums = [3,1,2,2,2,1,3], k = 2
# Output: 4
# Explanation:
# There are 4 pairs that meet all the requirements:
# - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
# - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
# - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
# - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

# Example 2:
# Input: nums = [1,2,3,4], k = 1
# Output: 0
# Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.

### Краткое условие:
# Надо вернуть колличество пара идексов массив nums которые делется на k.

# Алгоритм решение задачи:
# 0) Создаем переверную count со значением 0.
# 1) Проходимся циклом по диапазону от 0 до длины массива nums,
# 1.1) Проходимся циклом по диапазону от i + 1 до длины массива nums,
# 1.1.1) Если элемент i и элемент j одинаковые и (i * j) % k без остатка, то увеличь count на 1.
# 2) Верни count.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(1)

nums = [3, 1, 2, 2, 2, 1, 3]
k = 2

def countPairs(nums, k):
    count = 0

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if nums[i] == nums[j] and (i * j) % k == 0:

                count += 1

    return count

countPairs(nums, k)

assert countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2) == 4
assert countPairs(nums=[1, 2, 3, 4], k=1) == 0