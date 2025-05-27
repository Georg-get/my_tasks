### Условие задачи:
# Учитывая целочисленный массив с нулевым индексомnums , определите, существуют ли два подмассива длины 2с одинаковой суммой.
# Обратите внимание, что два подмассива должны начинаться с разных индексов.
# Возврат true, если эти подмассивы существуют, и falseв противном случае.
# Подмассив — это непрерывная непустая последовательность элементов массива.

# Example 1:
# Input: nums = [4,2,4]
# Output: true
# Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.

# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: false
# Explanation: No two subarrays of size 2 have the same sum.

# Example 3:
# Input: nums = [0,0,0]
# Output: true
# Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
# Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.

### Краткое условие:
# Если есть две пары чисел в которых есть одинаковые числа то вернуть True, иначе False.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по диапазону (длины массива nums -1),
# 1.1) Создаем переменную s, в которой храниться значение элемента массива i + (значение элемента массива+1).
# 1.2) Если ключ s есть в словаре dict, верни True.
# 1.3) Присваемываем значение ключа s True.
# 2) Вернуть False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1) (n)

nums = [1, 2, 3, 4, 5]

def findSubarrays(nums):
    dict = {}
                    # 5
    for i in range(len(nums) - 1):  # range(0, 4)
        s = nums[i] + nums[i + 1]  # s=1+(1+1) = 3

        if s in dict:
            # {6: True} - это первый унитест !!!
            # {0: True} - это третий унитест !!!
            return True

        dict[s] = True  # {3: True}

    return False

findSubarrays(nums)

assert findSubarrays(nums=[4, 2, 4]) == True
assert findSubarrays(nums=[1, 2, 3, 4, 5]) == False
assert findSubarrays(nums=[0, 0, 0]) == True
assert findSubarrays(nums=[1, 2, 3, 1, 0, 2]) == False # этот юнитест не пропускает нижние решение !!!

### Не проходят все тесыт 39 / 42 !!!!
#
# nums = [1, 2, 3, 4, 5]
#
# def findSubarrays(nums):
#
#     if nums == [0, 0]:
#         return False
#
#     dict = {}
#     result = []
#
#     for i in nums:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
#     for j in dict:
#         if dict[j] > 1:
#             result.append(j)
#     # []
#     if len(result) == 0:
#         return False
#     else:
#         return True
#
# findSubarrays(nums)