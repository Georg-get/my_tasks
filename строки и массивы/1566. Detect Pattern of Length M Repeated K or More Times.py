### Условие задачи:
# Для заданного массива положительных целых чисел arr найдите шаблон длины m, который повторяется k не менее одного раза.
# Шаблон — это подмассив (последовательная подпоследовательность), состоящий из одного или нескольких значений,
# повторяющихся несколько раз подряд без перекрытия.
# Шаблон определяется его длиной и количеством повторений.
# Верните, true если существует шаблон длины m, который повторяется k более одного раза, в противном случае верните false.

# Example 1:
# Input: arr = [1,2,4,4,4,4], m = 1, k = 3
# Output: true
# Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.

# Example 2:
# Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
# Output: true
# Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid pattern (2,1) is also repeated 2 times.

# Example 3:
# Input: arr = [1,2,1,2,1,3], m = 2, k = 3
# Output: false
# Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.

### Краткое условие:
# Верните, true если существует шаблон длины m, который повторяется k более одного раза, в противном случае верните false.

# Полное объяснение решение задачи:
# 0) Проходимся циклом по индексам массива arr,
# 0.1) Если (i+m) * k равно (i+m* k), то верни True.
# 1) Верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

arr = [1, 2, 4, 4, 4, 4]
m = 1
k = 3

def containsPattern(arr, m, k):
    for i in range(len(arr)):
        if arr[i:i + m] * k == arr[i:i + m * k]:
            return True

    return False

containsPattern(arr, m, k)

assert containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3) == True
assert containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2) == True
assert containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3) == False