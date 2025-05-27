### Условие задачи:
# Дано целочисленное числовое множество с индексом 0 nums, вернуть true,
# если его можно сделать строго возрастающим после удаления ровно одного элемента, или false в противном случае.
# Если массив уже строго возрастающий, вернуть true.
# Массив строго возрастает nums, если для каждого индекса nums[i - 1] < nums[i](1 <= i < nums.length).

# Example 1:
# Input: nums = [1,2,10,5,7]
# Output: true
# Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
# [1,2,5,7] is strictly increasing, so return true.

# Example 2:
# Input: nums = [2,3,1,2]
# Output: false
# Explanation:
# [3,1,2] is the result of removing the element at index 0.
# [2,1,2] is the result of removing the element at index 1.
# [2,3,2] is the result of removing the element at index 2.
# [2,3,1] is the result of removing the element at index 3.
# No resulting array is strictly increasing, so return false.

# Example 3:
# Input: nums = [1,1,1]
# Output: false
# Explanation: The result of removing any element is [1,1].
# [1,1] is not strictly increasing, so return false.

### Краткое условие:
# Надо вернуть true если из массива nums можно удалить один элемент и все элементы будут по возрастанию отсортированы.

# Алгоритм решение задачи:
# 0) Создаем пустой массив stack.
# 1) Проходимся циклом по диапазону от 1 до длины массива nums,
# 1.1) Если nums[i - 1] >= nums[i], то в массив stack добавь i.
# 2) Если массив stack равен 0, то верни True.
# 3) Если массив stack больше 1, то верни False.
# 4) Если (превый элемент массива stack равен 0 или из первого элемента вычесть 2 он будет меньше первого элемента) или
# (второй элемент стека равен длине массива или из первого элемента вычесть 2 он будет меньше из первого элемента прибавить 1 он),
# 4.1) Верни True.
# 5) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 2, 10, 5, 7]

def canBeIncreasing(nums):
    stack = []

    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            stack.append(i)

    if len(stack) == 0:
        return True

    elif len(stack) > 1:
        return False

    if (stack[0] == 1 or nums[stack[0] - 2] < nums[stack[0]]) or (
            stack[0] + 1 == len(nums) or nums[stack[0] - 1] < nums[stack[0] + 1]):
        return True
    else:
        return False

canBeIncreasing(nums)

assert canBeIncreasing(nums=[1, 2, 10, 5, 7]) == True
assert canBeIncreasing(nums=[2, 3, 1, 2]) == False
assert canBeIncreasing(nums=[1, 1, 1]) == False