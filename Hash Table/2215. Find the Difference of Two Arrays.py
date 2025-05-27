### Условие задачи:
# Учитывая два целочисленных массива с нулевым индексом nums1 и nums2, верните список answer размера, 2 где:
# answer[0] представляет собой список всех различных целых чисел, в nums1 которых нет в nums2.
# answer[1] представляет собой список всех различных целых чисел, в nums2 которых нет в nums1.
# Обратите внимание, что целые числа в списках могут возвращаться в любом порядке.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

# Example 2:
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

### Краткое условие:
# Вернуть матрицу с не повторяющимся элементами в массивах nums1 и nums2.

# Алгоритм решение задачи:
# 0) Создаем два словаря setNums1 = set(nums1) и setNums2 = set(nums2), и два пустых массива resultNums1 и resultNums2.
# 1) Проходимся циклом по словарю setNums1,
# 1.1) Если i нету в словаре setNums2, то добавь i в массив resultNums1.
# 2) Проходимся циклом по словарю setNums2,
# 2.2) Если j нету в словаре setNums1, то добавь j в массив resultNums2.
# 3) Вернуть массив в котором будет два массива resultNums1 и resultNums2 [resultNums1, resultNums2].

# Сложность:
# 1) Время O(n + m) (n)
# 2) Память O(n)

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

def findDifference(nums1, nums2):
    setNums1 = set(nums1)  # {1, 2, 3}
    setNums2 = set(nums2)  # {2, 4, 6}
    resultNums1 = []
    resultNums2 = []

    for i in setNums1:
        if i not in setNums2:
            resultNums1.append(i)
    # [1, 3]
    for j in setNums2:
        if j not in setNums1:
            resultNums2.append(j)
    # [4, 6]
    return [resultNums1, resultNums2]  # [[1, 3],[4, 6]]


findDifference(nums1, nums2)

assert findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]) == [[1, 3], [4, 6]]
assert findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]) == [[3], []]