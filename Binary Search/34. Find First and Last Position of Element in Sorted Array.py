### Условие задачи:
# Дан массив целых чисел nums, отсортированных в порядке не убывания,
# найдите начальную и конечную позицию заданного target значения.
# Если target не найден в массиве, верните [-1, -1].
# Вы должны написать алгоритм со O(log n) сложностью выполнения.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

### Краткое условие:
# Найти число в массиве. И вернуть номера элементов которые соответсруют числу которые мы ищем.
# Если такого числа нету вернуть "-1,-1".

# Алгоритм решение задачи:
# 0) Обьявить границы для поиска (left и right), которые будем сужать.
# 0.1) Создать пустой массив (result).
# 1) Пойтись по циклом по левой старане массива "nums",
# 1.1) Если в левой старане массива "nums", есть число которое похоже на число target, то добавь его в стек.
# 2) Пойтись по циклом по правой старане массива "nums",
# 2.1) Если в правой старане массива "nums", есть число которое похоже на число target, то добавь его в стек.
# 3) Проверить длина массива result == 0 .
# 3.1) Если да вернуть return [-1, -1] .
# 3.2) Если НЕТ то вернуть массив result.

# Сложность:
# 1) Время O(log n)
# 2) Память O(1)

nums = [5, 7, 7, 8, 8, 10]
target = 8

def searchRange(nums, target):
    result = [-1, -1]

    # Ищем бинарным поиском в левой части массива nums
    left = 0
    right = len(nums) - 1 # 5

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result[0] = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # [3, -1]
    # Ищем бинарным поиском в правай части массива nums
    left = 0
    right = len(nums) - 1 # 5

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result[1] = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # [3, 4]
    return result

searchRange(nums, target)

assert searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
assert searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
assert searchRange(nums=[], target=0) == [-1, -1]