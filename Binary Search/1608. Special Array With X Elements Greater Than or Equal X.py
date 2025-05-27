### Условие задачи:
# Вам дан массив nums неотрицательных целых чисел. nums считается особенным, если существует такое число,
# в котором x есть ровно x числа, большие или равные .nums x
# Обратите внимание, что это x необязательно должен быть элемент в nums.
# Возврат, x если массив особенный, в противном случае возврат-1. Можно доказать, что если является особенным,
# то nums значение for x уникально.

# Example 1:
# Input: nums = [3,5]
# Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

# Example 2:
# Input: nums = [0,0]
# Output: -1
# Explanation: No numbers fit the criteria for x.
# If x = 0, there should be 0 numbers >= x, but there are 2.
# If x = 1, there should be 1 number >= x, but there are 0.
# If x = 2, there should be 2 numbers >= x, but there are 0.
# x cannot be greater since there are only 2 numbers in nums.

# Example 3:
# Input: nums = [0,4,3,0,4]
# Output: 3
# Explanation: There are 3 values that are greater than or equal to 3.

### Краткое условие:
# вернуть колличество положительных числе в массие nums.

# Алгоритм решение задачи:
# 0) Определить границы поиска.(left и right) и пройтись циклом.
# 1) Проходимся циклом ваилд пока left не станет меньше или равно right,
# 1.1) Создаем переменную mid в которой будет храниться середина массива nums и переменную count со значением 0.
# 1.2) Проходимся циклом по массиву nums, если i больше или равно mid, то увеличь значение count на 1.
# 1.3) Если count равно mid то верни mid.
# 1.4) Если count больше mid, то увеличь left на mid + 1.
# 1.5) Иначе, уменьши right на mid - 1.
# 2) Верни -1

# Сложность:
# 1) памяти O(1)
# 2) времени O(n log n)

nums = [0, 4, 3, 0, 4]

def specialArray(nums):
    left = 0
    right = len(nums) # 5

    while left <= right:

        mid = (left + right) // 2
        count = 0

        for i in nums:
            if i >= mid:
                count += 1

        if count == mid:
            return mid # тут заканчивается первый и третий юнитест
        elif count > mid:
            left = mid + 1
        else:
            right = mid - 1

    return -1 # тут заканчивается второй юнитест

specialArray(nums)

assert specialArray(nums=[3, 5]) == 2
assert specialArray(nums=[0, 0]) == -1
assert specialArray(nums=[0, 4, 3, 0, 4]) == 3