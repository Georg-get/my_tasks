### Условие задачи:
# Учитывая строку s, поменяйте местами только все гласные в строке и верните ее.
# Гласные — это 'a', 'e', 'i', 'o', и 'u', и они могут встречаться как в нижнем, так и в верхнем регистре более одного раза.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

### Краткое условие:
# Надо в строке s поменять согласные буквы местами.

# Алгоритм решение задачи:
# 0) Создаем словарь dict с согласмыми буквами и массив result со значениеме строки s, переменную left со значением 0, и
# переменную right со значением длины массива result -1.
# 1) Проходимся циклома ваилд пока left не станет меньше right,
# 1.1) Если буква где устанолвен левый указатель есть в словаре dict и буква где устанолвен правый указатель есть в словаре dict,
# 1.1.1) То поменяй местами буквы в массиве result и увеличь значение переменой left на 1, и уменьши значение перемено right на 1.
# 1.2) Если буква где устанолвен левый указатель НЕТу в словаре dict, то увеличь значение переменой left на 1.
# 1.3) Если буква где устанолвен правый указатель НЕТу в словаре dict, то уменьши значение перемено right на 1.
# 2) Верни строку из массива result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "hello"

def reverseVowels(s):
    dict = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    result = list(s) # ['h', 'e', 'l', 'l', 'o']
    left = 0
    right = len(result) - 1

    while left < right:

        if result[left] in dict and result[right] in dict:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        elif result[left] not in dict:
            left += 1
        elif result[right] not in dict:
            right -= 1
    # ['h', 'o', 'l', 'l', 'e']
    return "".join(result)

reverseVowels(s)

assert reverseVowels(s="hello") == "holle"
assert reverseVowels(s="leetcode") == "leotcede"