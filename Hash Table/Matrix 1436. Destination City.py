### Условие задачи:
# Вам дан массив paths, где означает, что существует прямой путь от. Возвращает город назначения,
# то есть город без какого-либо пути, ведущего в другой город.paths[i] = [cityAi, cityBi]cityAicityBi
# Гарантируется, что граф путей образует прямую без петель, следовательно, город назначения будет ровно один.

# Example 1:
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo"
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

# Example 2:
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are:
# "D" -> "B" -> "C" -> "A".
# "B" -> "C" -> "A".
# "C" -> "A".
# "A".
# Clearly the destination city is "A".

# Example 3:
# Input: paths = [["A","Z"]]
# Output: "Z"

### Краткое условие:
# Вернуть последний элемент матрицы.

# Алгоритм решение задачи:
# 0) Создаем словарь startCities с значением set().
# 1) Проходимся циклом по матрице paths, добавляем каждый нуливой элемент массиа из матрицы paths в словарь startCities.
# И получаем словарь с уникальными городами.
# 2) Проходимся циклом по матрице paths,
# 2.1) Если первого элемента массива из матрицы paths НЕТу в словаре startCities, то верни j[1].
# 3) Верни строку.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

def destCity(paths):
    startCities = set()

    for i in paths:
        startCities.add(i[0])
    # {'London', 'Lima', 'New York'}

    for j in paths:
        print(j)
        if j[1] not in startCities:
            return j[1]

    return ""

destCity(paths)