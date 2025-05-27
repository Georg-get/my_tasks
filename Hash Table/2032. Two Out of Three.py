### Условие задачи:
# Учитывая три целочисленных массива nums1, nums2 и nums3, верните отдельный массив,
# содержащий все значения, которые присутствуют как минимум в двух из трех массивов.
# Вы можете возвращать значения в любом порядке.

# Example 1:
# Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# Output: [3,2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.

# Example 2:
# Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
# Output: [2,3,1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3.

# Example 3:
# Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
# Output: []
# Explanation: No value is present in at least two arrays.

### Краткое условие:
# Вернуть массив чисел которые больше всего повторяются, отсортированый по убыванию повторений.

                             ### ТУТ ПРОБЛЕМЫ С ТЕСТОВЫМИ ДАННАМИ !!!! ####
                                        ### Хэш табшицы ###
# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result, и массив nums в котором будет 3 массива (без повторяющеся числел у нутри себя).
# 1) Пройтись циклом по массиву nums,
# 1.1) Добавить i как ключ со значением (1 + значение ключа i) в словарь dict.
# 1.2) Если значение ключа i в словаре dict равно 2, то добавь i в массив result.
# 2) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]

def twoOutOfThree(nums1, nums2, nums3):
    dict = {}
    result = []
    nums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))  # [1, 2, 3, 2, 3, 3]

    for i in nums:
        dict[i] = 1 + dict.get(i, 0)
        if dict[i] == 2:
            result.append(i)

    return result # [2, 3]

twoOutOfThree(nums1, nums2, nums3)

assert twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]) == [3, 2]
assert twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2]) == [1, 2, 3]
assert twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]) == []

                            ### Хэш сет
# Алгоритм решение задачи:
# 0) Вернуть массив из множества массива nums1 и множество массива nums2,
# или множества массива nums2 и множество массива nums3,
# или множества массива nums1 и множество массива nums3.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

# nums1 = [1, 1, 3, 2]
# nums2 = [2, 3]
# nums3 = [3]
#
# def twoOutOfThree(nums1, nums2, nums3):
#     return list(set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3))
#
# twoOutOfThree(nums1, nums2, nums3)