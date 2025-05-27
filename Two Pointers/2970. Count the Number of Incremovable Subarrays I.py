### Условие задачи:
# Вам дан массив положительных целых чисел с индексом 0 .nums
# Подмассив nums называется неустранимым , если при удалении подмассива nums он становится строго возрастающим.
# Например, подмассив [3, 4]является неустранимым подмассивом, [5, 3, 4, 6, 7] поскольку удаление этого подмассива
# изменяет массив [5, 3, 4, 6, 7], который [5, 6, 7] строго увеличивается.
# Возвращает общее количество неудалимых подмассивов nums.
# Обратите внимание , что пустой массив считается строго возрастающим.
# Подмассив — это непрерывная непустая последовательность элементов массива.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: 10
# Explanation: The 10 incremovable subarrays are: [1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4], and [1,2,3,4],
# because on removing any one of these subarrays nums becomes strictly increasing. Note that you cannot select an empty subarray.

# Example 2:
# Input: nums = [6,5,7,8]
# Output: 7
# Explanation: The 7 incremovable subarrays are: [5], [6], [5,7], [6,5], [5,7,8], [6,5,7] and [6,5,7,8].
# It can be shown that there are only 7 incremovable subarrays in nums.

# Example 3:
# Input: nums = [8,7,6,6]
# Output: 3
# Explanation: The 3 incremovable subarrays are: [8,7,6], [7,6,6], and [8,7,6,6]. Note that [8,7] is not an incremovable
# subarray because after removing [8,7] nums becomes [6,6], which is sorted in ascending order but not strictly increasing.

                                            ### Добавить в список !

### Краткое условие:
# Требуется вернуть общее количество инкремируемых подмассивов в nums.


#                             Без алгоритма !!!

# Краткое объяснение решение задачи:
# 1. Создается переменная result, которая будет хранить количество инкремируемых подмассивов.
# 2. Два вложенных цикла:
#    - Первый цикл (for i) перебирает начальные индексы подмассивов.
#    - Второй цикл (for j) перебирает конечные индексы подмассивов.
# 3. Создание нового массива: Для каждого сочетания i и j создается новый массив remain_array,
# который состоит из элементов до i и после j.
# 4. Проверка условий:
#    - Проверяется, отсортирован ли remain_array и содержит ли он только уникальные элементы (путем сравнения его длины с длиной множества).
#    - Если оба условия выполняются, увеличивается счетчик result.
# 5. Возвращаем общее количество инкремируемых подмассивов.

# Полное объяснение решение задачи:
# 0) Создаем переменную result со значением 0.
# 1) Проходимся циклом по диапазону от 0 до длины массива nums,
# 1.1) Проходимся циклом по диапазону от i до длины массива nums,
# 1.1.1) Создаем переменную remain_array со значением срезом массива nums i + срезом массива nums j+1,
# 1.1.2) Если отсортированый массив remain_array равен remain_array и длина массив remain_array равна длине массива remain_array без дублей,
# 1.1.2.1) То увеличь result на 1.
# 2) Верни result.

# Сложность:
# 1) Время O(n^3 log n)
# 2) Память O(n)

### Сложная задача !!!

nums = [1, 2, 3, 4]

def incremovableSubarrayCount(nums):
    result = 0

    for i in range(len(nums)):

        for j in range(i, len(nums)):

            remain_array = nums[:i] + nums[j + 1:]
            # print(nums[:i])       # print(nums[j + 1:])             # print(nums[:i] + nums[j + 1:])
            # []                    # [2, 3, 4]                       # [2, 3, 4]
            # []                    # [3, 4]                          # [3, 4]
            # []                    # [4]                             # [4]
            # []                    # []                              # []
            # [1]                   # [3, 4]                          # [1, 3, 4]
            # [1]                   # [4]                             # [1, 4]
            # [1]                   # []                              # [1]
             # [1, 2]               # [4]                             # [1, 2, 4]
            # [1, 2]                # []                              # [1, 2]
            # [1, 2, 3]             # []                              # [1, 2, 3]
            if sorted(remain_array) == remain_array and len(remain_array) == len(set(remain_array)):
                result += 1

    return result

incremovableSubarrayCount(nums)

assert incremovableSubarrayCount(nums=[1, 2, 3, 4]) == 10
assert incremovableSubarrayCount(nums=[6, 5, 7, 8]) == 7
assert incremovableSubarrayCount(nums=[8, 7, 6, 6]) == 3
# Доп юнитесты для проверки некоторых условий:
assert incremovableSubarrayCount(nums=[]) == 0 # Пустой и односторонний массив
assert incremovableSubarrayCount(nums= [2, 2, 1, 3]) == 5 # Массивы с разными паттернами
assert incremovableSubarrayCount(nums= [1]) == 1 # Односторонний массив

#                                        Без алгоритма и старое решение !!!

# Полное объяснение решение задачи:
# 0) Создаем переменную lenListNums со значением длины массива nums.
# 1) Если lenListNums равно 1, то верни 1.
# 2) Если lenListNums равно 2, то верни 2.
# 3) Создаем переменные left и right со значением -1.
# 4) Проходимся циклом по диапазону от 1 до lenListNums,
# 4.1) Если nums[i] меньше или равно чем nums[i - 1], то присвой перемеменой left значяение i и выйди.
# 5) Если left равно -1, то верни (1 + lenListNums) * lenListNums // 2.
# 6) Проходимся циклом по диапазону lenListNums -1 , 0 , -1,
# 6.1) Если nums[i] меньше или равно чем nums[i - 1], то присвой перемеменой left значяение i и выйди.
# 7) Создаем переменную result со значением left + 1.
# 8) Проходимся циклом по диапазону lenListNums -1 ,  right - 1, -1,
# 8.1) Проходимся циклом ваил пока left и nums[left - 1] больше или равно чем nums[j], то left -= 1.
# 8.2) Увеличиваем переменную result на left + 1.
# 9) Вернуть переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

#
# nums = [1, 2, 3, 4]
#
#
# def incremovableSubarrayCount(nums):
#     lenListNums = len(nums)
#
#     if lenListNums == 1:
#         return 1
#     elif lenListNums == 2:
#         return 3
#
#     left = -1
#     right = -1
#
#     for i in range(1, lenListNums):
#         if nums[i] <= nums[i - 1]:
#             left = i
#             break
#
#     if left == -1:
#         return (1 + lenListNums) * lenListNums // 2
#
#     for i in range(lenListNums - 1, 0, - 1):
#         if nums[i] <= nums[i - 1]:
#             right = i
#             break
#
#     result = left + 1
#     for j in range(lenListNums - 1, right - 1, -1):
#         while left and nums[left - 1] >= nums[j]:
#             left -= 1
#         result += left + 1
#
#     return result
#
# incremovableSubarrayCount(nums)

# class Solution:
#     def incremovableSubarrayCount(self, nums: List[int]) -> int:
#         i, n = 0, len(nums)
#         while i + 1 < n and nums[i] < nums[i + 1]:
#             i += 1
#         if i == n - 1:
#             return n * (n + 1) // 2
#         ans = i + 2
#         j = n - 1
#         while j:
#             while i >= 0 and nums[i] >= nums[j]:
#                 i -= 1
#             ans += i + 2
#             if nums[j - 1] >= nums[j]:
#                 break
#             j -= 1
#         return ans
#                             Два указателя !!!

# Полное объяснение решение задачи:
# 0) Создаем

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

# nums = [1, 2, 3, 4]
#
# def incremovableSubarrayCount(nums):
#     result = 0
#     left = 0
#     right = 1
#
#     while left < len(nums):
#         if nums[:left] + nums[right:] == sorted(nums[right:] + nums[:left]) and len(nums[:left] + nums[right:]) == len(
#                 set(nums[:left] + nums[right:])):
#             result += 1
#
#         right += 1
#
#         if right > len(nums):
#             left += 1
#             right = left + 1
#
#     return result

                                ### Рабочие решение но долгое !!! ###
# Сложность:
# 1) Время O(n³ log n)
# 2) Память O(n)

# nums = [1, 2, 3, 4]

# def incremovableSubarrayCount(nums):
#     count = 0
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums) + 1):
#             l = nums[:i] + nums[j:]
#             if l == sorted(l) and len(l) == len(set(l)):
#                 count += 1
#     return count