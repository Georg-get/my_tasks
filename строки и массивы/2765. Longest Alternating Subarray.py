### Условие задачи:
# Вам дан целочисленный массив с индексом 0.nums Подмассив s длины m называется чередующимся, если: m больше, чем 1.
# s1 = s0 + 1. Подмассив с индексом 0 выглядит s как.
# Другими словами, , , , , и так далее до .[s0, s1, s0, s1,...,s(m-1) % 2]s1 - s0 = 1s2 - s1 = -1s3 - s2 = 1s4 - s3 = -1s[m - 1] - s[m - 2] = (-1)m
# Возвращает максимальную длину всех чередующихся подмассивов, присутствующих в массиве, nums или -1если такой подмассив не существует .
# Подмассив — это непрерывная непустая последовательность элементов внутри массива.

# Example 1:
# Input: nums = [2,3,4,3,4]
# Output: 4
# Explanation:
# The alternating sub arrays are [2, 3], [3,4], [3,4,3], and [3,4,3,4]. The longest of these is [3,4,3,4], which is of length 4.

# Example 2:
# Input: nums = [4,5,6]
# Output: 2
# Explanation:
# [4,5] and [5,6] are the only two alternating sub arrays. They are both of length 2.

### Краткое условие:
# Возвращает максимальную длину всех чередующихся подмассивов,
# присутствующих в массиве nums или -1если такой подмассив не существует.

# Полное объяснение решение задачи:
# 0) Создаем переменную result со значением -1.
# 1) Проходимся циклом по индексам массвива nums от 0 до длины массвива,
# 1.1) Проходимся циклом по индексам массвива nums от i+1 до длины массвива,
# 1.1.1) Если преведуший элемент массива nums равен нынешнему элементу массива + (-1) ** (j - i),
# 1.1.1.1) Увеличиваем result на максимум из result или j - i + 1.
# 1.1.1.2) Иначе, выйди из цикла.
# 2) Верни result.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

nums = [2, 3, 4, 3, 4]

def alternatingSubarray(nums):
    result = -1

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[j - 1] == nums[j] + (-1) ** (j - i):
                result = max(result, j - i + 1)

            else:
                break  # от третьего юнитеста

    return result

alternatingSubarray(nums)

assert alternatingSubarray(nums=[2, 3, 4, 3, 4]) == 4
assert alternatingSubarray(nums=[4, 5, 6]) == 2
assert alternatingSubarray(nums=[42, 43, 44, 43, 44, 43, 44, 45, 46]) == 6 # этот кейс валит код