### Условие задачи:
# Учитывая массив целых чисел nums, отсортированный в порядке возрастания, и целое число target,
# напишите функцию для target поиска nums. Если target существует, верните его индекс. В противном случае вернитесь -1.
# Вы должны написать алгоритм со O(log n) сложностью выполнения.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

### Краткое условие:
# Найти число в массиве. Вернуть номер элемента в массиве.

# Алгоритм решение задачи:
# 0) Написать бинарный поиск.
# 1) Вернуть номер индекса в массиве nums, который соответсвует числу target.
# 1.1) Если нету номер индекса в массиве nums, который соответсвует числу target, то верни -1.

# Сложность:
# 1) памяти O(n log n)
# 2) времени O(1)

nums = [-1, 0, 3, 5, 9, 12]
target = 9

def search(nums, target):
    left = 0
    right = len(nums) - 1  # 5

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

search(nums, target)

assert search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1