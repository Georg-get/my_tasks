### Условие задачи:
# Учитывая массив целых чисел nums, верните количество хороших пар.
# Пара (i, j) называется хорошей , если nums[i] == nums[j] и i < j.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0

### Краткое условие:
# Надо найти хорошие пары (если i == j or i < j) в массиве nums. Вернуть число хороших пар.

# Алгоритм решение задачи:
# 0) Если все элементы массива nums разные, то верни 0.
# 1) Если все элементы массива nums разные, то создай пустой словарь dict и переменную result = 0 для подсчета хороших пар.
# 1.1) Пройтись циклом по массиву nums.
# 1.1.1) Если такой ключ есть в словаре dict, то увеличь на 1 значение переменой result и увеличь значение которое находится в этом ключе на 1.
# 1.1.2) Если такой ключа НЕТу в словаре dict, то добавь это число в словаре dict, как ключ и значение этого ключа сделай 1.
# 1.2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 2, 3, 1, 1, 3]

def numIdenticalPairs(nums):
    if len(nums) == len(set(nums)):
        return 0

    else:
        dict = {}
        result = 0

        for i in nums:
            if i in dict:
                result += dict[i]  # result = result + dict[i]
                dict[i] += 1  # dict[i] = dict[i] + 1
                # {1:1, 2:1, 3:1} result = 0
                # {1:2, 2:1, 3:1} result = 1
                # {1:3, 2:1, 3:1} result = 3
                # {1:3, 2:1, 3:2} result = 4
            else:
                dict[i] = 1
                # {1:1}
                # {1:1, 2:1}
                # {1:1, 2:1, 3:1}
        # {1: 3, 2: 1, 3: 2}
        return result # 4

numIdenticalPairs(nums)

assert numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]) == 4
assert numIdenticalPairs(nums=[1, 1, 1, 1]) == 6
assert numIdenticalPairs(nums=[1, 2, 3]) == 0
