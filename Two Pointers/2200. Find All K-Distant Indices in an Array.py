### Условие задачи:
# Вам дан целочисленный массив с нулевым индексом nums и два целых числа key и k. K -дистантный индекс — это индекс,
# i для nums которого существует хотя бы один индекс j такой, что |i - j| <= kи nums[j] == key.
# Возвращает список всех k-отстоящих индексов, отсортированных в порядке возрастания.

# Example 1:
# Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
# Output: [1,2,3,4,5,6]
# Explanation: Here, nums[2] == key and nums[5] == key.
# - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. Thus, 0 is not a k-distant index.
# - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
# - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
# - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
# - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
# - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
# - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
# Thus, we return [1,2,3,4,5,6] which is sorted in increasing order.

# Example 2:
# Input: nums = [2,2,2,2,2], key = 2, k = 2
# Output: [0,1,2,3,4]
# Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index.
# Hence, we return [0,1,2,3,4].

                                    ### Добавить в список !

### Краткое условие:
# Возвращает список всех k-отстоящих индексов, отсортированных в порядке возрастания.

                        #           Через хэш сет, без двух указателей.
# Алгоритм решение задачи:
# 0) Создаем пустое множество result.
# 1) Проходимся циклом по диапазону длины массива nums,
# 1.1) Если nums[i] равно key,
# 1.1.1) Проходимся циклом по диапазону от i - k до i + k + 1,
# 1.1.1.1) Если 0 меньше или равен j меньше или равен длина массива nums -1, то добавь в словарь result значение j.
# 2) Верни массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)


# nums = [3, 4, 9, 1, 3, 9, 5]
# key = 9
# k = 1
#
# def findKDistantIndices(nums, key, k):
#     result = set()
#
#     for i in range(len(nums)):
#         if nums[i] == key:
#             for j in range(i - k, i + k + 1):
#                 if 0 <= j <= len(nums) - 1:
#                     result.add(j)
#
#     return list(result)
#
# findKDistantIndices(nums, key, k)

                                        ### Два указателя !!!!
# Алгоритм решение задачи:
# 0) Задаем левый и правый указатель, и пустой массив result.
# 1) Проходимся циклом ваил пока правый и левый указатель не дойдут до конца строки одновременно.
# 1.1) Если число из массива nums где установлен правый указатель не равно числу key, то двигай правый указатель вперед.
# 1.2) Иначе,
# 1.2.1) Если ли индекс `left` на расстоянии не более `k` от индекса `right`, то добавь в массив result индекс числа left.
# 1.2.2) Если ли индекс `left` на расстоянии больше чем `k` от индекса `right`, и left больше right, увеличь right на 1.
# 1.2.3) Иначе увеличь left на 1.
# 2) Верни массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1

def findKDistantIndices(nums, key, k):
    left = 0
    right = 0
    result = []

    while right < len(nums) and left < len(nums):
        if nums[right] != key:
            right += 1
        else:
            if abs(left - right) <= k:   # abs переводит отрицательные числа в положительные. Было -2 стало 2.
                result.append(left)

            if abs(left - right) > k and left > right:
                right += 1
            else:
                left += 1
    # [1, 2, 3, 4, 5, 6]
    return result

findKDistantIndices(nums, key, k)

assert findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1) == [1, 2, 3, 4, 5, 6]
assert findKDistantIndices(nums=[2, 2, 2, 2, 2], key=2, k=2) == [0, 1, 2, 3, 4]