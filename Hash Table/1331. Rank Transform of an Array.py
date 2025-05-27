### Условие задачи:
# Учитывая массив целых чисел  arr, замените каждый элемент его рангом.
# Ранг показывает, насколько велик элемент. Ранг имеет следующие правила:
# Ранг — целое число, начиная с 1.
# Чем больше элемент, тем больше ранг. Если два элемента равны, их ранг должен быть одинаковым.
# Ранг должен быть как можно меньшим.

# Example 1:
# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

# Example 2:
# Input: arr = [100,100,100]
# Output: [1,1,1]
# Explanation: Same elements share the same rank.

# Example 3:
# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]

### Краткое условие:
# Отсортировать массив arr по возрастанию и присвоить каждому числу номер в отсортированом массиве,
# вернуть массив с номерами чисел.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result.
# 1) Создаем переменную sortedArrayArr со значением отсортированого массив arr без дубликатов элементов.
# 2) Проходимся циклом по диапазону длины массив sortedArrayArr,
# 2.1) Добавляем в словарь dict ключ i со значением i +1.
# 3) Проходимся циклом по массиву arr, добавляем в массив result значение ключа i из словаря dict.
# 4) Вернуть result.

# Сложность:
# 1) Время O(n) (n log n)
# 2) Память O(n)

arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]

def arrayRankTransform(arr):
    dict = {}
    result = []
    sortedArrayArr = sorted(list(set(arr)))  # [5, 9, 12, 28, 37, 56, 80, 100]

    for i in range(len(sortedArrayArr)):
        dict[sortedArrayArr[i]] = i + 1
    # {5: 1, 9: 2, 12: 3, 28: 4, 37: 5, 56: 6, 80: 7, 100: 8}
    for i in arr:
        result.append(dict[i])  # {37: 5}-> 5
    return result  # [5,3,4,2,8,6,7,1,3]

arrayRankTransform(arr)

assert arrayRankTransform(arr=[40, 10, 20, 30]) == [4, 1, 2, 3]
assert arrayRankTransform(arr=[100, 100, 100]) == [1, 1, 1]
assert arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]) == [5, 3, 4, 2, 8, 6, 7, 1, 3]