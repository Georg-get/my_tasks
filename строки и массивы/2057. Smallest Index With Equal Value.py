### Условие задачи:
# Для заданного целочисленного массива с индексом 0 nums вернуть наименьший индекс,
# i такой nums что i mod 10 == nums[i], или -1если такой индекс не существует.
# x mod y обозначает остаток при x делении на y.

# Example 1:
# Input: nums = [0,1,2]
# Output: 0
# Explanation:
# i=0: 0 mod 10 = 0 == nums[0].
# i=1: 1 mod 10 = 1 == nums[1].
# i=2: 2 mod 10 = 2 == nums[2].
# All indices have i mod 10 == nums[i], so we return the smallest index 0.

# Example 2:
# Input: nums = [4,3,2,1]
# Output: 2
# Explanation:
# i=0: 0 mod 10 = 0 != nums[0].
# i=1: 1 mod 10 = 1 != nums[1].
# i=2: 2 mod 10 = 2 == nums[2].
# i=3: 3 mod 10 = 3 != nums[3].
# 2 is the only index which has i mod 10 == nums[i].

# Example 3:
# Input: nums = [1,2,3,4,5,6,7,8,9,0]
# Output: -1
# Explanation: No index satisfies i mod 10 == nums[i].

### Краткое условие:
# Надо найти индекс числа из массива nums , которое делется на 10 и дает в остатке элемент , если такого числа нету то вернуть -1.

# Алгоритм решение задачи:
# 0) Проходимся циклом по диапазону от 0 до длинный массива nums,
# 0.1) Если индекс i делется без остатка на 10 и равен элементу массив nums, то верни i.
# 1) Верни -1.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [0, 1, 2]

def smallestEqual(nums):

    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i

    return -1

smallestEqual(nums)

assert smallestEqual(nums=[0, 1, 2]) == 0
assert smallestEqual(nums=[4, 3, 2, 1]) == 2
assert smallestEqual(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == -1