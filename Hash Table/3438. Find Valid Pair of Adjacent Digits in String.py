### Условие задачи:
# Вам дана строка, s состоящая только из цифр. Допустимая пара определяется как две соседние цифры в s таком порядке:
# Первая цифра не равна второй.
# Каждая цифра в паре появляется s ровно столько раз, сколько соответствует ее числовому значению.
# Возвращает первую допустимую пару, найденную в строке s при обходе слева направо.
# Если допустимой пары не существует, возвращает пустую строку.

# Example 1:
# Input: s = "2523533"
# Output: "23"
# Explanation:
# Digit '2' appears 2 times and digit '3' appears 3 times. Each digit in the pair "23" appears in s exactly as many times as its numeric value. Hence, the output is "23".

# Example 2:
# Input: s = "221"
# Output: "21"
# Explanation:
# Digit '2' appears 2 times and digit '1' appears 1 time. Hence, the output is "21".

# Example 3:
# Input: s = "22"
# Output: ""
# Explanation:
# There are no valid adjacent pairs.

### Краткое условие:
# Возвращает первую допустимую пару, найденную в строке s при обходе слева направо.

# Алгоритм решение задачи:
# 0) Создаем словарь, в котором ключ будет число из строки s, а значение сколько раз это число повторилось в нем.
# 1) Проходимся по индексам массива от 1 до дилны строки s,
# 1.1) Если певедушие число из строки s не равно нынешнему,и преведушие число равно значениею из словаря и число равно значению из словаря,
# 1.1.1) То верни преведушие число + число нынешнене.
# 2) Вернуть пустую строку.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "2523533"

def findValidPair(s):
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in range(1, len(s)):
        if s[i - 1] != s[i] and int(s[i - 1]) == dict[s[i - 1]] and int(s[i]) == dict[s[i]]:
            return s[i - 1] + s[i]

    return ""

findValidPair(s)

assert findValidPair(s="2523533") == "23"
assert findValidPair(s="221") == "21"
assert findValidPair(s="22") == ""
assert findValidPair(s="1522") == ""