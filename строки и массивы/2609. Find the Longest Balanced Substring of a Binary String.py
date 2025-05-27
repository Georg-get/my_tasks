### Условие задачи:
# Вам дана двоичная строка, s состоящая только из нулей и единиц.
# Подстрока s считается сбалансированной, если все нули находятся перед единицами,
# а количество нулей равно количеству единиц внутри подстроки.
# Обратите внимание, что пустая подстрока считается сбалансированной подстрокой.
# Верните длину самой длинной сбалансированной подстроки s.
# Подстрока — это непрерывная последовательность символов внутри строки.

# Example 1:
# Input: s = "01000111"
# Output: 6
# Explanation: The longest balanced substring is "000111", which has length 6.

# Example 2:
# Input: s = "00111"
# Output: 4
# Explanation: The longest balanced substring is "0011", which has length 4.

# Example 3:
# Input: s = "111"
# Output: 0
# Explanation: There is no balanced substring except the empty substring, so the answer is 0.

### Краткое условие:
# Верните длину самой длинной сбалансированной подстроки s.

# Алгоритм решение задачи:
# 0) Создаем пустую строку string.
# 1) Проходимся циклом по диапазону от 0 до 25,
# 1.1) Увеличиваем строку string на '0' + string + '1' .
# 1.2) Если в строке string нету строки s, то вернуть 2 умноженое на i.
# 2) Вернуть 50.

# Сложность:
# 1) Время O(1)
# 2) Память O(n^2)

s = "01000111"

def findTheLongestBalancedSubstring(s):
    string = ''                         # Example: "01000111101"

    for i in range(25):                 # i    string              s

        string = '0' + string + '1'     # 0    ""           "01000111101"

        if string not in s:
            return 2 * i                # 1    "01"         "|01|00|01|111|01|"
                                        # 2    "0011"       "010|0011|1101"
    return 50                           # 3    "000111"     "01|000111|101"

findTheLongestBalancedSubstring(s)

assert findTheLongestBalancedSubstring(s="01000111") == 6
assert findTheLongestBalancedSubstring(s="00111") == 4
assert findTheLongestBalancedSubstring(s="111") == 0