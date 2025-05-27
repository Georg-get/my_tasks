### Условие задачи:
# Учитывая строку с индексом 0 word и символ ch, переверните ее сегмент, word который начинается с индекса 0
# и заканчивается индексом первого вхождения (ch включительно ) . Если персонаж chне существует в word, ничего не делайте.
# Например, если word = "abcdefd" и ch = "d", то вам следует поменять местами сегмент, который начинается 0
# и заканчивается 3 (включительно ). Результирующая строка будет."dcbaefd"
# Верните полученную строку.

# Example 1:
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

# Example 2:
# Input: word = "xyxzxe", ch = "z"
# Output: "zxyxxe"
# Explanation: The first and only occurrence of "z" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

# Example 3:
# Input: word = "abcd", ch = "z"
# Output: "abcd"
# Explanation: "z" does not exist in word.
# You should not do any reverse operation, the resulting string is "abcd".

### Краткое условие:
# Надо найти букву из строки ch в строке word и от этой буквы ch повернуть на оборот буквы и вернуть строку.

# Алгоритм решение задачи:
# 0) Если строки ch нету в строке word, то верни word.
# 1) Создаем:
# 1.1) Массив result со значением строки word
# 1.2) Пременные left со значением 0 и right со значением идекса буквы ch в массиве result.
# 2) Проходимся циклом ваидл пока left не станет меньше чем right,
# 2.1) Меняем местами буквы
# 2.2) Увеличиваем left на 1 и уменьшаем right на 1.
# 3) Вернуть строку из массива result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

word = "abcdefd"
ch = "d"

def reversePrefix(word, ch):
    if ch not in word: # Нужно для третьего юнитеста !!!
        return word

    result = list(word)  # ['a', 'b', 'c', 'd', 'e', 'f', 'd']
    left = 0
    right = result.index(ch)  # 3

    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    # ['d', 'c', 'b', 'a', 'e', 'f', 'd']
    return "".join(result)  # dcbaefd

reversePrefix(word, ch)

assert reversePrefix(word="abcdefd", ch="d") == "dcbaefd"
assert reversePrefix(word="xyxzxe", ch="z") == "zxyxxe"
assert reversePrefix(word="abcd", ch="z") == "abcd" # Он !!!