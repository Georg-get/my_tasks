### Условие задачи:
# Матрица n x n действительна, если каждая строка и каждый столбец содержат все целые числа от 1до n ( включительно ).
# Дана n x n целочисленная матрица matrix, возврат, true если матрица действительна . В противном случае вернитесь false.

# Example 1:
# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.

# Example 2:
# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.

### Краткое условие:
# Вернуть true если все числа в матрице matrix имеют пару в каждому массиве, если нету пары вернуть false.

# Алгоритм решение задачи:
# 0) Создаем переменную lenMatrix со значением длины матрицы matrix.
# 1) Проходимся циклом по диапазону длины матрицы matrix,
# 1.1) Создаем словарь lineSet со значением set,
# 1.2) Проходимся циклом по диапазону длины матрицы matrix,
# 1.2.1) Если элементы i и j из матрицы matrix есть в lineSet, то верни False.
# 1.2.2) Добавь в словарь lineSet элементы i и j из матрицы matrix.
# 2) Проходимся циклом по диапазону длины матрицы matrix,
# 2.1) Создаем словарь columnSet со значением set,
# 2.2) Проходимся циклом по диапазону длины матрицы matrix,
# 2.2.1) Если элементы i и j из матрицы matrix есть в columnSet, то верни False.
# 2.2.2) Добавь в словарь columnSet элементы i и j из матрицы matrix.
# 3) Верни True.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]

def checkValid(matrix):
    lenMatrix = len(matrix)
    # Проверяем строки на дубликаты элеменотов в массиве.
    for i in range(lenMatrix):
        lineSet = set()
        for j in range(lenMatrix):
            if matrix[i][j] in lineSet:
                return False
            lineSet.add(matrix[i][j])

    # Проверяем столбцов на дубликаты
    for j in range(lenMatrix):
        columnSet = set()
        for i in range(lenMatrix):
            if matrix[i][j] in columnSet:
                return False
            columnSet.add(matrix[i][j])

    return True

checkValid(matrix)