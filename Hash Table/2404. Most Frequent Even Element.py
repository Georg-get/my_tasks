### Условие задачи:
# Учитывая целочисленный массив nums, верните наиболее часто встречающийся четный элемент.
# Если есть ничья, верните наименьшую. Если такого элемента нет, верните -1.

# Example 1:
# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.

# Example 2:
# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.

# Example 3:
# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.

### Краткое условие:
# Необходимо вернуть наиболее часто встречающийся четный элемент.
# Если есть несколько таких элементов, вернуть наименьший из них.
# Если четных элементов нет, вернуть -1.

# Краткое объяснение решение задачи:
# Создается словарь dict для подсчета частоты четных чисел.
# Проходя по списку, добавляет только четные числа в словарь и увеличивает их счетчик при повторение числа.
# Если в словаре есть четные числа, то возвращает минимальное из наиболее частых четных чисел или -1, если четных чисел нет.

# Полное объяснение решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если i четное число,
# 1.1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.1.2) Иначе, добавь ключ i со значением 1 в словарь.
# 2) Если длина словаря dict больше 0,
# 2.1) Проходимся циклом по словарю dict,
# 2.1.1) Если значение ключа value равно максимальному значениею в словаре dict, то в массив result добавь key.
# 2.1.3) Верни минимальное число из массива result.
# 3) Иначе верни -1.

# Сложность:
# 1) Время O(m)
# 2) Память O(n)

nums = [0, 1, 2, 2, 4, 4, 1]

def mostFrequentEven(nums):
    dict = {}
    result = []

    for i in nums:
        if i % 2 == 0:  # не пускаем не четные числа в словарь dict !!!
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    # {'0': 1, '2': 2, '4': 2}
    if len(dict) > 0:

        for key, value in dict.items():
            if value == max(dict.values()):
                result.append(key)
        # result = [2,4]
        return min(result)  # 2

    else:
        return -1

mostFrequentEven(nums)

assert mostFrequentEven(nums=[0, 1, 2, 2, 4, 4, 1]) == 2
assert mostFrequentEven(nums=[4, 4, 4, 9, 2, 4]) == 4
assert mostFrequentEven(nums=[29, 47, 21, 41, 13, 37, 25, 7]) == -1  # ВСЕ ЧИСЛА НЕ ЧЕТНЫЕ !!!
assert mostFrequentEven(nums=[10000]) == 10000
assert mostFrequentEven(nums=[0, 0, 0, 0]) == 0  # тут падает мое решение
assert mostFrequentEven(
    nums=[8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]) == 3346  # тут падает мое решение
# Доп юнитесты для проверки некоторых условий:
assert mostFrequentEven(nums=[]) == -1  # Тест с пустым массивом
assert mostFrequentEven(nums=[0, 0, 1, 1]) == 0  # Тест с нулями
assert mostFrequentEven(nums=[2, 2, 2, 2]) == 2  # Тест с несколькими одинаковыми четными элементами
assert mostFrequentEven(nums=[1, 3, 5]) == -1  # Тест без четных элементов
assert mostFrequentEven(nums=[1, 3, 5, 2]) == 2  # Тест с одним четным элементом

### Не проходят все тесыт 50 / 219!!!!
#
# nums = [0, 1, 2, 2, 4, 4, 1]
#
# def mostFrequentEven(nums):
#     if len(nums) == 1:
#         return int(nums[0]) # защита от тесткейса 4 !!!
#
#     dict = {}
#     result = []
#
#     for i in nums:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     # {0: 1, 1: 2, 2: 2, 4: 2}
#     maxMeaningDict = max(dict.values()) # 2
#
#     for j in dict:
#         if dict[j] == maxMeaningDict and maxMeaningDict > 1 and j != 1:
#             result.append(j)
#     # [2, 4]
#     if len(result) == 0:
#         return -1
#     else:
#         return result[0] * 1
# mostFrequentEven(nums)