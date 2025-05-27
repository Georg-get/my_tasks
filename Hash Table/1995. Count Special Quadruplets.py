### Условие задачи:
# Учитывая целочисленный массив с индексом 0 nums , верните количество различных четверок (a, b, c, d) таких, что:
# nums[a] + nums[b] + nums[c] == nums[d], и
# a < b < c < d


# Example 1:
# Input: nums = [1,2,3,6]
# Output: 1
# Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

# Example 2:
# Input: nums = [3,3,6,4,5]
# Output: 0
# Explanation: There are no such quadruplets in [3,3,6,4,5].

# Example 3:
# Input: nums = [1,1,1,3,5]
# Output: 4
# Explanation: The 4 quadruplets that satisfy the requirement are:
# - (0, 1, 2, 3): 1 + 1 + 1 == 3
# - (0, 1, 3, 4): 1 + 1 + 3 == 5
# - (0, 2, 3, 4): 1 + 1 + 3 == 5
# - (1, 2, 3, 4): 1 + 1 + 3 == 5


### Краткое условие:
# Верните количество различных четверок (a, b, c, d)

### Хэш таблицы

                                                ### Добавить в список !

# Алгоритм решение задачи:
# 0) Создаем две переменные: count со значением 0 и lenNums со значением длины массива nums.
# 1) Проходимся циклом диапозону от 0 до lenNums,
# 1.1) Проходимся циклом диапозону от b+1 до lenNums,
# 1.1.1) Проходимся циклом диапозону от c+1 до lenNums,
# 1.1.1.1) Если nums[a] + nums[b] + nums[c] = nums[d], то увеличь count на 1.
# 2) Вернуть count.


# Сложность:
# 1) Время O(n^4)
# 2) Память O(1)

nums = [1, 2, 3, 6]

def countQuadruplets(nums):
    count = 0
    lenNums = len(nums)

    for a in range(lenNums): # range(0, 4)
        for b in range(a + 1, lenNums): # range(1, 4) range(2, 4) range(3, 4) range(4, 4)
            for c in range(b + 1, lenNums): # (2, 4) (3, 4)  (4, 4) (3, 4) (4, 4) (4, 4)
                for d in range(c + 1, lenNums): # range(3, 4)
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        count += 1

    return count

countQuadruplets(nums)

assert countQuadruplets(nums=[1, 2, 3, 6]) == 1
assert countQuadruplets(nums=[3, 3, 6, 4, 5]) == 0
assert countQuadruplets(nums=[1, 1, 1, 3, 5]) == 4

# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

### Сложная задача !!!

# from collections import defaultdict
#
# nums = [1, 2, 3, 6]
#
# def countQuadruplets(nums):
#     lenNums = len(nums)
#
#     dict = defaultdict(int) # (<class 'int'>, {})
#     result = 0
#
#     for i in range(lenNums - 3, 0, -1): # range(1, 0, -1)
#
#         c = i + 1
#
#         for j in range(i + 2, lenNums): # range(3, 4)
#             cur = nums[j] - nums[c]
#             dict[cur] += 1
#
#         for a in range(i): # range(0, 1)
#             target = nums[a] + nums[i]
#             result += dict[target]
#     # defaultdict(<class 'int'>, {3: 1})
#     return result # 1
#
# countQuadruplets(nums)
#
# assert countQuadruplets(nums=[1, 2, 3, 6]) == 1
# assert countQuadruplets(nums=[3, 3, 6, 4, 5]) == 0
# assert countQuadruplets(nums=[1, 1, 1, 3, 5]) == 4
