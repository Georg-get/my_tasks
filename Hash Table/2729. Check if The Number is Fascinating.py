### Условие задачи:
# Вам дано целое число n, состоящее ровно из 3 цифр.
# Число назовем n увлекательным,
# если после следующей модификации полученное число содержит все цифры от 1 до 9 ровно один раз и не содержит ни одной 0 буквы:
# Объедините n числа 2 * n и 3 * n.
# Верните true, если n интересно, или false иначе.
# Объединение двух чисел означает их соединение. Например, объединение 121 и 371 есть 121371.

# Example 1:
# Input: n = 192
# Output: true
# Explanation: We concatenate the numbers n = 192 and 2 * n = 384 and 3 * n = 576. The resulting number is 192384576.
# This number contains all the digits from 1 to 9 exactly once.

# Example 2:
# Input: n = 100
# Output: false
# Explanation: We concatenate the numbers n = 100 and 2 * n = 200 and 3 * n = 300. The resulting number is 100200300.
# This number does not satisfy any of the conditions.

### Краткое условие:
# Надо сложить три строки: строка n + строка n*2 + строка n*3 и проверить чтобы в этой строке там не было 0.

# Алгоритм решение задачи:
# 0) Создаем строку result со значением строка n + строка n*2 + строка n*3.
# 1) Проверяем если в строке result число 0, если да то вернуть False.
# 2) Верни длину строки result и длину set строки result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

n = 192

def isFascinating(n):
    result = str(n) + str(2 * n) + str(3 * n)

    if '0' in result:
        return False
    elif len(result) == len(set(result)):
        return True
    else:
        return False
    # return len(result) == len(set(result))

isFascinating(n)

assert isFascinating(n=192) == True
assert isFascinating(n=100) == False