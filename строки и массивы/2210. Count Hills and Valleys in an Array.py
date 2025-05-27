### Условие задачи:
# Вам дан целочисленный массив с индексом 0. nums Индекс i является частью холма в , nums если ближайшие неравные соседи i меньше nums[i].
# Аналогично, индекс i является частью долины в, nums если ближайшие неравные соседи i больше nums[i].
# Смежные индексы i и j являются частью одного холма или долины, если nums[i] == nums[j].
# Обратите внимание: для того чтобы индекс был частью холма или долины,
# он должен иметь неравного соседа как слева, так и справа от индекса.
# Верните количество холмов и долин в nums.

# Example 1:
# Input: nums = [2,4,1,1,6,5]
# Output: 3
# Explanation:
# At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
# At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill.
# At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
# At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2.
# At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
# At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley.
# There are 3 hills and valleys so we return 3.

# Example 2:
# Input: nums = [6,6,5,5,4,1]
# Output: 0
# Explanation:
# At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley.
# At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley.
# At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor a valley.
# At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor a valley.
# At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor a valley.
# At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley.
# There are 0 hills and valleys so we return 0.

### Краткое условие:
# Верните количество холмов и долин в nums.

# Алгоритм решение задачи:
# 0) Задаем левый и правый указатель, и переменную result со значением 0.
# 1) Проходимся циклом ваилд пока right не дойдет до конца массива nums,
# 1.1) Если левый и правый указатель не равны,
# 1.1.1) Если (число перед левым указателем меньше числа где установлен левый указател и правый указатель меньше чем левый)
# или (число перед левым указателем меньше числа где установлен левый указател и правый указатель больше чем левый), то увеличь result на 1.
# 1.1.2) Левый указатель равен правому.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [2, 4, 1, 1, 6, 5]

def countHillValley(nums):
    left = 1
    right = 2
    result = 0

    while right < len(nums):

        if nums[left] != nums[right]:
            if (nums[left - 1] < nums[left] and nums[right] < nums[left]) or (nums[left - 1] > nums[left] and nums[right] > nums[left]):
                result += 1

            left = right

        right += 1

    return result

countHillValley(nums)

assert countHillValley(nums=[2, 4, 1, 1, 6, 5]) == 3
assert countHillValley(nums=[6, 6, 5, 5, 4, 1]) == 0