### Условие задачи:
# Вам даны два двумерных целочисленных массива items1и items2, представляющие два набора элементов.
# Каждый массив items имеет следующие свойства:
# items[i] = [ value i, weight i] где представляет стоимость и представляет вес предмета. value i weight i ith
# Ценность каждого предмета items уникальна.
# Возвращает двумерный целочисленный массив, ret где, где является суммой весов всех элементов со значением .
# ret[i] = [value i, weight i] weight i value i
# Примечание: ret следует возвращать в порядке возрастания значения.

# Example 1:
# Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# Output: [[1,6],[3,9],[4,5]]
# Explanation:
# The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
# The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
# The item with value = 4 occurs in items1 with weight = 5, total weight = 5.
# Therefore, we return [[1,6],[3,9],[4,5]].

# Example 2:
# Input: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
# Output: [[1,4],[2,4],[3,4]]
# Explanation:
# The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 3, total weight = 1 + 3 = 4.
# The item with value = 2 occurs in items1 with weight = 3 and in items2 with weight = 1, total weight = 3 + 1 = 4.
# The item with value = 3 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
# Therefore, we return [[1,4],[2,4],[3,4]].

# Example 3:
# Input: items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
# Output: [[1,7],[2,4],[7,1]]
# Explanation:
# The item with value = 1 occurs in items1 with weight = 3 and in items2 with weight = 4, total weight = 3 + 4 = 7.
# The item with value = 2 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
# The item with value = 7 occurs in items2 with weight = 1, total weight = 1.
# Therefore, we return [[1,7],[2,4],[7,1]].

### Краткое условие:
# Вернуть матрицу, в которой будет сумма двух матриц items1 и items2.

# Алгоритм решение задачи:
# 0) Создаем два пустых словаря dict1 и dict2, и пустой массив result.
# 1) Проходимся по матрице items1 и перезаписываем матрицу в словарь dict1,
# где первый элемент массива это ключ со значением второго элемента.
# 2) Проходимся по матрице items2 и перезаписываем матрицу в словарь dict2,
# где первый элемент массива это ключ со значением второго элемента.
# 3) Проходимся циклом по словарю dict1, увеличиваем значение каждого ключа на свое значение.
# 4) Проходимся циклом по словарю dict2,
# 4.1) Если k нету в словаре dict1, то добавь ключ k в словарь dict1 со значением dict1[k] + dict1[k].
# 5) Проходимся циклом по словарю dict1, добавляем ключ и значение в массив result.
# 6) Вернуть отсортировые массивы по возврастанию внутри массива result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]

def mergeSimilarItems(items1, items2):
    dict1 = {}
    dict2 = {}
    result = []

    for i in items1:
        dict1[i[0]] = i[1]
    # print(dict1) {1: 1, 4: 5, 3: 8}

    for j in items2:
        dict2[j[0]] = j[1]
    # print(dict2) {3: 1, 1: 5}

    for k in dict1:
        if k in dict1:
            dict1[k] = dict1[k] + dict1[k]
    # print(dict1) {1: 2, 4: 10, 3: 16}

    for j in dict2:
        if j not in dict1:
            dict1[j] = dict2[j]
    # print(dict2) {3: 1, 1: 5}

    for i in dict1:
        result.append([i, dict1[i]])
    # [[1, 2], [4, 10], [3, 16]]
    return (sorted(result))  # [[1, 2], [3, 16], [4, 10]]

mergeSimilarItems(items1, items2)