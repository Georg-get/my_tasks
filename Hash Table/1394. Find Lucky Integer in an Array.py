### Условие задачи:
# Учитывая массив целых чисел arr, счастливое целое число — это целое число, частота которого в массиве равна его значению.
# Возвращает наибольшее счастливое целое число в массиве. Если счастливого целого числа нет, return -1.

# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# Example 3:
# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.

### Краткое условие:
# Надо найти число, которое будет совпадать по количеству повторений и значению в массиве arr.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result.
# 2) Проходимся циклом по массиву arr,
# 2.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 2.2) Если ключ i НЕТу в словаре dict, то добавь ключ i со значением 1 в словарь dict.
# 3) Проходимся циклом по словарю dict,
# 3.1) Если ключ j равен своему значению, то добавь j в массив result.
# 4) Если длина массива result равна 0, то верни -1.
# 5) Если длина массива result НЕ равна 0, то верни максивальный элемент из массива result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

arr = [1, 2, 2, 3, 3, 3]

def findLucky(arr):
    dict = {}
    result = []

    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {1: 1, 2: 2, 3: 3}
    for j in dict:
        if j == dict[j]:
            result.append(j)
    # [1, 2, 3]
    if len(result) == 0:
        return -1
    else:
        return max(result)  # 3

findLucky(arr)

assert findLucky(arr=[2, 2, 3, 4]) == 2
assert findLucky(arr=[1, 2, 2, 3, 3, 3]) == 3
assert findLucky(arr=[2, 2, 2, 3, 3]) == -1