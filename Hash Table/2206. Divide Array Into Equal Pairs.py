### Условие задачи:
# Вам дан целочисленный массив, nums состоящий из 2 * n целых чисел.
# Вам нужно разделиться nums на n пары так, чтобы:
# Каждый элемент принадлежит ровно одной паре.
# Элементы, присутствующие в паре, равны.
# Возврат true, если числа можно разделить на n пары, в противном случае возврат false.

# Example 1:
# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation:
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

### Краткое условие:
# Надо разделить длину массива nums на 2 и если получеться число количество пар то вернуть True,
# а если число пар не получится вернуть False.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Пройтись циклом по массиву nums,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение этого ключа на 1.
# 1.2) Если ключа i НЕТу в словаре dict, то добавь его со значением 1.
# 2) Пройтись циклом по словарю dict,
# 2.1) Если значение ключа dict[j] делеться на 2 и равно 0, то верни False.
# 3) Верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [3, 2, 3, 2, 2, 2]

def divideArray(nums):
    dict = {}

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {3: 2, 2: 4}
    for j in dict:
        if dict[j] % 2 == 1:  # все значение ключей в словаре делятся на 2 без остатка !
            return False
    # {3: 2, 2: 4}
    return True

divideArray(nums)

assert divideArray(nums=[3, 2, 3, 2, 2, 2]) == True
assert divideArray(nums=[1, 2, 3, 4]) == False