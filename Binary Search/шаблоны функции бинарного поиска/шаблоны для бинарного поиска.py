### Условие задачи:
    .



### Краткое условие:
#

# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n)
# 2) Память O(n log n)

    left = 1
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2