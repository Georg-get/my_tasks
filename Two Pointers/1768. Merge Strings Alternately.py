### Условие задачи:
# Вам даны две строки word1 и word2. Объедините строки, добавляя буквы в чередующемся порядке, начиная с word1.
# Если строка длиннее другой, добавьте дополнительные буквы в конец объединенной строки.
# Верните объединенную строку.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d

### Краткое условие:
# Надо обьединить две строки чтобы буквы были отстортированы по индексам свой строки.

# Алгоритм решение задачи:
# 0) Создаем пустую строку result, и переменную left со значением длины word1,
# и переменную right со значением длины word2 и переменную i со значенеим 0.
# 1) Проходимся циклом ваилд пока i не станет меньше left или i не станет меньше right,
# 1.1) Если i меньше left, то увеличь переменную result на word1[i] (добавь букву из строки word1 в строку result)
# 1.2) Если i меньше right, то увеличь переменную result на word2[i] (добавь букву из строки word2 в строку result)
# 1.3) Увеличь i на 1.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

word1 = "abc"
word2 = "pqr"

def mergeAlternately(word1, word2):
    result = ""
    left = len(word1)
    right = len(word2)
    i = 0

    while i < left or i < right:

        if i < left:
            result += word1[i]
        # a
        if i < right:
            result += word2[i]
        # ap
        i += 1

    return result  # apbqcr

mergeAlternately(word1, word2)

assert mergeAlternately(word1="abc", word2="pqr") == "apbqcr"
assert mergeAlternately(word1="ab", word2="pqrs") == "apbqrs"
assert mergeAlternately(word1="abcd", word2="pq") == "apbqcd"