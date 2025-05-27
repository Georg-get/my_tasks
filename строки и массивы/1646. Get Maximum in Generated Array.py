### Условие задачи:
# Вам дано целое число n. Целочисленный массив с индексом 0 nums длины n + 1 генерируется следующим образом:
# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] когда 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] когда 2 <= 2 * i + 1 <= n
# Вернуть максимальное целое число в массиве nums .


# Example 1:
# Input: n = 7
# Output: 3
# Explanation: According to the given rules:
#   nums[0] = 0
#   nums[1] = 1
#   nums[(1 * 2) = 2] = nums[1] = 1
#   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
#   nums[(2 * 2) = 4] = nums[2] = 1
#   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
#   nums[(3 * 2) = 6] = nums[3] = 2
#   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
# Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.

# Example 2:
# Input: n = 2
# Output: 1
# Explanation: According to the given rules, nums = [0,1,1]. The maximum is max(0,1,1) = 1.

# Example 3:
# Input: n = 3
# Output: 2
# Explanation: According to the given rules, nums = [0,1,1,2]. The maximum is max(0,1,1,2) = 2.

### Краткое условие:
# Вернуть максимальное целое число в массиве nums.


# Полное объяснение решение задачи:
# 0) Если n равно 0, то верни 0.
# 1) Создаем массив c значениеми 0 и 1.
# 1.1) Проходимся циклом по диапазону от 2 до n+1,
# 1.1.1) Если i четное число, то в массив nums добавляем i деленное на 2.
# 1.1.2) Иначе, в массив nums добавляем i деленное на 2 + i деленное на 2+1.
# 1.1.3) Вернуть максимальное число из массива nums.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

n = 7

def getMaximumGenerated(n):

    if n == 0:  # четвертый юни-тест !
        return 0

    else:

        nums = [0, 1]

        for i in range(2, n + 1):  # range(2, 8)
            if i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[i // 2] + nums[(i // 2) + 1])
        # [0, 1, 1, 2, 1, 3, 2, 3]

        return max(nums)

getMaximumGenerated(n)

assert getMaximumGenerated(n=7) == 3
assert getMaximumGenerated(n=2) == 1
assert getMaximumGenerated(n=3) == 2
assert getMaximumGenerated(n=0) == 0  # if n == 0: