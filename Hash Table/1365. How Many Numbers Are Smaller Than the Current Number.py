### Условие задачи:
# Учитывая массив nums, для каждого nums[i] найдите, сколько чисел в массиве меньше его.
# То есть для каждого nums[i] надо посчитать количество допустимых j s таких, что  j != i и nums[j] < nums[i] .
# Вернуть ответ в массиве.

# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]

# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]

### Краткое условие:
# Надо вернуть массив в котором будут номера индексов чисел из массива nums.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result.
# 0.1) Сортируем массив nums по возврастанию.
# 1) Проходимся циклом по диапазону длине отсортированого масссива nums.
# 1.1) Если такого ключа НЕТу в словаре dict, то добавь этот ключ со значением номера счетчика.
# 2) Проходим циклом по диапазону длине массива nums.
# 2.1) Берем элемент из массива nums и ищем такой ключ в словаре dict,
# 2.1.1) если такой ключ есть, то берем его значение из словаря dict и добавляем в массив result.
# 3) Вернуть массив result.

# Сложность:
# 1) Время O(n log n)
# 2) Память O(n)

nums = [8, 1, 2, 2, 3]

def smallerNumbersThanCurrent(nums):
    dict = {}
    result = []
    sortedArrayNums = sorted(nums)  # [1, 2, 2, 3, 8]

    for i in range(len(sortedArrayNums)):
        if not sortedArrayNums[i] in dict:
            dict[sortedArrayNums[i]] = i
    # {1: 0, 2: 1, 3: 3, 8: 4}
    for j in range(len(nums)):
        result.append(dict[nums[j]])
    # [4, 0, 1, 1, 3]
    return result

smallerNumbersThanCurrent(nums)

assert smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
assert smallerNumbersThanCurrent(nums=[6, 5, 4, 8]) == [2, 1, 0, 3]
assert smallerNumbersThanCurrent(nums=[7, 7, 7, 7]) == [0, 0, 0, 0]