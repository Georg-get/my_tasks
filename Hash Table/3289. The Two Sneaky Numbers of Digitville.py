### Условие задачи:
# В городе Диджитвилль существовал список чисел, который назывался, nums содержащий целые числа от 0д о n - 1.
# Каждое число должно было встречаться в списке ровно один раз,
# однако два проказливых числа прокрались в список один раз, сделав список длиннее обычного.
# Как городской детектив, ваша задача — найти эти два подлых числа.
# Верните массив размером два, содержащий два числа (в любом порядке), чтобы мир мог вернуться в Диджитвилль.

# Example 1:
# Input: nums = [0,1,1,0]
# Output: [0,1]
# Explanation:
# The numbers 0 and 1 each appear twice in the array.

# Example 2:
# Input: nums = [0,3,2,1,3,2]
# Output: [2,3]
# Explanation:
# The numbers 2 and 3 each appear twice in the array.

# Example 3:
# Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]
# Output: [4,5]
# Explanation:
# The numbers 4 and 5 each appear twice in the array.

### Краткое условие:
# Надо вернуть массив в котором будет два самых популярныйх числа из массива nums.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Иначе, добавь ключ i со значением 1 в словарь dict.
# 2) Проходимся циклом по словарю dict,
# 2.1) Если значение val равно максивальному значению в словаре dict и массив result меньше 2, то в массив result добавь key.
# 3) Верни отсортированный массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [0, 1, 1, 0]

def getSneakyNumbers(nums):
    dict = {}
    result = []

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {0: 2, 1: 2}
    for key, val in dict.items():
        if val == max(dict.values()) and len(result) < 2:
            result.append(key)
    # [0, 1]
    return sorted(result) # от 2 юнитеста

getSneakyNumbers(nums)

assert getSneakyNumbers(nums=[0, 1, 1, 0]) == [0, 1]
assert getSneakyNumbers(nums=[0, 3, 2, 1, 3, 2]) == [2, 3] # sorted(result)
assert getSneakyNumbers(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]) == [4, 5]
