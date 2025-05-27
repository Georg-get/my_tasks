### Условие задачи:
# Учитывая массив целых чисел arr, возврат true,
# если количество вхождений каждого значения в массиве уникально или false нет.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Example 2:
# Input: arr = [1,2]
# Output: false

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

### Краткое условие:
# Вернуть true, если каждое число имеет дубль в массиве arr. А если дубликатов нету в массиве arr вернуть false.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по массиву arr,
# 1.1) Если ключа i НЕТу в словаре dict,
# 1.1.1) Есть количество вхождений i элемента из массива arr НЕТу в словаре dict как значение,
# 1.1.1.1) то добавить i как ключ со значением количество вхождений i элемента из массива arr
# 1.1.2) Есть количество вхождений i элемента из массива arr ЕСТЬ в словаре dict как значение, то верни False.
# 2) Вернуть True.

# Сложность:
# 1) Время O(n) (n^2)
# 2) Память O(n)

arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

def uniqueOccurrences(arr):
    dict = {}

    for i in arr:
        if i not in dict.keys():
            if arr.count(i) not in dict.values():
                dict[i] = arr.count(i)
            else:
                return False
    # {-3: 3, 0: 2, 1: 4, 10: 1}
    return True

uniqueOccurrences(arr)

assert uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]) == True
assert uniqueOccurrences(arr=[1, 2]) == False # {1: 1}
assert uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True