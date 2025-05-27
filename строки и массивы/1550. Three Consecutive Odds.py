### Условие задачи:
# Дан массив целых чисел arr, вернуть, true если в массиве есть три последовательных нечетных числа.
# В противном случае вернуть false.

# Example 1:
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.

# Example 2:
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.

### Краткое условие:
# Дан массив целых чисел arr, вернуть, true если в массиве есть три последовательных нечетных числа.

# Алгоритм решение задачи:
# 0) Задаем левый и правый указатель.
# 1) Проходимся циклом ваилд пока правый указатель не дойдет до конца длины массива,
# 1.1) Если число где стаит левый указатель не четное и число где стаит левый указатель+1 не четное и число где стаит правый указатель не четное,
# 1.1.1) Вернуть True.
# 1.2) Двигаем левый и правый указатель на 1.
# 2) Вернуть False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]

def threeConsecutiveOdds(arr):
    left = 0
    right = 2

    while right < len(arr):
        if arr[left] % 2 != 0 and arr[left + 1] % 2 != 0 and arr[right] % 2 != 0:
            return True

        left += 1
        right += 1

    return False

threeConsecutiveOdds(arr)

assert threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]) == True
assert threeConsecutiveOdds(arr=[2, 6, 4, 1]) == False