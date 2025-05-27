### Условие задачи:
# Вам дан двумерный целочисленный массив с индексом 0 dimensions.
# Для всех индексов i, представляет собой длину и 0 <= i < dimensions.length представляет собой ширину прямоугольника .dimensions[i][0] dimensions[i][1] i
# Верните площадь прямоугольника, имеющего самую длинную диагональ.
# Если есть несколько прямоугольников с самой длинной диагональю, верните площадь прямоугольника, имеющего максимальную площадь.

# Example 1:
# Input: dimensions = [[9,3],[8,6]]
# Output: 48
# Explanation:
# For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈ 9.487.
# For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
# So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.

# Example 2:
# Input: dimensions = [[3,4],[4,3]]
# Output: 12
# Explanation: Length of diagonal is the same for both which is 5, so maximum area = 12.

### Краткое условие:
# Если есть несколько прямоугольников с самой длинной диагональю, верните площадь прямоугольника, имеющего максимальную площадь.

# Полное объяснение решение задачи:
# 0) Создаем перемнные maxArea и maxDiag со значением 0.
# 1) Проходимся циклом по индексам масива dimensions,
# 1.1) Записываем в перемнную l число с индексов 0 , а в w число с индексов 1.
# 1.2) Получаем значие currDiag = l ** 2 + w ** 2,
# 1.3) Если currDiag больше maxDiag или (currDiag равно maxDiag и l * w больше чем maxArea),
# 1.3.1) maxDiag равно currDiag.
# 1.3.2) maxArea равно l * w.
# 2) Вернуть maxArea.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

dimensions = [[9, 3], [8, 6]]

def licenseKeyFormatting(dimensions):
    maxArea = 0
    maxDiag = 0

    for i in range(len(dimensions)):
        l, w = dimensions[i] # l = > 9 , 8
                             # w = > 3 , 6
        currDiag = l ** 2 + w ** 2 # 90 # 100

        if currDiag > maxDiag or (currDiag == maxDiag and l * w > maxArea):
            maxDiag = currDiag
            maxArea = l * w

    return maxArea

licenseKeyFormatting(dimensions)

assert licenseKeyFormatting(dimensions=[[9, 3], [8, 6]]) == 48
assert licenseKeyFormatting(dimensions=[[3, 4], [4, 3]]) == 12