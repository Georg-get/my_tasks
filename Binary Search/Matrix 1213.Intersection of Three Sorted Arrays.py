### Условие задачи:
# Даны три неубывающих массива чисел. Найти число, которое присутствует во всех трех массивах.

# Example 1:
# Input: [1,2,4,5], [3,3,4], [2,3,4,5,6]
# Output: 4

### Краткое условие:
# Найти число которое посвотряеться во всех трех массивах.

#               Без бинарного поиска (в лоб) 1
# Алгоритм решение задачи:
# 0) Обьединить массивы: arr1, arr2, arr3 в массив list
# 0.1) Создать переменную result.
# 1) Пройтись циклом по массиву list и найти тот элелемент который чаще всего повторяется в массиве list
# и запесать результат в переменную result.
# 2) Вернуть return result.

# Сложность:
# 1) памяти O(n)
# 2) времени O(n^2)

# arr1 = [1, 2, 4, 5]
# arr2 = [3, 3, 4]
# arr3 = [2, 3, 4, 5, 6]


# def arraysIntersection(arr1, arr2, arr3):
#     list = arr1 + arr2 + arr3
#     result = []
#     max_count = 0
#     for i in list:
#         count = list.count(i)
#         if count > max_count:
#             max_count = count
#             result = i
#     return result
#
#
# arraysIntersection(arr1, arr2, arr3)


#               Без бинарным поиском (в лоб) 2
# Алгоритм решение задачи:
# 0) Создать пустой массив result
# 1) Пройтись циклом по массиву arr1,
# 1.1) Если элемент из массива arr1 есть в массиве arr2 и есть массиве arr3, то добавь это число в массив result.
# 2) Вернуть return result.

# Сложность:
# 1) памяти O(k)
# 2) времени O(n^2)

# arr1 = [1, 2, 4, 5]
# arr2 = [3, 3, 4]
# arr3 = [2, 3, 4, 5, 6]
#
# def arraysIntersection(arr1, arr2, arr3):
#     result = []
#     for num in arr1:
#         if num in arr2 and num in arr3:
#             result.append(num)
#     return result
#
# arraysIntersection(arr1, arr2, arr3)


#               C бинарным поиском
# Алгоритм решение задачи:
# 0) Отсортировать массивы: arr1, arr2, arr3 по возврастанию.
# 0.1) Создать пустой массив result.
# 0.2) Пишем функцию бинарного поска, которая ищет в массие число которое = target.
# 1) Проходимся циклом по массиву arr3,
# 1.1) Если функция бинарного поиска нашла элемент из массива arr3 в массие arr1,
# 1.1.1) то проверяем функцией бинарнорго поиска есть ли это число в массие arr2,
# 1.1.2) если оно там есть то добавляем это число в массив result.
# 1.1.3) Если НЕТ то pass.
# 1.2) Если НЕТ то pass.
# 2) Вернуть return result.

# Сложность:
# 1) памяти O(n log n)
# 2) времени O(1)

arr1 = [1, 2, 4, 5]
arr2 = [3, 3, 4]
arr3 = [2, 3, 4, 5, 6]


def arraysIntersection(arr1, arr2, arr3):
    arr1.sort()
    arr2.sort()
    arr3.sort()
    result = []

    for i in arr3:
        if binarySearch(arr1, i):
            if binarySearch(arr2, i):
                result.append(i)
            else:
                pass
        else:
            pass
    return result


def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


arraysIntersection(arr1, arr2, arr3)
