### Условие задачи:

# Example 1:
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

# Example 2:
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

# Example 3:
# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]

### Краткое условие:
# Отсортировать массив в порядке убывание повторяющих пар числе из массива nums.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result
# 1) Проходимся циклом по массиву nums,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа на 1.
# 1.2) Если ключ i НЕТу в словаре dict, то добавь ключа i со значением 1 в словарь dict.
# 2) Сортируем массив result, по возрастанию ключей словаря dict.
# 3) Вернуть массив result.

# Сложность:
# 1) Время O(n) (n log n)
# 2) Память O(n)

nums = [1, 1, 2, 2, 2, 3]

def frequencySort(nums):
    def customKey(j):
        return dict[j], -j

    dict = {}
    result = []

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {1: 2, 2: 3, 3: 1}
    # {3:1, 1:2, 2:3}
    result = sorted(nums, key=customKey)
    # result = sorted(nums, key=lambda x: (dict[x], -x))
    # [3, 1, 1, 2, 2, 2]
    return result

frequencySort(nums)

assert frequencySort(nums=[1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]
assert frequencySort(nums=[2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]
assert frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1]