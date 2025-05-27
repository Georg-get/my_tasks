### Условие задачи:
# Учитывая m x n матрицу grid, которая отсортирована в невозрастающем порядке как по строкам,
# так и по столбцам, верните количество отрицательных чисел в grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0

### Краткое условие:
# Вывести число положительных элементов в матрице.

#                                                   А) Без бинарного поиска
# Алгоритм решение задачи:
# 0) Создать пустой массив list.
# 1) Пройтись циклом по всем элементам матрецы grid
# 1.1) Если элемент матрецы grid совпадает с меньше 0, то добавь в этот элемент в массив list.
# 1.2) Если НЕТ то, pass
# 2) Вернуть число колличество элементов в массив list.

# # Сложность:
# # 1) памяти O(n*m)
# # 2) времени O(k)

# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#
# def countNegatives(grid):
#     result = []
#     for row in grid:
#         for element in row:
#             if element < 0:
#                 result.append(element)
#             else:
#                 pass
#     return len(result)
#
# countNegatives(grid)

#                                           Б) С бинарным поиском
# Алгоритм решение задачи:
# 0) создать переменную result = 0
# 1) Написать функцию бинарного поиска (binarySearch),
# которая на вход принимает массив и ишет в нем первый отрицательный элемент.
# 2) Пройтись циклом по элементам матрицы grid.
# 2.1) result = result + размер массива из матрицы grid - результат фукции binarySearch с параметром массива из матрицы grid
# 3) Вернуть число колличество элементов в массив result.

# # Сложность:
# # 1) памяти O(n*log(m))
# # 2) времени O(1)

grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

def countNegatives(grid):

    def binarySearch(array):
        left = 0
        right = len(array) - 1

        while left <= right:

            mid = (left + right) // 2

            if array[mid] < 0:
                right = mid - 1

            elif array[mid] >= 0:
                left = mid + 1

        return left

    result = 0

    for i in grid:
        result = result + len(i) - binarySearch(i)

    return result

countNegatives(grid)