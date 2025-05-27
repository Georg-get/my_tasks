### Условие задачи:
# Учитывая строку s, состоящую из строчных или прописных букв, верните длину самого длинного палиндрома,
# который можно построить из этих букв.
# Буквы чувствительны к регистру , например,  "Aa" здесь это не считается палиндромом.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

### Краткое условие:
# Вернуть длину слова палиндрома.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result со значением 0.
# 1) Проходимся по строке s,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Если ключа i НЕТу в словаре dict, то добавь ключ i со значением 1 в словарь dict.
# 1.3) Если значение ключа i делется на два без остатка, то увеличь значение переменной result на 1.
# 1.4) Если значение ключа i НЕ делется на два без остатка, то уменьши значение переменной result на 1.
# 2) Если result больше 1, то верни длину строки s - result + 1.
# 2) Если result МЕНЬШЕ 1, то верни длину строки s.

# Сложность:
# 1) Время O(n)
# 2) Память O(n) (k)

s = "abccccdd"

def longestPalindrome(s):
    dict = {}
    result = 0

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

        if dict[i] % 2 == 1:
            result += 1
        else:
            result -= 1
    # {'a': 1, 'b': 1, 'c': 4, 'd': 2}
    # 2
    if result > 1:
        return len(s) - result + 1
    else:
        return len(s)

longestPalindrome(s)

assert longestPalindrome(s="abccccdd") == 7
assert longestPalindrome(s="a") == 1