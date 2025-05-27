### Условие задачи:
# Необычная строка — это строка, в которой никакие три последовательных символа не совпадают.
# Дана строка s, удалите из нее минимально возможное количество символов, s чтобы сделать ее замысловатой.
# Верните окончательную строку после удаления. Можно показать, что ответ всегда будет уникальным.

# Example 1:
# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".

# Example 2:
# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".

# Example 3:
# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".

### Краткое условие:
# Удалить повторяющеся буквы, которые повторяются больше 2 раз в строке s.

# Алгоритм решение задачи:
# 0) Создаем пустой массив stack.
# 1) Проходимся циклом поп строке s,
# 1.1) Если длина стека больше 2,
# или последний элемент стека не равен предпоследниму элемента стека,
# или последний элемент стека не равен i,
# 1.1.1) То добавь i в массив stack.
# 2) Верни строку преобразованую из массив stack.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "leeetcode"

def makeFancyString(s):
    stack = []

    for i in s:
        if len(stack) < 2 or stack[-1] != stack[-2] or stack[-1] != i:
            stack.append(i)

    return "".join(stack)

makeFancyString(s)

assert makeFancyString(s="leeetcode") == "leetcode"
assert makeFancyString(s="aaabaaaa") == "aabaa"
assert makeFancyString(s="aab") == "aab"