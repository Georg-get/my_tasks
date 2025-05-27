### Условие задачи:
# Вам дан 0-индексированный массив nums длины, n содержащий различные положительные целые числа.
# Верните минимальное количество сдвигов вправо, необходимых для сортировки nums, и -1 если это невозможно.
# Сдвиг вправо определяется как сдвиг элемента с индексом i на индекс (i + 1) % n для всех индексов.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 2
# Explanation:
# After the first right shift, nums = [2,3,4,5,1].
# After the second right shift, nums = [1,2,3,4,5].
# Now nums is sorted; therefore the answer is 2.

# Example 2:
# Input: nums = [1,3,5]
# Output: 0
# Explanation: nums is already sorted therefore, the answer is 0.

# Example 3:
# Input: nums = [2,1,4]
# Output: -1
# Explanation: It's impossible to sort the array using right shifts.

### Краткое условие:
# Верните минимальное количество сдвигов вправо, необходимых для сортировки nums, и -1 если это невозможно.

# Алгоритм решение задачи:
# 0) Создаем переменную sortedNums со значением отслотированого массива nums по возрастанию.
# 1) Проходимся циклом по диапазону от 0 до длины массива nums,
# 1.1) Создаем пустой массив arry.
# 1.2) Если nums равен sortedNums, то верни i.
# 1.3) Добавь в массив arry последний элемент массива nums.
# 1.4) nums равно arry + последний элемент массива nums.
# 2) Верни -1.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

nums = [3, 4, 5, 1, 2]

def minimumRightShifts(nums):
    sortedNums = sorted(nums)

    for i in range(len(nums)):
        arry = []

        if nums == sortedNums:
            return i

        arry.append(nums[-1])
        nums = arry + nums[:-1]

    return -1

minimumRightShifts(nums)

assert minimumRightShifts(nums=[3, 4, 5, 1, 2]) == 2
assert minimumRightShifts(nums=[1, 3, 5]) == 0
assert minimumRightShifts(nums=[2, 1, 4]) == -1