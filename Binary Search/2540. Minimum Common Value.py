### Условие задачи:
# Учитывая два целочисленных массива nums1 и nums2, отсортированные в порядке неубывания, верните минимальное целое число,
# общее для обоих массивов. nums1 Если среди и нет общего целого числа nums2, верните -1.
# Обратите внимание, что целое число считается общим для nums1и nums2,
# если оба массива имеют хотя бы одно вхождение этого целого числа.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.

# Example 2:
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

### Краткое условие:
# Если в массивах nums1 и nums2 нету общих числО то вернуть -1. Если есть одно общих числе, то надо вернуть его !

# Алгоритм решение задачи:
# 0) Создать пустой массив result.
# 1) Найди бинарным поискам похожие элементы в nums1 и nums2. Добавь эти элементы в массив result.
# 2) Если размер массив result равен 0, то верни return -1.
# 2.1) Если размер массив result НЕ равен 0, то верни return result[0].

# Сложность:
# 1) времени O(n log n))
# 2) памяти O(n)

nums1 = [1, 2, 3, 6]
nums2 = [2, 3, 4, 5]


def getCommon(nums1, nums2):
    result = []

    for i in nums1:

        left = 0
        right = len(nums2) - 1 # 3

        while left <= right:
            mid = (left + right) // 2

            if nums2[mid] == i:
                if nums2[mid] not in result:
                    result.append(nums2[mid])
                break

            elif i < nums2[mid]:
                right = mid - 1
            else:
                left = mid + 1
    # [2, 3]
    #       2      == 0
    if len(result) == 0:
        return -1
    else:
        #  2
        return result[0]  # 2 - тут закончиться ПЕРВЫЙ и ВТОРОЙ юнитест !!!

getCommon(nums1, nums2)

# assert getCommon(nums1=[1, 2, 3], nums2=[2, 4]) == 2
# assert getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]) == 2
# assert getCommon(nums1=[1, 2, 3, 6], nums2=[7, 8, 9, 10]) == -1


                                            # Через хэш таблицы
# class Solution:
#     def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
#         return min(set(nums1) & set(nums2), default=-1)