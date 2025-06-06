### Условие задачи:
# Напишите функцию, которая переворачивает строку. Входная строка задается как массив символов s.
# Вы должны сделать это, изменив входной массив на месте, добавив O(1) дополнительную память.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

### Краткое условие:
# Певевернуть все элементы массива s. Последний в начале массива, первый в конце.
# Вернуть массив s.

# Алгоритм решение задачи:
# 0) Создаем переменные: left со значнием 0 и right со значнием длины массива s-1.
# 1) Проходимся циклома ваилд пока left не станет меньше right,
# 1.1) Меняем местами первую букву и последнию букву.
# 1.2) Увеличеваем переменную left на 1 и уменьшаем right на 1.
# 2) Вернуть массив sю

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = ["h", "e", "l", "l", "o"]

def reverseString(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s  # ['o', 'l', 'l', 'e', 'h']

reverseString(s)

assert reverseString(s=["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
assert reverseString(s=["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]