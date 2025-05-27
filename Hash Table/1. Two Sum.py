### Условие задачи:
# Учитывая массив целых чисел nums и целое число target, верните индексы двух чисел так, чтобы их сумма составляла target.
# Вы можете предположить, что каждый вход будет иметь ровно одно решение,
# и вы не можете использовать один и тот же элемент дважды.
# Вы можете вернуть ответ в любом порядке.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

### Краткое условие:
# Надо вернуть индексы тех числел которые дают в сумме число target.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Пройтись циклом по диапазону длине массива nums.
# 1.1) Посчитать diff = target - nums[i]
# 1.2.1) Если ключ diff есть в словаре dict, то верни массив со значением этого ключа и i.
# 1.2.2) Если нету ключа похожего на diff в словаре dict, то добавь этот элемент в словарь dict со значением i.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    dict = {}

    for i in range(len(nums)): # range(0,4)
        diff = target - nums[i]  # diff = 9 - 2

        if diff in dict:
            # {0},  1
            return [dict[diff], i]
        else:
            dict[nums[i]] = i
            # {2: 0}

twoSum(nums, target)

assert twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert twoSum(nums=[3, 2, 4], target=6) == [1, 2]
assert twoSum(nums=[3, 3], target=6) == [0, 1]