### Условие задачи:
# Вам дан целочисленный массив nums.
# Уникальными элементами массива являются элементы, которые встречаются в массиве ровно один раз.
# Возвращает сумму всех уникальных элементов nums.

# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.

# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

### Краткое условие:
# Надо вернуть сумму всех элементов которые не повторяються в массиве nums.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result = 0 для подсчета суммы не повторяющеся чисел в массиве nums.
# 1) Пройтись циклом по массиву nums,
# 1.1) Если i есть в словаре dict, то увеличь этот ключ значение ключа на 1.
# 1.2) Если i нету в словаре dict, то добавь этот ключ со значением 0.
# 2) Пройтись циклом по словарю dict,
# 2.1) Если значение ключа равно 0, то увеличь значение переменной result на ключ.
# 3) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 2, 3, 2]

def sumOfUnique(nums):
    dict = {}
    result = 0

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 0
    # {1: 0, 2: 1, 3: 0}
    for j in dict:
        if dict[j] == 0:
            result += j
            # {(1): 0, 2: 1, (3): 0}
            # 1 + 3 = 4
    #       4
    return result

sumOfUnique(nums)

assert sumOfUnique(nums=[1, 2, 3, 2]) == 4
assert sumOfUnique(nums=[1, 1, 1, 1, 1]) == 0
assert sumOfUnique(nums=[1, 2, 3, 4, 5]) == 15