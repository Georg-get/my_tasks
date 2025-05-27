### Условие задачи:
# Массив arr является горой , если выполняются следующие свойства: arr.length >= 3
# Существуют i такие, 0 < i < arr.length - 1что:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Учитывая горный массив arr, верните индекс i такой,
# что arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# Вы должны решить ее по O(log(arr.length))временной сложности.

# Example 1:
# Input: arr = [0,1,0]
# Output: 1

# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1

### Краткое условие:
# Пик годы !
# Надо найти идекс самого большого числа.

# Алгоритм решение задачи:
# 0) Обьявить границы для поиска (left и right), которые будем сужать.
# 1) Бежать циклом пока left < right.
# 1.1) mid = делим попалам.
# 1.2) проверяем где находиться пик.
# 1.2.1) если слева,то двигаем left.
# 1.2.2) если с права, то двигаем high.
# 2) вернуть left.

# Сложность:
# 1) памяти O(log n)
# 2) времени O(1)

arr = [0, 1, 0]

def peakIndexInMountainArray(arr):
    left = 0
    right = len(arr) - 1  # 2

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    #       1
    return left

peakIndexInMountainArray(arr)

assert peakIndexInMountainArray(arr=[0, 1, 0]) == 1
assert peakIndexInMountainArray(arr=[0, 2, 1, 0]) == 1
assert peakIndexInMountainArray(arr=[0, 10, 5, 2]) == 1
