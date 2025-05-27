### Условие задачи:
# Нам дан список nums целых чисел, представляющий собой список, сжатый с помощью кодирования длин серий.
# Рассмотрим каждую смежную пару элементов [freq, val] = [nums[2*i], nums[2*i+1]] (с i >= 0).
# Для каждой такой пары есть freq элементы со значением, val объединенные в подсписок.
# Объедините все подсписки слева направо, чтобы создать распакованный список.
# Верните распакованный список.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

# Example 2:
# Input: nums = [1,1,2,3]
# Output: [1,3,3]

### Краткое условие:
# Верните распакованный список.

# Алгоритм решение задачи:
# 0) Создаем пустой массив result, и левый и правый указатель.
# 1) Проходимся циклом ваилд пока left не дойдет до предпоследнего элемента массив nums или right не дойдет до конца массива nums.
# 1.1) Проходимся циклом ваилд пока элемент где стаит левый указатель не станет больше 0,
# 1.1.1) в массив result добавляем элемент массива nums где стаит правый указатель, уменьшаем левый указатель на 1.
# 1.2) Увеличиваем left на 2 и right на 2.
# 2) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 2, 3, 4]

def decompressRLElist(nums):
    result = []
    left = 0
    right = 1

    while left < len(nums) - 1 or right < len(nums):

        while nums[left] > 0:
            result.append(nums[right])
            nums[left] -= 1

        left += 2
        right += 2

    return result

decompressRLElist(nums)

assert decompressRLElist(nums=[1, 2, 3, 4]) == [2, 4, 4, 4]
assert decompressRLElist(nums=[1, 1, 2, 3]) == [1, 3, 3]