### Условие задачи:
# Дан массив arr целых положительных чисел, отсортированный в строгом порядке возрастания, и целое число k.
# Верните положительное целое число, отсутствующее в этом массиве k

# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

### Краткое условие:
# Надо создать массив числе которых нету в arr и вернуть число которое соответствует k.

# Алгоритм решение задачи:
# 0) Определить границы поиска.(left и right) и пройтись циклом.
# 1) Если разница между arr[mid] и (mid + 1) (текущее значение - порядковый номер) меньше, чем k,
# 1.1) то пропущенное число находится в правой части списка, то двигаемся в лева и там ишем середину
# 1.2) Если нет до двигай в право и ищем там середину
# 2) Верни левый элемент + k

# Сложность:
# 1) памяти O(n log n)
# 2) времени O(1)

arr = [1, 2]
k = 1

def findKthPositive(arr, k):
    left = 0
    right = len(arr) - 1 # 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] - (mid + 1) < k:
            left = mid + 1
        else:
            right = mid - 1
    #       2   + 1
    return left + k  # 3

findKthPositive(arr, k)

assert findKthPositive(arr=[2, 3, 4, 7, 11], k=5) == 9
assert findKthPositive(arr=[1, 2, 3, 4], k=2) == 6
assert findKthPositive(arr=[1, 2], k=1) == 3