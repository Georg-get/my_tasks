### Условие задачи:
# Вам дан двумерный целочисленный массив с индексом 0 nums, представляющий координаты паркующихся автомобилей на числовой прямой.
# Для любого индекса i где — начальная точка автомобиля и — конечная точка автомобиля. nums[i] = [starti, endi] start i ith end i i th
# Возвращает количество целочисленных точек на линии, покрытых любой частью автомобиля.

# Example 1:
# Input: nums = [[3,6],[1,5],[4,7]]
# Output: 7
# Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.

# Example 2:
# Input: nums = [[1,3],[5,8]]
# Output: 7
# Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

### Краткое условие:
# Вернуть количество из матрицы.

# Алгоритм решение задачи:
# 0) Создаем переменную setDict в которой будет храниться set.
# 1) Пройтись циклом по матрице nums,
# 1.1) Проходимся циклом по массиву внутри матрицы nums с диапазоном (от первого элемента до второго элемента+1 массива внутри матрицы).
# 1.1.1) Если j НЕТу в словаре setDict, то добавить j словарь setDict.
# 2) Вернуть размер словаря setDict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [[3, 6], [1, 5], [4, 7]]

def numberOfPoints(nums):
    setDict = set()

    for i in nums:
        print(range(i[0], i[1] + 1))
        for j in range(i[0], i[1] + 1):
            if j not in setDict:
                setDict.add(j)

    return len(setDict)

numberOfPoints(nums)