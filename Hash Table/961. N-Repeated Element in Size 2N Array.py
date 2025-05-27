### Условие задачи:
# Вам дан целочисленный массив nums со следующими свойствами:
# nums.length == 2 * n.
# nums содержит n + 1 уникальные элементы.
# Ровно один элемент nums повторяется n раз.
# Возвращает элемент, который повторяется n несколько раз.

# Example 1:
# Input: nums = [1,2,3,3]
# Output: 3

# Example 2:
# Input: nums = [2,1,2,5,3,2]
# Output: 2

# Example 3:
# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5

### Краткое условие:
# Вывести число которое больше всего повторяется в массиве nums.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если i есть в словаре dict, то увеличь значение ключа на 1.
# 1.2) Если i НЕТу в словаре dict, то добавь i как ключ со значением 0.
# 2) Верни ключ с максимальным значением в словаре dict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [5, 1, 5, 2, 5, 3, 5, 4]

def repeatedNTimes(nums):
    dict = {}

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 0
    # {5: 3, 1: 0, 2: 0, 3: 0, 4: 0}
    return max(dict, key=dict.get) #5

repeatedNTimes(nums)

assert repeatedNTimes(nums=[1, 2, 3, 3]) == 3
assert repeatedNTimes(nums=[2, 1, 2, 5, 3, 2]) == 2
assert repeatedNTimes(nums=[5, 1, 5, 2, 5, 3, 5, 4]) == 5