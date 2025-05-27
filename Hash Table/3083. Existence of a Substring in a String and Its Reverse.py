### Условие задачи:
# Учитывая строку s, найдите любую подстрока длины 2, которая также присутствует в обратной стороне s.
# Возврат true, если такая подстрока существует, и false в противном случае.

# Example 1:
# Input: s = "leetcode"
# Output: true
# Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

# Example 2:
# Input: s = "abcba"
# Output: true
# Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".

# Example 3:
# Input: s = "abcd"
# Output: false
# Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.

### Краткое условие:
# Если в строке s есть подстрака с длиной 2, которая также присутствует в обратной стороне s.
# Возврат true, иначе false.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по диапазону длины строки s,
# 1.1) Добавляем 2 буквы из строки s как ключ со значением 1 в словарь dict.
# 2) Создаем перемернутую строку reverseLineS.
# 3) Проходимся циклом по диапазону длины строки reverseLineS,
# 3.1) Если в перевернутой строке reverseLineS есть пара букв которая еть в словаре dict, то вернуть True.
# 4) Вернуть False если мы не нашли схожих пар букв.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "leetcode"

def isSubstringPresent(s):
    dict = {}

    for i in range(len(s) - 1): # range(0, 7)
        dict[s[i] + s[i + 1]] = 1
    # {'le': 1, 'ee': 1, 'et': 1, 'tc': 1, 'co': 1, 'od': 1, 'de': 1}
    reverseLineS = s[:: -1]
    # edocteel
    for j in range(len(reverseLineS) - 1): # range(0, 7)
        if reverseLineS[j] + reverseLineS[j + 1] in dict: # "ее" строка есть в словаре dict
            return True
    return False

isSubstringPresent(s)

assert isSubstringPresent(s="leetcode") == True
assert isSubstringPresent(s="abcd") == False
assert isSubstringPresent(s="abcba") == True
assert isSubstringPresent(s="hozpjlo") == False

                                                ### Не все тесты проходят 674 / 717
# s = "leetcode"
#
# def isSubstringPresent(s):
#     dict = {}
#     result = 0
#
#     for i in s:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     # {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}
#
#     for j in dict:
#         if dict[j] > 1:
#             result += 1
#     # 1
#
#     if result >= 1:
#         return True
#     else:
#         return False
#
# isSubstringPresent(s)
#
# assert isSubstringPresent(s="leetcode") == True
# assert isSubstringPresent(s="abcd") == False
# assert isSubstringPresent(s="abcba") == True
# assert isSubstringPresent(s="hozpjlo") == False # тут код падает !!!