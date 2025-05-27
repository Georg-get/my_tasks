### Условие задачи:
# Учитывая массив, nums отсортированный в порядке не убывания,
# верните максимум между количеством положительных целых чисел и количеством отрицательных целых чисел.
# Другими словами, если количество положительных целых чисел в nums is pos и количество отрицательных целых чисел равно neg,
# то возвращается максимальное значение pos и neg.
# Обратите внимание, что это 0 не является ни положительным, ни отрицательным.

# Example 1:
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3

# Example 2:
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3

# Example 3:
# Input: nums = [5,20,66,1314]
# Output: 4

### Краткое условие:
# Вывести количество чисел которых больше.
# Если в массиве nums больше положительных числе чем отрицательных, то вернуть количество положительных чисел.
# Если в массиве nums больше отрецательных чисел чем положительных, то вернуть количество отрецательных чисел.

### Без бинарного поиска ###
# Алгоритм решение задачи:
# 0) Создать переменные: numberOfPositiveNumbers и numberOfNegativeNumbers
# 1) Посчитать колличество отрецательных чисел и этот результат записать в переменную numberOfNegativeNumbers
# 1.1) Если нету отрицательных чисел то запеши в переменную numberOfNegativeNumbers = 0
# 2) Посчитать колличество положительных чисел и этот результат записать в переменную numberOfPositiveNumbers
# 2.1) Если нету положительных чисел то запеши в переменную numberOfPositiveNumbers = 0
# 3) Сравки две переменные: numberOfPositiveNumbers и numberOfNegativeNumbers
# 3.1) Если numberOfPositiveNumbers >= numberOfNegativeNumbers, то верни numberOfPositiveNumbers.
# 3.2) Если numberOfPositiveNumbers <= numberOfNegativeNumbers, то верни numberOfNegativeNumbers.

###                                             C бинарным поиском                                                    ###
# Алгоритм решение задачи:
# 0) Удалить все 0 из массива nums
# 1) Написать функцию бинарного поиска которая ищет все положительные числа в массиве nums и,
# складывает количество индексов в переменную numberOfPositiveNumbers
# 2) Написать функцию бинарного поиска которая ищет все отрицательные числа в массиве nums и,
# складывает количество индексов в переменную numberOfNegativeNumbers
# 3) Сравки две переменные: numberOfPositiveNumbers и numberOfNegativeNumbers
# 3.1) Если numberOfPositiveNumbers >= numberOfNegativeNumbers, то верни numberOfPositiveNumbers.
# 3.2) Если numberOfPositiveNumbers <= numberOfNegativeNumbers, то верни numberOfNegativeNumbers.

# Сложность:
# 1) времени O(n*log(n))
# 2) памяти O(1)

nums = [-3, -2, -1, 0, 0, 1, 2]

def maximumCount(nums):
    def binarySearch(arr, target, leftmost=True):
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2

            if leftmost == True and target <= arr[mid]:
                right = mid
            elif target < arr[mid]:
                right = mid
            else:
                left = mid + 1

        return left

    while 0 in nums:  # nums = [-3, -2, -1, 0, 0, 1, 2]
        nums.remove(0)         # Удаляем все 0 из массива nums !!!
    # nums = [-3, -2, -1, 1, 2]

    numberOfNegativeNumbers = binarySearch(nums, 0) # 3
    numberOfPositiveNumbers = len(nums) - binarySearch(nums, 0, False) # 2
    #        2                              3
    if numberOfPositiveNumbers >= numberOfNegativeNumbers:
        return numberOfPositiveNumbers # 3 - тут закончиться ВТОРОЙ юнитест !!!
    elif numberOfPositiveNumbers <= numberOfNegativeNumbers:
        return numberOfNegativeNumbers # 3 - тут закончиться ПЕРВЫЙ и ТРЕТИЙ юнитест !!!
    # return max(numberOfNegativeNumbers, numberOfPositiveNumbers)

maximumCount(nums)

assert maximumCount(nums=[-2, -1, -1, 1, 2, 3]) == 3
assert maximumCount(nums=[-3, -2, -1, 0, 0, 1, 2]) == 3
assert maximumCount(nums=[5, 20, 66, 1314]) == 4

                                        ### БЕЗ бинарным поиском ###
# Сложность:
# 1) памяти O(1)
# 2) времени O(n)

# nums = [-2, -1, -1, 1, 2, 3]
#
# def maximumCount(nums):
#     numberOfPositiveNumbers = 0
#     numberOfNegativeNumbers = 0
#
#     for i in nums:
#         if i < 0:
#             numberOfNegativeNumbers += 1
#         elif i > 0:
#             numberOfPositiveNumbers += 1
#
#     if numberOfPositiveNumbers >= numberOfNegativeNumbers:
#         return numberOfPositiveNumbers
#     elif numberOfPositiveNumbers <= numberOfNegativeNumbers:
#         return numberOfNegativeNumbers
#
# maximumCount(nums)