### Условие задачи:
# Массив считается особым, если каждая пара его соседних элементов содержит два числа с разной четностью.
# Вам дан массив целых чисел nums. Верните, true если nums это специальный массив, в противном случае верните false.

# Example 1:
# Input: nums = [1]
# Output: true
# Explanation:
# There is only one element. So the answer is true.

# Example 2:
# Input: nums = [2,1,4]
# Output: true
# Explanation:
# There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

# Example 3:
# Input: nums = [4,3,1,6]
# Output: false
# Explanation:
# nums[1] and nums[2] are both odd. So the answer is false.

### Краткое условие:
# Верните, true если nums это специальный массив, в противном случае верните false.

# Полное объяснение решение задачи:
# 0) Проходимся циклом по диапазону индексов от 1 до длины длиный массива,
# 0.1) Если число перед i четное и i тоже четное, то верни False.
# 1) Вернуть True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1]

def isArraySpecial(nums):

    for i in range(1, len(nums)):
        if nums[i - 1] % 2 == nums[i] % 2:
            return False

    return True

isArraySpecial(nums)

assert isArraySpecial(nums=[1]) == True
assert isArraySpecial(nums=[2, 1, 4]) == True
assert isArraySpecial(nums=[4, 3, 1, 6]) == False