### Условие задачи:
# Вам дан массив nums, где каждое число в массиве встречается либо один, либо два раза.
# Возвращает побитовое значение всех чисел, которые встречаются в массиве дважды, или 0,
# если ни одно число не встречается дважды. XOR

# Example 1:
# Input: nums = [1,2,1,3]
# Output: 1
# Explanation:
# The only number that appears twice in nums is 1.

# Example 2:
# Input: nums = [1,2,3]
# Output: 0
# Explanation:
# No number appears twice in nums.

# Example 3:
# Input: nums = [1,2,2,1]
# Output: 3
# Explanation:
# Numbers 1 and 2 appeared twice. 1 XOR 2 == 3.


### Краткое условие:
# Надо найти дубликаты чисел в массиве nums и если они есть сложить их побитова, если дублей нету то вернуть 0.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result со значением 0.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Иначе, добавь ключ i со значением 1 в словарь dict.
# 2) Проходимся циклом по словарю dict,
# 2.1) Если value больше или равно 2, то увеличь переменную result на по битова на key (ключ из словаря dict).
# 3) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 2, 1, 3]

def duplicateNumbersXOR(nums):
    dict = {}
    result = 0

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {1: 2, 2: 1, 3: 1}
    for key, value in dict.items():
        if value >= 2:
            result ^= key  # это от 4 юнитеста !

    return result

duplicateNumbersXOR(nums)

assert duplicateNumbersXOR(nums=[1, 2, 1, 3]) == 1
assert duplicateNumbersXOR(nums=[1, 2, 3]) == 0
assert duplicateNumbersXOR(nums=[1, 2, 2, 1]) == 3
assert duplicateNumbersXOR(
    nums=[10, 18, 7, 10, 18]) == 24  # этот юнитест валит код (из-за него надо побитова увеличивать result) !!!