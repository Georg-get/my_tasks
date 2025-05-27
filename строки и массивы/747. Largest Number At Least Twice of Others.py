### Условие задачи:
# Вам дан массив целых чисел nums, где наибольшее целое число является уникальным.
# Определите, является ли наибольший элемент массива по крайней мере вдвое больше любого другого числа в массиве.
# Если это так, верните индекс наибольшего элемента или верните -1 в противном случае.

# Example 1:
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.

### Краткое условие:
# Если это так, верните индекс наибольшего элемента или верните -1 в противном случае.

# Полное объяснение решение задачи:
# 0) Находим максимальное число в массиве nums и его индекс.
# 1) Удаляем это число из массива и находим второе максивально число в массиве nums.
# 2) Если максимально число больше или ранво 2 * на максимальное второе число, то верки индекс максимального числа.
# 3) Иначе, верни -1.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [3, 6, 1, 0]

def dominantIndex(nums):
    maxValue = max(nums)  # 6
    maxIndesCounter = int(nums.index(max(nums)))  # 1
    nums.remove(maxValue)  # [3, 1, 0]
    secondMaxValue = max(nums)  # 3 

    if maxValue >= 2 * secondMaxValue:
        return maxIndesCounter
    else:
        return -1

dominantIndex(nums)

assert dominantIndex(nums=[3, 6, 1, 0]) == 1  # if maxValue >= 2 * secondMaxValue: знак =
assert dominantIndex(nums=[1, 2, 3, 4]) == -1
assert dominantIndex(nums=[0, 0, 0, 1]) == 3  # if maxValue >= 2 * secondMaxValue: знак >