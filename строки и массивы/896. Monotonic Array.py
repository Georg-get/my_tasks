### Условие задачи:
# Массив называется монотонным, если он монотонно возрастает или монотонно убывает.
# Массив nums является монотонно возрастающим, если для всех i <= j, nums[i] <= nums[j].
# Массив nums является монотонно убывающим, если для всех i <= j, nums[i] >= nums[j].
# Учитывая целочисленный массив nums, возврат true, если данный массив является монотонным, или false в противном случае .

# Example 1:
# Input: nums = [1,2,2,3]
# Output: true

# Example 2:
# Input: nums = [6,5,4,4]
# Output: true

# Example 3:
# Input: nums = [1,3,2]
# Output: false

### Краткое условие:
# Вернуть true если массив nums является монотонным (числа в нем отсортированы), иначе false.

# Алгоритм решение задачи:
# 0) Создаем переменную copyNums со значением массива nums.
# 1) Сортируем массив copyNums по возрастанию.
# 2) Если массив copyNums равен массив nums, то верни True.
# 3) Если массив nums равен массив copyNums на оборот, то верни True.
# 4) Если массив nums НЕ РАВЕН массив copyNums на оборот ИЛИ массив copyNums НЕ РАВЕН массив nums, то верни False.

# Сложность:
# 1) Время O(n log n)
# 2) Память O(1)

nums = [1, 3, 2]

def isMonotonic(nums):
    copyNums = nums.copy()  # [1,3,2]
    copyNums.sort()  # [1,2,3]

    if copyNums == nums:
        return True
    elif nums == copyNums[::-1]:  # copyNums перевернутый
        return True
    else:
        return False

isMonotonic(nums)

assert isMonotonic(nums=[1, 3, 2]) == False
assert isMonotonic(nums=[1, 2, 2, 3]) == True
assert isMonotonic(nums=[6, 5, 4, 4]) == True