### Условие задачи:
# Вам дан целочисленный массив heightдлины n.
# Есть nвертикальные линии, нарисованные так, что двумя конечными точками линии являются и .ith(i, 0)(i, height[i])
# Найдите две линии, которые вместе с осью X образуют контейнер, в котором содержится больше всего воды.
# Возвращайте максимальное количество воды, которое может храниться в контейнере .
# Обратите внимание , что вы не можете наклонять контейнер.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

### Краткое условие:
# Возвращайте максимальное количество воды, которое может храниться в контейнере.

# Алгоритм решение задачи:
# 0) Создаем переменную left со занчением 0 и переменную right со значнием длины массива-1, и переменную result со значением 0.
# 1) Проходимся циклом воелд пока переменная left не станед меньше right,
# 1.1) Создаем переменную maximum со занченеим (right - left) * минимальное значение (height[left], height[right]).
# 1.2) Увеличиваем переменную result на максивальное значение result либо maximum.
# 1.3) Если элемент left из массива height меньше или равен элементу height из массива height, то увеличь значение left на 1.
# 1.4) Если элемент left из массива height НЕ меньше или НЕ равен элементу height из массива height, то умньши значение right на 1.
# 2) Верни переменную result.


# Сложность:
# 1) Время O(n)
# 2) Память O(n)

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def maxArea(height):
    left = 0
    right = len(height) - 1 # 8
    result = 0

    while left < right:
        maximum = (right - left) * min(height[left], height[right])
        result = max(result, maximum)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    #         49
    return result

maxArea(height)

assert maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert maxArea(height=[1, 1]) == 1