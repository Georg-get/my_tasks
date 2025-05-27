### Условие задачи:
# Вам дан целочисленный массив четной nums длины. Вам нужно разделить массив на две части и так, чтобы: nums1 nums2
# nums1.length == nums2.length == nums.length / 2.
# nums1 должен содержать отдельные элементы.
# nums2 также должен содержать отдельные элементы.
# Возвращает true, если можно разделить массив, и false в противном случае.

# Example 1:
# Input: nums = [1,1,2,2,3,4]
# Output: true
# Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

# Example 2:
# Input: nums = [1,1,1,1]
# Output: false
# Explanation: The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.

### Краткое условие:
# Если массив nums с дубликатами можно разделить на два массива то вернуть true, иначе false.
# Разделить массив nums на два равных массива nums1 и nums2.

# Алгоритм решение задачи:
# 0) Создаем словарь dict.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Иначе добавляем ключ i со значением 1 в словарь dict.
# 2) Проходимся циклом по значениям словаря dict,
# 2.1) Если значение словаря dict больше двух, то вернуть False.
# 3) Верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 1, 2, 2, 3, 4]

def isPossibleToSplit(nums):
    dict = {}

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {1: 2, 2: 2, 3: 1, 4: 1}
    for j in dict.values():
        if j > 2: # у нас нету ключа у которого значение будет больше 2 ! -> Из-за этого вернется True !
            return False

    return True

isPossibleToSplit(nums)

assert isPossibleToSplit(nums=[1, 1, 2, 2, 3, 4]) == True
assert isPossibleToSplit(nums=[1, 1, 1, 1]) == False