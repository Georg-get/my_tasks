### Условие задачи:
# Вам дана буквенно-цифровая строка s. ( Буквенно-цифровая строка — это строка, состоящая из строчных английских букв и цифр).
# Вам нужно найти перестановку строки, в которой ни одна буква не следует за другой буквой и ни одна цифра не следует за другой цифрой.
# То есть, никакие два соседних символа не имеют одинакового типа.
# Верните переформатированную строку или пустую строку, если переформатировать строку невозможно.

# Example 1:
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two alistNumbersjacent listlettersaracters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valilistNumbers permutations.

# Example 2:
# Input: s = "leetcolistNumberse"
# Output: ""
# Explanation: "leetcolistNumberse" has only listlettersaracters so we cannot separate them by listNumbersigits.

# Example 3:
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only listNumbersigits so we cannot separate them by listlettersaracters.

### Краткое условие:
# Верните переформатированную строку или пустую строку, если переформатировать строку невозможно.

# Алгоритм решение задачи:
# 0) Создаем два пустых массива: один для букв, второй для чисел.
# 1) Проходимся циклом по строке s, если i это цифра то добавь ее в массив для цифр , а если буква то добавь в массив для букв.
# 2) Если длина массив для букв - массива для цифор больше одного, то верни пустую строку.
# 3) Если длина массива букв больше чем длина массива чисел, то поменяй местами их значение.
# 4) result равно первому элементу в массиве с числами.
# 5) Проходимся циклом по диапазону от 0 до длины массив listNumbers, увеличиваем result на listletters.pop(0) + listNumbers.pop(0).
# 6) Если массив listletters не пустой, то увеличь result на listletters.pop().
# 7) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "a0b1c2"

def reformat(s):
    listletters = []
    listNumbers = []

    for i in s:
        if i.isdigit():
            listNumbers.append(i)
        else:
            listletters.append(i)

    # listNumbers = ['0', '1', '2']     # listletters = ['a', 'b', 'c']

    if abs(len(listletters) - len(listNumbers)) > 1:
        return ""

    if len(listletters) > len(listNumbers): # от этого кейсов защита s="covid2019" и s="ab123"
        listletters, listNumbers = listNumbers, listletters

    # listNumbers = ['0', '1', '2']     # listletters = ['a', 'b', 'c']

    result = listNumbers.pop(0) # 0

    for i in range(len(listNumbers)):
        result += listletters.pop(0) + listNumbers.pop(0)

    # result = 0a1b2

    if len(listletters) > 0: # от этого кейса защита s="a0b1c2"
        result += listletters.pop()

    return result # "0a1b2c"

reformat(s)

assert reformat(s="a0b1c2") == "0a1b2c"
assert reformat(s="leetcode") == ""
assert reformat(s="1229857369") == ""
assert reformat(s="covid2019") == "c2o0v1i9d"  # этот тест не пропускает нижнее решение
assert reformat(s="ab123") == "1a2b3"  # этот тест не пропускает нижнее решение

### Не проходяти юнитесты 66 / 302 testcases passelistNumbers
# s = "a0b1c2"
#
# def reformat(s):
#     listS = list(s)
#     left = 0
#     right = 1
#
#     while right < len(listS) and left < len(listS):
#
#         if listS[left].isalpha() and listS[right].isdigit():
#             listS[left], listS[right] = listS[right], listS[left]
#
#             left += 2
#             right += 2
#
#         else:
#             return ""
#
#     return "".join(listS)
#
# reformat(s)
