### Условие задачи:
# Дан целочисленный массив с индексом 0 nums размера n.
# Найдите максимальную разницу между nums[i] и nums[j] (т.е. nums[j] - nums[i]), такую, что 0 <= i < j < n и nums[i] < nums[j].
# Верните максимальную разницу. Если такой нет i и j существует, верните -1.

# Example 1:
# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

# Example 2:
# Input: nums = [9,4,3,2]
# Output: -1
# Explanation:
# There is no i and j such that i < j and nums[i] < nums[j].

# Example 3:
# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

### Краткое условие:
# Верните максимальную разницу. Если такой нет i и j существует, верните -1.

# Алгоритм решение задачи:
# 0) Создаем левый и правый указатель, и переменную result со значением -1.
# 1) Проходимся циклом ваилд пока левый и правый указатель не встретятся.
# 1.1) Если при вычитание правого и левого указателя больше result и правый указатель больше левлго и число левого указател меньше правого,
# 1.1.1) То result равень nums[right] - nums[left].
# 1.2) Если right == left + 1, то right = len(nums) - 1 и увеличиваем left на 1.
# 1.3) Иначе, уменьшаем right на 1.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [7, 1, 5, 4]

def maximumDifference(nums):
    left = 0
    right = len(nums) - 1
    result = -1

    while left < right:
        if nums[right] - nums[left] > result and right > left and nums[left] < nums[right]:
            result = nums[right] - nums[left]

        if right == left + 1:
            right = len(nums) - 1
            left += 1
        else:
            right -= 1

    return result

maximumDifference(nums)

assert maximumDifference(nums=[7, 1, 5, 4]) == 4
assert maximumDifference(nums=[9, 4, 3, 2]) == -1
assert maximumDifference(nums=[1, 5, 2, 10]) == 9