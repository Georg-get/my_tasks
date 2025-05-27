### Условие задачи:
# Вам даны два целочисленных массива с нулевым индексом nums1 и nums2 размеров n и m соответственно.
# Рассмотрим расчет следующих значений:
# Число индексов i таких, что 0 <= i < nи nums1[i]встречается хотя бы один раз в nums2.
# Число индексов i таких, что 0 <= i < mи nums2[i]встречается хотя бы один раз в nums1.
# Возвращает целочисленный массив answer размера 2, содержащего два значения в указанном выше порядке.

# Example 1:
# Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]
# Output: [3,4]
# Explanation: We calculate the values as follows:
# - The elements at indices 1, 2, and 3 in nums1 occur at least once in nums2. So the first value is 3.
# - The elements at indices 0, 1, 3, and 4 in nums2 occur at least once in nums1. So the second value is 4.

# Example 2:
# Input: nums1 = [3,4,2,3], nums2 = [1,5]
# Output: [0,0]
# Explanation: There are no common elements between the two arrays, so the two values will be 0.

### Краткое условие:
# Надо сравнить два массива nums1 и nums2,
# вернуть массив с максивалным числом повторяющися элементов из двух массивов.

# Алгоритм решение задачи:
# 0) Создаем :
# 0.1) словарь setArryNums1 в котором будут храниться НЕ повторяющеся элементы массива nums1.
# 0.2) словарь setArryNums2 в котором будут храниться НЕ повторяющеся элементы массива nums2.
# 0.3) Переменные result1 и result2 со значением 0.
# 1) Проходимся циклом по массиву nums1.
# 1.1) Если i есть в словаре setArryNums2, то увеличь значение переменной result1 на 1.
# 2) Проходимся циклом по массиву nums2.
# 2.1) Если i есть в словаре setArryNums1, то увеличь значение переменной result2 на 1.
# 3) Верни массив из значений result1 и result2.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums1 = [4, 3, 2, 3, 1]  # [3,2,3] есть в массиве nums2, 3 раза повторяются числа в массиве nums1.
nums2 = [2, 2, 5, 2, 3, 6]  # [2,2,2,3] есть в массиве nums1, 4 раза повторяются числа в массиве nums2.

def findIntersectionValues(nums1, nums2):
    setArryNums1 = set(nums1) # {1, 2, 3, 4}
    setArryNums2 = set(nums2) # {2, 3, 5, 6}
    result1 = 0
    result2 = 0

    for i in nums1:
        if i in setArryNums2:
            result1 += 1
    # result1 = 3
    # setArryNums2 = {2, 3, 5, 6}
    for j in nums2:
        if j in setArryNums1:
            result2 += 1
    # result2 = 4
    # setArryNums1 = {1, 2, 3, 4}
    return [result1, result2]

findIntersectionValues(nums1, nums2)

assert findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]) == [3, 4]
assert findIntersectionValues(nums1=[3, 4, 2, 3], nums2=[1, 5]) == [0, 0]