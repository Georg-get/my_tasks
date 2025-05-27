### Условие задачи:
# Вам дан массив различных целых чисел arr и массив массивов целых чисел pieces, в которых целые числа pieces различны.
# Ваша цель — сформировать путем объединения массивов в любом порядке.
# Однако вам не разрешено изменять порядок целых чисел в каждом массиве .arr pieces[i]
# Возврат true, если можно сформировать массив arr из pieces. В противном случае вернитесь false.

# Example 1:
# Input: arr = [15,88], pieces = [[88],[15]]
# Output: true
# Explanation: Concatenate [15] then [88]

# Example 2:
# Input: arr = [49,18,16], pieces = [[16,18,49]]
# Output: false
# Explanation: Even though the numbers match, we cannot reorder pieces[0].

# Example 3:
# Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# Output: true
# Explanation: Concatenate [91] then [4,64] then [78]


### Краткое условие:
# Вернуть true перестановка двух чисел.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result.
# 1) Проходимся циклом по мастрице pieces, дублируем ключ как значение в словарь dict.
# 2) Проходимся циклом по массиву arr,
# 2.1) Если i есть в словаре dict, то добавь значение ключа i в массив result.
# 3) Если из элементов списка pieces составить исходный список arr в том же порядке, что и в arr, то верни True.
# 4) Если из элементов списка pieces НЕ составить исходный список arr в том же порядке, что и в arr, то верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

arr = [15, 88]
pieces = [[88], [15]]

def canFormArray(arr, pieces):
    dict = {}
    result = []

    for i in pieces:
        dict[i[0]] = i
    # {88: [88], 15: [15]}
    for i in arr:
        if i in dict:
            result.append(dict[i])
    # [[15], [88]]
    if "".join(str(i) for i in arr) == "".join(str(j) for i in result for j in i):
        return True
    else:
        return False

canFormArray(arr, pieces)