### Условие задачи:
# Вам дан целочисленный массив nums. Мы считаем массив хорошим , если он является перестановкой массива base[n].
# base[n] = [1, 2, ..., n - 1, n, n] (другими словами, это массив длины n + 1,
# который содержит 1ровно n - 1 один раз плюс два вхождения n). Например, base[1] = [1, 1]и  base[3] = [1, 2, 3, 3].
# Возврат true , если данный массив хорош, в противном случае возврат . false
# Примечание. Перестановка целых чисел представляет собой расположение этих чисел.

# Example 1:
# Input: nums = [2, 1, 3]
# Output: false
# Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

# Example 2:
# Input: nums = [1, 3, 3, 2]
# Output: true
# Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.

# Example 3:
# Input: nums = [1, 1]
# Output: true
# Explanation: Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.

# Example 4:
# Input: nums = [3, 4, 4, 1, 2, 1]
# Output: false
# Explanation: Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.

### Добавить в список !

### Краткое условие:
# Верните true, если данный массив "хороший", в противном случае верните false.

# Краткое объяснение решение задачи:
# Проверяет, что:
#    - Максимальное значение в nums встречается ровно 2 раза
#    - Длина списка равна максимальному значению в nums + 1.
#    - В списке уникальных значений столько же, сколько максимальное значение в nums.
# Если все условия выполняются, возвращаем True, иначе — False.

# Полное объяснение решение задачи:
# 0) Создаем переменную maximumValueNums со значением максивального числа из массива nums.
# 1) Если число которое самое максивальное повторяется 2 раза в массиве nums и длина массива равна maximumValueNums + 1 и длина множества без дубликатов массива nums равна maximumValueNums,
# 1.1) То верни True.
# 2) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

### Сложная задача !!!

nums = [1, 3, 3, 2]

def isGood(nums):


    maximumValueNums = max(nums)  # 3

    # 2 (сколько раз повторяется 3 в массиве nums)
    # 4          # 3  + 1               # 3                 # 3
    if nums.count(maximumValueNums) == 2 and len(nums) == maximumValueNums + 1 and len(set(nums)) == maximumValueNums:
        return True
    else:
        return False

isGood(nums)

assert isGood(nums=[2, 1, 3]) == False
assert isGood(nums=[1, 3, 3, 2]) == True
assert isGood(nums=[1, 1]) == True
assert isGood(nums=[3, 4, 4, 1, 2, 1]) == False
# Доп юнитесты для проверки некоторых условий:
# assert isGood(nums=[]) == False  # Проверка на пустой массив

### Старый рабочий код c хэш таблицей !!! ###

# Полное объяснение решение задачи:
# 0) Создаем переменную lenNums со значением длинны массива nums -1 и пустой словарь dict.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если n больше lenNums, то верни False.
# 1.2) Если ключа n нету в словаре dict, то добавь этот ключ n со значением 1 в словарь dict.
# 1.3) Если ключа n есть в словаре dict, то если n равно lenNums и значение ключ n равно 1, то значение ключа n равно 2.
# 1.4) Если ключа n НЕТу в словаре dict, то верни False.
# 2) Проходимся циклом по диапазону (от 1 до lenNums+1), Если ключа i нету в словаре dict, то верни False.
# 3) Верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

# nums = [1, 3, 3, 2]
#
# def isGood(nums):
#     lenNums = len(nums) - 1
#     dict = {}
#
#     for n in nums:
#         if n > lenNums:
#             return False
#
#         if n not in dict:
#             dict[n] = 1
#         else:
#             if n == lenNums and dict[n] == 1:
#                 dict[n] = 2
#             else:
#                 return False
#     # {1: 1, 3: 2, 2: 1}
#     for i in range(1, lenNums + 1):  # range(1, 4)
#         if i not in dict:
#             return False
#
#     return True
