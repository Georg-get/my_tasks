### Условие задачи:
# Учитывая строку s, найдите длину самой длинной подстрока без повторения символов.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Краткое условие:
# Дана строка, найдите длину самой длинной подстроки без повторяющихся символов.

# Алгоритм решение задачи:
# 0) Создаем две переменные result и left со значением 0 и пустой словарь dict.
# 1) Проходимся циклом по диапазону длины строки s,
# 1.1) Если ключ i из строки s есть в словаре dict, то присвой переменой left значнеие максмльного числа из left и dict[s[i]] + 1.
# 1.2) Значение ключа s[i] из словаря dict равна i.
# 1.3) Присваеваем переменной result значение максимам между result и i - left + 1.
# 2) Вернуть переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "abcabcbb"

def lengthOfLongestSubstring(s):
    result = 0
    left = 0
    dict = {}

    for i in range(len(s)):

        if s[i] in dict:
            left = max(left, dict[s[i]] + 1)  # 0 1 => 1

        dict[s[i]] = i  # 0
        result = max(result, i - left + 1)
    # {'a': 3, 'b': 7, 'c': 5}
    return result

lengthOfLongestSubstring(s)

assert lengthOfLongestSubstring(s="abcabcbb") == 3
assert lengthOfLongestSubstring(s="bbbbb") == 1
assert lengthOfLongestSubstring(s="pwwkew") == 3