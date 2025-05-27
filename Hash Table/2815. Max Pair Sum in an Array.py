### Условие задачи:
# Вам дан целочисленный массив с нулевым индексом nums.
# Вам необходимо найти максимальную сумму пары чисел из nums таких, чтобы максимальная цифра в обоих числах была равна.
# Возвращает максимальную сумму или, -1 если такой пары не существует.

# Example 1:
# Input: nums = [51,71,17,24,42]
# Output: 88
# Explanation:
# For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88.
# For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.
# It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: No pair exists in nums with equal maximum digits.

                                                ### Добавить в список !

### Краткое условие:
# Надо сложить максивальное и минимальное число из массива nums и результат будет палендромом.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result равную -1.
# 1) Проходимся циклом по массиву nums,
# 1.1) Присваеваем x значение функции для поиска максивального числа из двухзначного числа.
# 1.2) Если x есть в словаре dict, то присвой переменной result значение ключа x+i и переменной result,
# и ключ x сделай со значениме i.
# 1.3) Если x НЕТу в словаре dict, то добавь ключ x со значениме i.
# 2) Верни переменную result

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

nums = [51, 71, 17, 24, 42]

def maxSum(nums):
    dict = {}
    result = -1

    def findMax(n):
        a = 0
        while n > 0:
            a = max(a, n % 10)  # 51
            n //= 10  # 1
        #      5
        return a

    for i in nums:
        # 51
        x = findMax(i)  # 5
        if x in dict:
            result = max(dict[x] + i, result)
            dict[x] = max(dict[x], i)
        else:
            dict[x] = i
    # 88
    return result

maxSum(nums)

assert maxSum(nums=[51, 71, 17, 24, 42]) == 88
assert maxSum(nums=[1, 2, 3, 4]) == -1