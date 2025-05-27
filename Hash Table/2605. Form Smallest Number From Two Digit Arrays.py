### Условие задачи:
# Учитывая два массива уникальных цифр nums1и nums2, верните наименьшее число , содержащее хотя бы одну цифру из каждого массива .

# Example 1:
# Input: nums1 = [4,1,3], nums2 = [5,7]
# Output: 15
# Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.

# Example 2:
# Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
# Output: 3
# Explanation: The number 3 contains the digit 3 which exists in both arrays.

### Краткое условие:
# Вернуть число, которое повторяется в двух массивах nums1 и nums2,
# Если нету такого числа вернуть строку из двух минимальных числел из друх массивов

# Алгоритм решение задачи:
# 0) Создаем массив allList с элементыми из массивов nums1+nums2 без повторений.
# 1) Проходимся циклом по масству allList,
# 1.1) Если число i есть в массиве nums1 и в массиве nums2, то верни i.
# 2) Если минимальное число из массива nums2 больше минимальное число из массива nums1,
# 2.1) То верни число из двух минимальных числе из массива nums2 и nums1.
# 3) Если минимальное число из массива nums2 НЕ больше минимальное число из массива nums1,
# 3.1) То верни число из двух минимальных числе из массива nums1 и nums2.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums1 = [4, 1, 3]
nums2 = [5, 7]

def minNumber(nums1, nums2):
    allList = list(set(nums1 + nums2))
    # [1, 2, 3, 5, 6, 7]

    for i in allList:
        if i in nums1 and i in nums2:
            return i # 3

    if min(nums2) < min(nums1):
        return int(str(min(nums2)) + str(min(nums1)))
    else:
        return int(str(min(nums1)) + str(min(nums2)))

minNumber(nums1, nums2)

assert minNumber(nums1=[4, 1, 3], nums2=[5, 7]) == 15
assert minNumber(nums1=[3, 5, 2, 6], nums2=[3, 1, 7]) == 3