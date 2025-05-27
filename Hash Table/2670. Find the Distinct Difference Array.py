### Условие задачи:
# Вам дан массив с нулевым индексом nums длиной n.
# Массив различных разностей — nums это массив такой diff длины , которая равна количеству различных элементов в суффиксе,
# вычтенному из количества различных элементов в префиксе .ndiff[i]nums[i + 1, ..., n - 1] nums[0, ..., i]
# Верните массив различных разностей nums.
# Обратите внимание, что это nums[i, ..., j]означает под массив,
# nums начинающийся с индекса i и заканчивающийся индексом j включительно.
# В частности, if i > j then nums[i, ..., j]обозначает пустой под массив.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: [-3,-1,1,3,5]
# Explanation: For index i = 0, there is 1 element in the prefix and 4 distinct elements in the suffix. Thus, diff[0] = 1 - 4 = -3.
# For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
# For index i = 2, there are 3 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 3 - 2 = 1.
# For index i = 3, there are 4 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 4 - 1 = 3.
# For index i = 4, there are 5 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 5 - 0 = 5.

# Example 2:
# Input: nums = [3,2,3,4,2]
# Output: [-2,-1,0,2,3]
# Explanation: For index i = 0, there is 1 element in the prefix and 3 distinct elements in the suffix. Thus, diff[0] = 1 - 3 = -2.
# For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
# For index i = 2, there are 2 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 2 - 2 = 0.
# For index i = 3, there are 3 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 3 - 1 = 2.
# For index i = 4, there are 3 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 3 - 0 = 3.


                                            ### Добавить в список !
### Краткое условие:
# Верните массив различных разностей nums.
# Вернуть массив дифоф, диф = элемент в массиве - (длина масива- номер элемента массива который мы хотим вычисть).

# Алгоритм решение задачи:
# 0) Создаем два пустых словаря dict1 и dict2, и пустой массив result.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если i есть как ключа в словаре dict1, то увеличь значение ключа на 1.
# 1.2) Если i НЕТу как ключа в словаре dict1, то добавь ключ i со значением 1.
# 2) Проходимся циклом по массиву nums,
# 2.1) Если j есть как ключа в словаре dict2, то увеличь значение ключа на 1.
# 2.2) Если j НЕТу как ключа в словаре dict2, то добавь ключ j со значением 1.
# 2.3) Вычитаем уменьшаем значение ключа dict1[j] на 1, если dict1[j] равен 0, то удаляем это ключ с dict1[j] со значением.
# 2.4) Добавляем в массив result, значение = длина словаря dict2 - длина словаря dict1.
# 3) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

nums = [1, 2, 3, 4, 5]

def distinctDifferenceArray(nums):
    dict1 = {}
    dict2 = {}
    result = []

    for i in nums:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
    # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}

    for j in nums:
        if j in dict2:
            dict2[j] += 1
        else:
            dict2[j] = 1
        # print(dict1) {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
        # print(dict2) {1: 1}
        dict1[j] -= 1
        # print(dict1) {1: 0, 2: 1, 3: 1, 4: 1, 5: 1}
        if (dict1[j] == 0):
            del dict1[j]
            # print(dict1) {2: 1, 3: 1, 4: 1, 5: 1}
        # print(dict1) {2: 1, 3: 1, 4: 1, 5: 1}
        # print(dict2) {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
        #                       1       -   4 = -3
        result.append(len(dict2.keys()) - len(dict1.keys()))

    return result  # [-3,-1,1,3,5]

distinctDifferenceArray(nums)

assert distinctDifferenceArray(nums=[1, 2, 3, 4, 5]) == [-3, -1, 1, 3, 5]
assert distinctDifferenceArray(nums=[3, 2, 3, 4, 2]) == [-2, -1, 0, 2, 3]