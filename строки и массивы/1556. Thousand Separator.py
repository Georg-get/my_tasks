### Условие задачи:
# Дано целое число n, добавьте точку («.») в качестве разделителя тысяч и верните его в строковом формате.

# Example 1:
# Input: n = 987
# Output: "987"

# Example 2:
# Input: n = 1234
# Output: "1.234"

### Краткое условие:
# Дано целое число n, добавьте точку («.») в качестве разделителя тысяч и верните его в строковом формате.

# Алгоритм решение задачи:
# 0) Создаю строичку string со значением строки n и пустой массив stack.
# 1) Проходимся циклом по диапазону от конца строки до 0,
# 1.1) stack добавляем i,
# 1.2) count равно длина строки string - 1
# 1.3) Если count делется на 3 без остатака и i больше 0, то добавь '.' в stack и наче пасс.
# 2) Верни перевернатую строку из массива stack.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

n = 1234

def thousandSeparator(n):
    string = str(n) # 1234
    stack = []

    for i in range(len(string) - 1, -1, -1):  # range(3, -1, -1)
        stack.append(string[i]) # 4 # 3 # 2 # 1
        count = len(string) - i

        if count % 3 == 0 and i > 0:
            stack.append('.')
        else:
            pass

    return ''.join(stack[::-1])

thousandSeparator(n)

assert thousandSeparator(n=987) == "987"
assert thousandSeparator(n=1234) == "1.234"