### Условие задачи:
# Дана строка s, содержащая только строчные английские буквы и '?'символ, преобразуйте все символы '?'в строчные буквы так,
# чтобы конечная строка не содержала никаких последовательных повторяющихся символов. Вы не можете изменять не '?'символы.
# Гарантируется, что в заданной строке нет последовательно повторяющихся символов, за исключением'?' .
# Верните окончательную строку после выполнения всех преобразований (возможно, нулевых) .
# Если существует более одного решения, верните любое из них. Можно показать, что ответ всегда возможен при заданных ограничениях.

# Example 1:
# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid.
# Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

# Example 2:
# Input: s = "ubv?w"
# Output: "ubvaw"
# Explanation: There are 24 solutions for this problem.
# Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".

### Краткое условие:
# Верните окончательную строку после выполнения всех преобразований (возможно, нулевых) .

                                        ### Добавить в список !

# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

                    ### Сложная задача !!!

s = "?zs"

def modifyString(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    notins = ''

    for i in alphabet:
        if i not in s:
            notins += i
        if len(notins) > 1:
            break
    # notins = ab
    for i in notins:
        if s.count('??') > 0:
            s = s.replace('??', notins[:2])
        else:
            s = s.replace('?', notins[0])

    # "azs"
    return s

modifyString(s)

assert modifyString(s="?zs") == "azs"
assert modifyString(s="ubv?w") == "ubvaw"
assert modifyString(s="j?qg??b") == "jaqgacb"