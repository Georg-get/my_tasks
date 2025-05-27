### Условие задачи:
# Учитывая два целочисленных массива nums1 и nums2, верните массив их пересечения.
# Каждый элемент результата должен быть уникальным, и вы можете возвращать результат в любом порядке.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

                                    ### ТУТ ПРОБЛЕМЫ С ТЕСТОВЫМИ ДАННАМИ !!!! ####

### Краткое условие:
# Надо найти массив пересечений двух массивов. Повторяющие элементы должны пересекаться один раз. ОДНО ПОВТОРЯЮЩИЙ ЭЛЕМЕНТЫ !!!

# Алгоритм решение задачи:
# 0) Создать массив result.
# 1) Отсортировать два массива (nums1 и nums2) по возврастанию.
# 2) Далее происходит по элементам списка nums1.
# 2.1) Для каждого элемента из nums1 выполняется бинарный поиск в списке nums2.
# 2.2) Если элемент найден, и его значение еще не добавлено в result, то оно добавляется.
# 3) Вернуть массив result.

# Сложность:
# 1) Время O(m log n)
# 2) Память O(k)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

def intersection(nums1, nums2):
    nums1.sort()  # [1, 1, 2, 2]
    nums2.sort()  # [2, 2]
    result = []

    for i in nums1:

        left = 0
        right = len(nums2) - 1

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
    # [2]
    return result

intersection(nums1, nums2)

assert intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]) == [2]
assert intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [4, 9] # тут проблема с тестовыми даннами !!!