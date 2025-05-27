### Условие задачи:
# Вам дана 2D целочисленная матрица с индексом 0 grid и размером n * n со значениями в диапазоне.
# Каждое целое число появляется ровно один раз, за ​​ исключением того, которое появляется дважды , а которое отсутствует.
# Задача — найти повторяющиеся и пропущенные числа и.[1, n2] a b a b
# Возвращает целочисленный массив с индексом 0ans и размером 2где ans[0]равно a и ans[1]равно b.

# Example 1:
# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

# Example 2:
# Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].

### Краткое условие:
# Надо вернуть массив состоящий из двух чисел [число которое больше всего повторяеться в матрице , ]

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную left.
# 0.1) Создаем переменную lenGridTwo в которой будет храниться величина мастрицы grid умноженая на 2,
# и переменную right в которой будет храниться (1+lenGridTwo)* lenGridTwo//2.
# 1) Проходимся циклом по матрице grid (берем массив из матрицы grid),
# 1.1) Проходимся циклом по массиву из матрицы grid,
# 1.1.1) Если j есть в словаре setDict, то записываем j в переменную left.
# 1.1.2) Если j НЕТу в словаре setDict, то добавляем ключ j в словарь и вычитаем j из переменной right.
# 2) Вернуть массив состоящий из переменных left и right.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

grid = [[1, 3], [2, 2]]

def findMissingAndRepeatedValues(grid):
    setDict = set()
    left = None

    lenGridTwo = len(grid) ** 2
    right = (1 + lenGridTwo) * lenGridTwo // 2

    for i in grid:
        for j in i:
            if j in setDict:
                left = j
            else:
                setDict.add(j)
                right -= j

    return [left, right]

findMissingAndRepeatedValues(grid)