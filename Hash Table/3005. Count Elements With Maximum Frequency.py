### Условие задачи:
# Вам дан массив nums, состоящий из целых положительных чисел.
# Возвращает общие частоты элементов так, чтобы все эти элементы имели максимальную частоту. nums
# Частота элемента — это количество вхождений этого элемента в массив.

# Example 1:
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.

# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.

### Краткое условие:
# Надо вернуть количестов максивальных повторений в массиву nums,
# если повторений нету то вернуть количество чисел в массиве.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result со значением 0.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Если ключ i НЕТу в словаре dict, то добавь ключа i со значением 1 в словарь dict.
# 2) Создаем переменную maxMeaningDict со значением максимального значение из словаря dict.
# 3) Проходимся циклом по словарю dict,
# 3.1) Если значение ключа j равно переменной maxMeaningDict, то увеличь переменную result на dict[j].
# 4) Вернуть переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [17, 17, 2, 12, 20, 17, 12]

def maxFrequencyElements(nums):
    dict = {}
    result = 0

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {17: 3, 2: 1, 12: 2, 20: 1}
    maxMeaningDict = max(dict.values())
    # 3
    for j in dict:
        if dict[j] == maxMeaningDict:
            result += dict[j]

    return result  # 3

maxFrequencyElements(nums)

assert maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]) == 4
assert maxFrequencyElements(nums=[1, 2, 3, 4, 5]) == 5
assert maxFrequencyElements(nums=[17, 17, 2, 12, 20, 17, 12]) == 3
assert maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]) == 4