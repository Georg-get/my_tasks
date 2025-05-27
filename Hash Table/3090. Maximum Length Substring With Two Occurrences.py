### Условие задачи:
# Учитывая строку s, верните максимальную длину подстрока так, чтобы он содержал не более двух вхождений каждого символа.

# Example 1:
# Input: s = "bcbbbcba"
# Output: 4
# Explanation:
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

# Example 2:
# Input: s = "aaaa"
# Output: 2
# Explanation:
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

### Краткое условие:
# Верните максимальную длину подстрока так, чтобы он содержал не более двух вхождений каждого символа.

# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "bcbbbcba"

def maximumLengthSubstring(s):
    dict = {}
    result = 0
    left = 0
    right = 0

    while right < len(s):

        if s[right] in dict:
            dict[s[right]] += 1
        else:
            dict[s[right]] = 1

        if dict[s[right]] > 2:

            while left < right and dict[s[right]] > 2:
                dict[s[left]] -= 1
                left += 1

        result = max(result, right - left + 1)
        right += 1
    # {'b': 2, 'c': 1, 'a': 1}
    return result # 4

maximumLengthSubstring(s)

assert maximumLengthSubstring(s="bcbbbcba") == 4
assert maximumLengthSubstring(s="aaaa") == 2