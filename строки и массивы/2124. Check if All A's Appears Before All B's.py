### Условие задачи:
# Дана строка s, состоящая только из символов 'a'и 'b', возврат true ,
# если каждый 'a' появляется перед каждым 'b' в строке. В противном случае вернитесь false.

# Example 1:
# Input: s = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
# Hence, every 'a' appears before every 'b' and we return true.

# Example 2:
# Input: s = "abab"
# Output: false
# Explanation:
# There is an 'a' at index 2 and a 'b' at index 1.
# Hence, not every 'a' appears before every 'b' and we return false.

# Example 3:
# Input: s = "bbb"
# Output: true
# Explanation:
# There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

### Краткое условие:
# Возврат true , если каждый 'a' появляется перед каждым 'b' в строке. В противном случае вернитесь false.

# Алгоритм решение задачи:
# 0) Создаем пустой массив stack.
# 1) Проходимся циклом по строке s,
# 1.1) Если i равна строке "b", то добавь i в массив stack.
# 1.2) Если длина массив stack больше 0 и i равна строке "а", верни False.
# 2) Верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "aaabbb"

def checkString(s):
    stack = []

    for i in s:

        if i == "b":
            stack.append(i)

        if len(stack) > 0 and i == "a":
            return False

    return True

checkString(s)

assert checkString(s="aaabbb") == True
assert checkString(s="abab") == False
assert checkString(s="bbb") == True