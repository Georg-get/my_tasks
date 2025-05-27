### Условие задачи:
# Дан массив arr, замените каждый элемент в этом массиве наибольшим элементом среди элементов справа от него,
# а последний элемент замените на -1.
# После этого верните массив.

# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation:
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# Example 2:
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

### Краткое условие:
# Дан массив arr, замените каждый элемент в этом массиве наибольшим элементом среди элементов справа от него,
# а последний элемент замените на -1.
# После этого верните массив.

# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

arr = [17, 18, 5, 4, 6, 1]


def replaceElements(arr):
    m = -1

    for i in range(len(arr) - 1, -1, -1):  # range(5, -1, -1)
        if arr[i] > m:
            m, arr[i] = arr[i], m
        else:
            arr[i] = m
    return arr


replaceElements(arr)

assert replaceElements(arr=[17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
assert replaceElements(arr=[400]) == [-1]
