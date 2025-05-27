### Условие задачи:
# Вам дана строка s.
# Ваша задача — удалить все цифры, выполнив эту операцию несколько раз:
# Удалите первую цифру и ближайший нецифровой символ слева от нее.
# Верните полученную строку после удаления всех цифр.

# Example 1:
# Input: s = "abc"
# Output: "abc"
# Explanation:
# There is no digit in the string.

# Example 2:
# Input: s = "cb34"
# Output: ""
# Explanation:
# First, we apply the operation on s[2], and s becomes "c4".
# Then we apply the operation on s[1], and s becomes "".

### Краткое условие:
# Верните полученную строку после удаления всех цифр.

                                    ### Стек ###

# Алгоритм решение задачи:
# 0) Создаем пустой массив stack.
# 1) Проходимся циклом по строке s,
# 1.1) Если i это цифра и стек не пустой, то удали последний элемент стека.
# 1.2) Иначе, в стек добавь i.
# 2) Верни преобразованую строку stack.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "abc"

def clearDigits(s):
    stack = []

    for i in s:
        if i.isdigit() and len(stack) > 0:
            stack.pop()
        else:
            stack.append(i)

    return "".join(stack)

clearDigits(s)

assert clearDigits(s="abc") == "abc"
assert clearDigits(s="cb34") == ""