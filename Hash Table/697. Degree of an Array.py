### Условие задачи:
# Учитывая непустой массив неотрицательных целых чисел nums,
# степень этого массива определяется как максимальная частота любого из его элементов.
# Ваша задача — найти наименьшую возможную длину (непрерывного) подмассива nums, имеющего ту же степень, что и nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

                                            ### Добавить в список !

### Краткое условие:
# Найти наименьшую возможную длину (непрерывного) подмассива nums, имеющего ту же степень, что и nums.

# Алгоритм решение задачи:
# 0) Создаем 3 пустых словаря: degreeNums, left, right.
# 0.1) Создаем переменную degree со значением 0 и переменную shortest со значением длины массива nums.
# 1) Проходимся циклом по массу nums по его номерам элемента и значениям,
# 1.1) Если ключ num есть в словаре degreeNums, то увеличь значение ключа num на 1.
# 1.2) Если ключ num НЕТу в словаре degreeNums, то добавь ключ num со значение 1 в словарь degreeNums.
# 1.3) Присвой значение переменной degree максивальный элемент между degree и ключом в словаре degreeNums.
# 1.4) Если ключа num НЕТу в словаре left, то добавь ключ num со значением i в словарь left.
# 1.5) Добавляем ключ num со значением i в словарь right.
# 2) Проходимся циклом по значением словаря degreeNums,
# 2.1) Если freq равен degree, то найди самое минимальное число среди shortest и right[num] - left[num] + 1.
# 3) Верни shortest.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

nums = [1, 2, 2, 3, 1]

def findShortestSubArray(nums):
    degreeNums = {}
    left = {}
    right = {}
    degree = 0
    lenNums = len(nums)

    for i, num in enumerate(nums):
        if num in degreeNums:
            degreeNums[num] += 1
        else:
            degreeNums[num] = 1
        degree = max(degree, degreeNums[num])

        if num not in left:
            left[num] = i
        right[num] = i
    # {1: 2, 2: 2, 3: 1}
    # {1: 0, 2: 1, 3: 3}
    # {1: 4, 2: 2, 3: 3}
    for num, freq in degreeNums.items():
        if freq == degree:
            #              (5 ,         4       -   0       + 1)
            lenNums = min(lenNums, right[num] - left[num] + 1)  # 5

    return lenNums  # 2

findShortestSubArray(nums)

assert findShortestSubArray(nums=[1, 2, 2, 3, 1]) == 2
assert findShortestSubArray(nums=[1, 2, 2, 3, 1, 4, 2]) == 6