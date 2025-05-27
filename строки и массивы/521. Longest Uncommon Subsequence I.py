### Условие задачи:
# Учитывая две строки a и b, верните длину самой длинной необычной подпоследовательности между a и b.
# Если такой необычной подпоследовательности не существует, верните -1.
# Необычная подпоследовательность между двумя строками — это строка, которая является последовательность
# ровно одного из них.

# Example 1:
# Input: a = "aba", b = "cdc"
# Output: 3
# Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
# Note that "cdc" is also a longest uncommon subsequence.

# Example 2:
# Input: a = "aaa", b = "bbb"
# Output: 3
# Explanation: The longest uncommon subsequences are "aaa" and "bbb".

# Example 3:
# Input: a = "aaa", b = "aaa"
# Output: -1
# Explanation: Every subsequence of string a is also a subsequence of string b.
# Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be -1.

### Краткое условие:
# Если строки a и b равны то вернуть -1, если нет то верни длину самой длинной строки.

# Алгоритм решение задачи:
# 0) Если строки a и b равны то вернуть -1.
# 1) Если строки a и b НЕ равны, то проверь какая строка длинее и верни длину самой длиной строки.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

a = "aba"
b = "cdc"

def findLUSlength(a, b):
    if a == b:
        return -1
    else:
        if len(a) > len(b): # return max(len(a), len(b))
            return len(a)
        else:
            return len(b)


findLUSlength(a, b)

assert findLUSlength(a="aba", b="cdc") == 3
assert findLUSlength(a="aaa", b="bbb") == 3
assert findLUSlength(a="aaa", b="aaa") == -1
assert findLUSlength(a="aefawfawfawfaw", b="aefawfeawfwafwaef") == 17