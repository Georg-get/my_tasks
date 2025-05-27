### Условие задачи:
    .



### Краткое условие:
#

# Алгоритм решение задачи:
# 0)

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums=

def longestPalindrome(nums):
    dict = {}

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

longestPalindrome(nums)

assert longestPalindrome(nums="abccccdd") == 7
assert longestPalindrome(nums="a") == 1