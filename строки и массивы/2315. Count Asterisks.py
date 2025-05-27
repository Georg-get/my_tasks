### Условие задачи:
# Вам дана строка s, в которой каждые две последовательные вертикальные полосы '|'сгруппированы в пару.
# Другими словами, 1 -й и 2- й '|' составляют пару, 3- й и 4- й '|' — пару и так далее.
# Возвращает число '*' in s, исключая число '*'между каждой парой'|' .
# Обратите внимание , что каждый '|'будет принадлежать ровно одной паре.

# Example 1:
# Input: s = "l|*e*et|c**o|*de|"
# Output: 2
# Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
# The characters between the first and second '|' are excluded from the answer.
# Also, the characters between the third and fourth '|' are excluded from the answer.
# There are 2 asterisks considered. Therefore, we return 2.

# Example 2:
# Input: s = "iamprogrammer"
# Output: 0
# Explanation: In this example, there are no asterisks in s. Therefore, we return 0.

# Example 3:
# Input: s = "yo|uar|e**|b|e***au|tifu|l"
# Output: 5
# Explanation: The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l".
# There are 5 asterisks considered. Therefore, we return 5.

### Краткое условие:
# Возвращает число '*'in s, исключая число '*'между каждой парой'|' .

# Алгоритм решение задачи:
# 0) Создаем пустой массив stack, и переменные count и result со значением 0.
# 1) Проходимся циклом по строке s,
# 1.1) Если i равна * и count делется на 2 без остатка, то увеличь переменную result на 1.
# 1.2) Если i равна "|", то увеличь переменную count на 1.
# 1.3) Добавляем в stack значение i.
# 2) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "l|*e*et|c**o|*de|"

def countAsterisks(s):
    stack = []
    count = 0
    result = 0
    
    for i in s:

        if i == "*" and count % 2 == 0:
            result += 1

        elif i == "|":
            count += 1

        stack.append(i)
    # ['l', '|', '*', 'e', '*', 'e', 't', '|', 'c', '*', '*', 'o', '|', '*', 'd', 'e', '|']
    return result # 2

countAsterisks(s)

assert countAsterisks(s="l|*e*et|c**o|*de|") == 2
assert countAsterisks(s="iamprogrammer") == 0
assert countAsterisks(s="yo|uar|e**|b|e***au|tifu|l") == 5