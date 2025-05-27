### Условие задачи:
# Вам дан целочисленный массив с нулевым индексом nums.
# Конкатенация двух чисел — это число, образованное соединением их цифр.
# Например, объединение 15, 49 есть 1549.
# Значение конкатенации изначально nums равно 0. Выполняйте эту операцию, пока nums не станет пустым:
# Если существует более одного числа в nums, выберите первый элемент и последний элемент соответственно nums
# и добавьте значение их конкатенации к значению конкатенации nums, затем удалите первый и последний элемент из nums.
# Если один элемент существует, добавьте его значение к значению конкатенации nums, а затем удалите его.
# Верните значение конкатенации nums.

# Example 1:
# Input: nums = [7,52,2,4]
# Output: 596
# Explanation: Before performing any operation, nums is [7,52,2,4] and concatenation value is 0.
#  - In the first operation:
# We pick the first element, 7, and the last element, 4.
# Their concatenation is 74, and we add it to the concatenation value, so it becomes equal to 74.
# Then we delete them from nums, so nums becomes equal to [52,2].
#  - In the second operation:
# We pick the first element, 52, and the last element, 2.
# Their concatenation is 522, and we add it to the concatenation value, so it becomes equal to 596.
# Then we delete them from the nums, so nums becomes empty.
# Since the concatenation value is 596 so the answer is 596.

# Example 2:
# Input: nums = [5,14,13,8,12]
# Output: 673
# Explanation: Before performing any operation, nums is [5,14,13,8,12] and concatenation value is 0.
#  - In the first operation:
# We pick the first element, 5, and the last element, 12.
# Their concatenation is 512, and we add it to the concatenation value, so it becomes equal to 512.
# Then we delete them from the nums, so nums becomes equal to [14,13,8].
#  - In the second operation:
# We pick the first element, 14, and the last element, 8.
# Their concatenation is 148, and we add it to the concatenation value, so it becomes equal to 660.
# Then we delete them from the nums, so nums becomes equal to [13].
#  - In the third operation:
# nums has only one element, so we pick 13 and add it to the concatenation value, so it becomes equal to 673.
# Then we delete it from nums, so nums become empty.
# Since the concatenation value is 673 so the answer is 673.

### Краткое условие:
# Верните значение конкатенации массива nums.

# Алгоритм решение задачи:
# 0) Создаем переменные left со значением 0 и right со значением длины массива nums-1, и переменную result со значением 0.
# 1) Проходимся циклом ваилд пока left не станет меньше или ранва right,
# 1.1) Если left равно right, то увеличь переменную result на число где стаит левый указатель из массива nums.
# 1.2) Если left НЕ равно right, то увеличь переменную result на число где стаит левый и правый указатель из массива nums.
# 1.3) Увеличь значение переменной left на 1 и уменьши значение переменной right на 1.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [7, 52, 2, 4]

def findTheArrayConcVal(nums):
    left = 0
    right = len(nums) - 1
    result = 0

    while left <= right:
        if left == right:
            result += int(nums[left])

        else:
            result += int(str(nums[left]) + str(nums[right]))

        left += 1
        right -= 1

    return result # 596

findTheArrayConcVal(nums)

assert findTheArrayConcVal(nums=[7, 52, 2, 4]) == 596
assert findTheArrayConcVal(nums=[5, 14, 13, 8, 12]) == 673