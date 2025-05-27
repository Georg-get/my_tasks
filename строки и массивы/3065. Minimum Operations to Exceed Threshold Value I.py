### Условие задачи:
# Вам дан целочисленный массив с индексом 0 nums и целое число k.
# За одну операцию можно удалить одно вхождение наименьшего элемента nums.
# Возвращает минимальное количество операций, необходимое для того, чтобы все элементы массива были больше или равны k.

# Example 1:
# Input: nums = [2,11,10,1,3], k = 10
# Output: 3
# Explanation: After one operation, nums becomes equal to [2, 11, 10, 3].
# After two operations, nums becomes equal to [11, 10, 3].
# After three operations, nums becomes equal to [11, 10].
# At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
# It can be shown that 3 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.

# Example 2:
# Input: nums = [1,1,2,4,9], k = 1
# Output: 0
# Explanation: All elements of the array are greater than or equal to 1 so we do not need to apply any operations on nums.

# Example 3:
# Input: nums = [1,1,2,4,9], k = 9
# Output: 4
# Explanation: only a single element of nums is greater than or equal to 9 so we need to apply the operations 4 times on nums.

### Краткое условие:
# Возвращает минимальное количество операций, необходимое для того, чтобы все элементы массива были больше или равны k.

# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 0.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если i больше или равно k, то не чего не делай.
# 1.2) Если i НЕ больше или НЕ равно k, то увеличь result на 1.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [2, 11, 10, 1, 3]
k = 10

def minOperations(nums, k):
    result = 0

    for i in nums:
        if i >= k:
            pass
        else:
            result += 1

    return result

minOperations(nums, k)

assert minOperations(nums=[2, 11, 10, 1, 3], k=10) == 3
assert minOperations(nums=[1, 1, 2, 4, 9], k=1) == 0
assert minOperations(nums=[1, 1, 2, 4, 9], k=9) == 4
