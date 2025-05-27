### Условие задачи:

# Вам дан двоичный массив nums (индексированный с 0).
# Мы определяем как число, двоичное представление которого является подмассивом (от старшего бита до младшего бита).xi nums[0..i]
# Например, если nums = [1,0,1], то , , и .x0 = 1x1 = 2x2 = 5
# Возвращает массив логических значений, answer где answer[i] есть, true если делится на. xi 5

# Example 1:
# Input: nums = [0,1,1]
# Output: [true,false,false]
# Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
# Only the first number is divisible by 5, so answer[0] is true.

# Example 2:
# Input: nums = [1,1,1]
# Output: [false,false,false]

### Краткое условие:
# Возвращает массив логических значений, answer где answer[i] есть, true если делится на. xi 5

# Полное объяснение решение задачи:
# 0) Создаем пустой массив result и num со значение 0.
# 1) Проходимся циклом по массиву nums,
# 1.1) num равно (num * 2 + i) % 5
# 1.2) В массив result добавляем True либо False, зависимо от того равно ли число num нулю.
# 2) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [0, 1, 1]

def prefixesDivBy5(nums):
    result = []
    num = 0

    for i in nums:
        num = (num * 2 + i) % 5
        result.append(num == 0)

    return result

prefixesDivBy5(nums)

assert prefixesDivBy5(nums=[0, 1, 1]) == [True, False, False]
assert prefixesDivBy5(nums=[1, 1, 1]) == [False, False, False]
assert prefixesDivBy5(nums=[0, 1, 1, 1, 1, 1]) == [True, False, False, False, True, False]