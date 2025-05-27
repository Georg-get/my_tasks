### Условие задачи:
# Учитывая массив arr целых чисел, проверьте, существуют ли два индекса i и j такие, что:
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Example 2:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

### Краткое условие:
# Если i равена индуксу j умноженаму на 2 то вернуть True, если нету то вернуть False.


                    ### Хэш таблицы !!! ###
# Алгоритм решение задачи:
# 0) Создаем пустое множество dictSet.
# 1) Проходимся циклом по массиву arr,
# 1.1) Если ключ i*2 есть в словаре dictSet или ключ i / 2 есть в словаре dictSet, то верни True.
# 1.2) Добавь i в словарь dictSet.
# 2) Верни False.

# Сложность:
# 1) памяти O(n)
# 2) времени O(n)

arr = [10, 2, 5, 3]

def checkIfExist(arr):
    dictSet = set()

    for i in arr:
        if i * 2 in dictSet or i / 2 in dictSet:
            # {10, 2} - это первый юнитест !!!
            return True

        dictSet.add(i)

    return False

checkIfExist(arr)

assert checkIfExist(arr=[10, 2, 5, 3]) == True
assert checkIfExist(arr=[3, 1, 7, 11]) == False

### Бинарный поиск !!! ###
# Алгоритм решение задачи:
# 0) Сортируем массив arr по возрастанию.
# 1) Проходимся бинарным поиском по массиву arr, если таргет совпадает с условием то вернуть True иначе False.

# Сложность:
# 1) памяти O(n log n)
# 2) времени O(1)
#
# arr = [10, 2, 5, 3]
#
# def checkIfExist(arr):
#     arr = sorted(arr)  # [2, 3, 5, 10]
#
#     for i in range(len(arr)): # range(0, 4)
#
#         left = 0
#         right = len(arr) - 1 # 3
#
#         while left <= right:
#             mid = (left + right) // 2
#
#             if arr[mid] * 2 == arr[i] and mid != i:
#                 return True
#             elif arr[mid] * 2 > arr[i]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#
#     return False
#
# checkIfExist(arr)