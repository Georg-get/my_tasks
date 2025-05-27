### Условие задачи:
# Дан массив nums целых чисел, вычислите, сколько из них содержат четное количество цифр.

# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.

### Краткое условие:
# Надо вернуть колличество чисел которых длина делется на два без остатка из массива nums.

# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [12, 345, 2, 6, 7896]

def findNumbers(nums):
    result = 0

    for i in nums:
        if len(str(i)) % 2 == 0:
            result += 1

    return result

findNumbers(nums)

assert findNumbers(nums=[12, 345, 2, 6, 7896]) == 2
assert findNumbers(nums=[555, 901, 482, 1771]) == 1