### Условие задачи:
# Учитывая два целочисленных массива nums1 и nums2, верните массив их пересечения.
# Каждый элемент результата должен появляться столько раз, сколько он отображается в обоих массивах,
# и вы можете возвращать результат в любом порядке.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

### Краткое условие:
# Надо найти массив пересечений двух массивов. Повторяющие элементы должны быть добавлены все. ВСЕ ПОВТОРЯЮЩИСЯ ЭЛЕМЕНТЫ !!!

# Алгоритм решение задачи:
# 0) Создать массив result.
# 1) Отсортировать два массива (nums1 и nums2) по возврастанию.
# 2) Написать функцию бинарного поиска
# 2.1) Если элемент совпадает с target, он удаляется из списка nums2, чтобы избежать повторений.
# 2.2) Если элемент > target, то двигай мид в права.
# 2.3) Если элемент < target, то двигай мид в лева.
# 3) Проходимся циклом по массиву nums1,
# 3.1) Если элементн из массива nums1 находиться функцией бинанрного поиска, то добавь его в массив result.
# 4) Верни return result.

# Сложность:
# 1) Время O(m log n)
# 2) Память O(n)

nums1 = [1, 2, 2, 1]
nums2 = [2]

def intersect(nums1, nums2):
    def binarySearch(nums2, target):
        left = 0
        right = len(nums2) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums2[mid] == target:
                del nums2[mid]
                return True

            elif nums2[mid] > target:
                right = mid - 1

            elif nums2[mid] < target:
                left = mid + 1

    nums1.sort()  # [1, 1, 2, 2]
    nums2.sort()  # [2]
    result = []

    for i in nums1:
        if binarySearch(nums2, i):
            result.append(i)
    #       [2]
    return result

intersect(nums1, nums2)

assert intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]) == [2, 2]
assert intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [4, 9]