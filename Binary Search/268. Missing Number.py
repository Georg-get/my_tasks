### Условие задачи:
# Учитывая массив nums, содержащий nразличные числа в диапазоне [0, n],
# верните единственное число в диапазоне, которое отсутствует в массиве.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

### Краткое условие:
# Надо вернуть число которое отсудствует в массиве nums.

# Алгоритм решение задачи:
# 0) Сортируем массив nums, по возврастанию.
# 1) Определить границы поиска.(left и right) и пройтись циклом,
# 1.1) Определяем середину = (left + right) // 2,
# 1.2) Если серидина массива nums равна mid, то увеличеваем значение переменой left на mid + 1.
# 1.3) Если серидина массива nums НЕ равна mid, то увеличеваем значение переменой right на mid - 1.
# 2) Верунть переменную left.

# Сложность:
# 1) Время O(n log n)
# 2) Память O(k)

nums = [3, 0, 1]

def missingNumber(nums):
    nums.sort()  # [0, 1, 3]
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1
    #       2
    return left

missingNumber(nums)

assert missingNumber(nums=[3, 0, 1]) == 2
assert missingNumber(nums=[0, 1]) == 2
assert missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8