### Условие задачи:
# Для заданного целого числа columnNumber вернуть соответствующий ему заголовок столбца, как он отображается в таблице Excel.
# Например:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

# Example 1:
# Input: columnNumber = 1
# Output: "A"

# Example 2:
# Input: columnNumber = 28
# Output: "AB"

# Example 3:
# Input: columnNumber = 701
# Output: "ZY"

### Краткое условие:
# Для заданного целого числа columnNumber вернуть соответствующий ему заголовок столбца, как он отображается в таблице Excel.

# Полное объяснение решение задачи:
# 0) Создаем строку abc со всеми заглавными буквами и пустую строку result.
# 1) Проходимся циклом ваилд пока columnNumber не станет равно 0,
# 1.1) Уменьшаем columnNumber на 1.
# 1.2) result равно буква с индексом columnNumber % 26 из строки abc + result .
# 1.3) Делим columnNumber на 26.
# 2) Вернуть result.

# Сложность:
# 1) Время O(log n)
# 2) Память O(n)

columnNumber = 1

def convertToTitle(columnNumber):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while columnNumber:
        columnNumber -= 1
        result = abc[columnNumber % 26] + result
        columnNumber //= 26

    return result

convertToTitle(columnNumber)

assert convertToTitle(columnNumber=1) == "A"
assert convertToTitle(columnNumber=28) == "AB"
assert convertToTitle(columnNumber=701) == "ZY"