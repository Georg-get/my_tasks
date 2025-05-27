### Условие задачи:
# Дан массив целых чисел nums, не содержащий нулей, найдите наибольшее положительное целое число k,
# которое -k также существует в этом массиве.
# Вернуть положительное целое число k. Если такого целого числа нет, верните -1.

# Example 1:
# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.

# Example 2:
# Input: nums = [-1,10,6,7,-7,1]
# Output: 7
# Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

# Example 3:
# Input: nums = [-10,8,6,7,-2,-3]
# Output: -1
# Explanation: There is no a single valid k, we return -1.

### Краткое условие:
# Вернуть число, которое повторяется в массиве nums, даже есть оно отрицательное.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dictSet с set и переменную result со значением -1.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если ключ -i есть в словаре dictSet и ключ i больше переменной result, то присвой переменной result значение i.
# 2) Вернуть переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [-1, 2, -3, 3]

def findMaxK(nums):
    dictSet = set(nums) # {2, 3, -3, -1}
    result = -1

    for i in nums:
        if -i in dictSet and i > result:
            result = i
            
    return result # 3

findMaxK(nums)

assert findMaxK(nums=[-1, 2, -3, 3]) == 3
assert findMaxK(nums=[-1, 10, 6, 7, -7, 1]) == 7
assert findMaxK(nums=[-10, 8, 6, 7, -2, -3]) == -1