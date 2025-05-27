### Условие задачи:
# Дан массив целых чисел nums (индексированный на 0) и два целых числа target и start,
# найдите индекс i такой, что и минимизируется nums[i] == target . abs(i - start)
# Обратите внимание, что   — это абсолютное значение .abs(x)x
# Возвращаться abs(i - start).
# Гарантируется , что target существует в nums.

# Example 1:
# Input: nums = [1,2,3,4,5], target = 5, start = 3
# Output: 1
# Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

# Example 2:
# Input: nums = [1], target = 1, start = 0
# Output: 0
# Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.

# Example 3:
# Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
# Output: 0
# Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.

### Краткое условие:
# Возвращаться abs(i - start). Гарантируется , что target существует в nums.

# Алгоритм решение задачи:
# 0) Создаем левый и правый указатель.
# 1) Проходимся циклом ваилд пока левый указатель не станет равен или больше 0 или правый указатель не дойдет до конца массива.
# 1.1) Если левый указатель больше или равен 0 и число где установлен левый указатель равно target, то верни abs(left - start).
# 1.2) Если правый указатель дощел до конца массива nums и число где установлен правый указатель равно target, то верни abs(right - start).
# 1.3) Иначе, уменьши left на 1 и увеличь right на 1.
# 2) Верни -1.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [1, 2, 3, 4, 5]
target = 5
start = 3

def getMinDistance(nums, target, start):
    left = start
    right = start

    while left >= 0 or right < len(nums):

        if left >= 0 and nums[left] == target:
            return abs(left - start)

        elif right < len(nums) and nums[right] == target:
            return abs(right - start)

        else:
            left -= 1
            right += 1

    return -1

getMinDistance(nums, target, start)

assert getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3) == 1
assert getMinDistance(nums=[1], target=1, start=0) == 0
assert getMinDistance(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=1, start=0) == 0