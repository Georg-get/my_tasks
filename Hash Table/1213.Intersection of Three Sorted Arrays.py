### Условие задачи:
# Даны три целочисленных массива arr1, arr2 и arr3, отсортированные в строго возрастающем порядке.
# Верните отсортированный массив, состоящий только из тех целых чисел, которые встречаются во всех трех массивах.

# Example 1:
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.

### Краткое условие:
# Вернуть массив двух числиел, которые больше всего повторяются во всех трех массивах.

# Алгоритм решение задачи:
# 0) Создаем множество из массива чисел arr1.
# 1) Создаем множество из массива чисел arr2.
# 2) Создаем множество из массива чисел arr3.
# 3) Создаем множество result с пересечениями из множеств: set1, set2, set3.
# 4) Вернуть массив из множество числе result.

                            ### Не проходят все юнитесты !!!

# Сложность:
# 1) Время O(m)
# 2) Память O(n)

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

def arraysIntersection(arr1, arr2, arr3):
    set1 = set(arr1)  # {1, 2, 3, 4, 5}
    set2 = set(arr2)  # {1, 2, 5, 7, 9}
    set3 = set(arr3)  # {1, 3, 4, 5, 8}

    result = set1.intersection(set2).intersection(set3)
    # {1, 5}
    return sorted(list(result)) # [1, 5]

arraysIntersection(arr1, arr2, arr3)

assert arraysIntersection(arr1=[1, 2, 3, 4, 5], arr2=[1, 2, 5, 7, 9], arr3=[1, 3, 4, 5, 8]) == [1, 5]
# Доп юнитесты для проверки некоторых условий:
assert arraysIntersection(arr1=[1, 2, 3, 4, 5], arr2=[2, 3, 4], arr3=[3, 4]) == [3]
assert arraysIntersection(arr1=[1, 2, 3], arr2=[4, 5, 6], arr3=[7, 8, 9]) == []
assert arraysIntersection(arr1=[], arr2=[1, 2, 3], arr3=[4, 5, 6]) == []
assert arraysIntersection(arr1=[1, 2, 2, 3], arr2=[2, 2, 3], arr3=[2, 3, 3]) == [2]
assert arraysIntersection(arr1=[1, 2, 3], arr2=[1, 2, 3], arr3=[1, 2, 3]) == [1, 2, 3]
assert arraysIntersection(arr1=[1], arr2=[1], arr3=[1]) == [1]
assert arraysIntersection(arr1=[1, 2, 3], arr2=[2], arr3=[2, 3, 4]) == [2]

### Хэш таблицы !!!
# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n)
# 2) Память O(n)
#
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [1, 2, 5, 7, 9]
# arr3 = [1, 3, 4, 5, 8]
#
# def arraysIntersection(arr1, arr2, arr3):
#     dict = {}
#     result = []
#
#     for i in arr1:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#
#     for j in arr2:
#         if j in dict:
#             dict[j] += 1
#         else:
#             dict[j] = 1
#
#     for k in arr3:
#         if k in dict:
#             dict[k] += 1
#         else:
#             dict[k] = 1
#     # {1: 3, 2: 2, 3: 2, 4: 2, 5: 3, 7: 1, 9: 1, 8: 1}
#     for key, vales in dict.items():
#         if vales == max(dict.values()):
#             result.append(key)
#     # [1, 5]
#     return result
#
# arraysIntersection(arr1, arr2, arr3)
