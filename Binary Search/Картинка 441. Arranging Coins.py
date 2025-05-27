### Условие задачи:
# У вас есть n монеты и вы хотите построить из них лестницу.
# Лестница состоит из k рядов, где в ряду ровно монеты. Последний ряд лестницы может быть неполным.ith i
# Учитывая целое число n, верните количество полных рядов лестницы, которую вы построите.

# Example 1:
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Example 2:
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.

### Краткое условие:
# Учитывая целое число n, верните количество полных рядов лестницы, которую вы построите.

# Алгоритм решение задачи:
# 0) Задаем диапазон для бинарного поиска.
# 1) Проходимся циклом ваилд пока left не станет меньше или равно right,
# 1.2) Создаем переменную mid со значением ((right - left) // 2) + left.
# 1.3) Создаем переменную coins со значением (mid * (mid + 1)) // 2.
# 1.4) Если coins меньше или равно n, то увеличь left на mid + 1,
# 1.5) Иначе, уменьши right на mid - 1.
# 2) Верни right.

# Сложность:
# 1) Время O(n)
# 2) Память O(n log n)

n = 5

def arrangeCoins(n):
    left = 1
    right = n  # 5

    while left <= right:
        mid = ((right - left) // 2) + left
        coins = (mid * (mid + 1)) // 2

        if coins <= n:
            left = mid + 1
        else:
            right = mid - 1

    return right

arrangeCoins(n)

assert arrangeCoins(n=5) == 2
assert arrangeCoins(n=8) == 3