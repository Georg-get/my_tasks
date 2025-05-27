### Условие задачи:
# Учитывая массив nums целых n чисел где nums[i] находится в диапазоне [1, n],
# верните массив всех целых чисел в диапазоне [1, n], которые не входят в nums диапазон.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

### Краткое условие:
# Вернуть массив с пропущеными числами. Одним числам в массиве !!!

# Алгоритм решение задачи:
# 0) Создаем пустой массив result и словарь с set(массив nums).
# 1) Проходимся циклом по диапазону (от 1 до длины массива nums+1),
# 1.1) Если ключа i НЕТу в словаре numsSet, то добавь i в массив result.
# 2) Верни массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [4, 3, 2, 7, 8, 2, 3, 1]

def findDisappearedNumbers(nums):
    result = []
    numsSet = set(nums)  # {1, 2, 3, 4, 7, 8}

    for i in range(1, len(nums) + 1):  # (1,9)
        if i not in numsSet:
            result.append(i)
    # [5,6]
    return result

findDisappearedNumbers(nums)

assert findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
assert findDisappearedNumbers(nums=[1, 1]) == [2]