### Условие задачи:
# Дан массив целых чисел arr, вернуть true, если мы можем разбить массив на три непустые части с равными суммами.
# Формально мы можем разбить массив, если сможем найти индексы
# i + 1 < jс(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

# Example 1:
# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Example 2:
# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false

# Example 3:
# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

### Краткое условие:
# Дан массив целых чисел arr, вернуть true, если мы можем разбить массив на три непустые части с равными суммами.

# Полное объяснение решение задачи:
# 0) Создаем переменные temp и found со значением 0, summ со значением суммы всех чисел массива arr, part со значением summ деленная на 3.
# 1) Если summ НЕ делется на 3, то верни False.
# 2) Проходимся циклом по массиву arr, увеличиваем temp на i,
# 2.1) Если temp равен part, то temp равен 0, и увеличиваем found на 1.
# 3) Если found больше или равно 3, то верни True.
# 4) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]

def canThreePartsEqualSum(arr):
    temp = 0
    found = 0
    summ = sum(arr)

    part = summ / 3

    if summ % 3 != 0:
        return False

    for i in arr:
        temp += i
        if temp == part:
            temp = 0
            found += 1

    if found >= 3:
        return True
    else:
        return False

canThreePartsEqualSum(arr)

assert canThreePartsEqualSum(arr=[0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) == True
assert canThreePartsEqualSum(arr=[0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) == False
assert canThreePartsEqualSum(arr=[3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) == True