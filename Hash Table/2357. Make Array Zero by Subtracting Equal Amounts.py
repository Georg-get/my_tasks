### Условие задачи:
# Вам дан массив неотрицательных целых чисел nums. За одну операцию необходимо:
# Выберите целое положительное число x, которое x меньше или равно наименьшему ненулевому элементу в nums.
# Вычтите x из каждого положительного элемента в nums.
# Возвращает минимальное количество операций, чтобы сделать каждый элемент nums равным 0.

# Example 1:
# Input: nums = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

# Example 2:
# Input: nums = [0]
# Output: 0
# Explanation: Each element in nums is already 0 so no operations are needed.

### Краткое условие:
# Надо найти сколько раз можно уменьшить массив nums на минимальнуе значение массива nums.

# Алгоритм решение задачи:
# 0) Преобразуем массив nums в словарь с set и убираем дубли элементов.
# 1) Удаляем ключ 0 из словаря nums.
# 2) Вернуть длину словаря nums.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 5, 0, 3, 5]

def minimumOperations(nums):
    nums = set(nums)  # {0, 1, 3, 5}
    nums.discard(0)  # {1, 3, 5}
    return len(nums)  # 3

minimumOperations(nums)

assert minimumOperations(nums=[1, 5, 0, 3, 5]) == 3
assert minimumOperations(nums=[0]) == 0