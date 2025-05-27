### Условие задачи:
# Значение буквенно - цифровой строки можно определить как:
# Числовое представление строки в базовом формате 10, если оно состоит только из цифр.
# В противном случае длина строки.
# Учитывая массив strs буквенно-цифровых строк, верните максимальное значение любой строки в формате strs.

# Example 1:
# Input: strs = ["alic3","bob","3","4","00000"]
# Output: 5
# Explanation:
# - "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
# - "bob" consists only of letters, so its value is also its length, i.e. 3.
# - "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
# - "4" also consists only of digits, so its value is 4.
# - "00000" consists only of digits, so its value is 0.
# Hence, the maximum value is 5, of "alic3".

# Example 2:
# Input: strs = ["1","01","001","0001"]
# Output: 1
# Explanation:
# Each string in the array has value 1. Hence, we return 1.

### Краткое условие:
# Если в массиве strs есть слова, то верни длину этого элемента массива strs. Если там нету слов то верни самую большую цифру.

# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 0.
# 1) Проходимся циклом по массиву strs,
# 1.1) Если i это цифра, то увеличь result маскисальное значение из result и числа i.
# 1.2) Если i НЕ это цифра, то увеличь result маскисальное значение из result и длины строки i.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

strs = ["alic3", "bob", "3", "4", "00000"]

def maximumValue(strs):
    result = 0

    for i in strs:
        if i.isdigit():
            result = max(result, int(i))
        else:
            result = max(result, len(i))

    return result

maximumValue(strs)

assert maximumValue(strs=["alic3", "bob", "3", "4", "00000"]) == 5
assert maximumValue(strs=["1", "01", "001", "0001"]) == 1