### Условие задачи:
# Вам дана строка, s состоящая из строчных английских букв, и разрешено выполнять над ней операции.
# За одну операцию вы можете заменить символ на s другую строчную английскую букву.
# Ваша задача — составить s палиндром за минимально возможное количество операций.
# Если существует несколько палиндромов, которые можно составить с помощью минимального количества операций, сделайте лексикографически наименьший.
# Строка aлексикографически меньше строки b(той же длины), если в первой позиции,
# где a и b отличаются, строка a имеет букву, которая появляется раньше в алфавите, чем соответствующая буква в b.
# Верните полученную строку палиндрома.

# Example 1:
# Input: s = "egcfe"
# Output: "efcfe"
# Explanation: The minimum number of operations to make "egcfe" a palindrome is 1,
# and the lexicographically smallest palindrome string we can get by modifying one character is "efcfe", by changing 'g'.

# Example 2:
# Input: s = "abcd"
# Output: "abba"
# Explanation: The minimum number of operations to make "abcd" a palindrome is 2,
# and the lexicographically smallest palindrome string we can get by modifying two characters is "abba".

# Example 3:
# Input: s = "seven"
# Output: "neven"
# Explanation: The minimum number of operations to make "seven" a palindrome is 1,
# and the lexicographically smallest palindrome string we can get by modifying one character is "neven".

### Краткое условие:
# Надо строку s преобразовать в слова палиндром и вернуть слова палиндром.

# Алгоритм решение задачи:
# 0) Создаем пременные left со значением 0 и right со значением длины строки s, и массив result со значением букв из строки s.
# 1) Проходимся циклом ваилд пока left не станет меньше чем right,
# 1.1) Если указатель left не равен указателю right в массиве result,
# 1.1.1) Меняем значене result[left] на минимальное значение из result[left] или result[right].
# 1.1.2) Меняем значене result[right] на result[left].
# 1.2) Увеличить значение переменной left на 1.
# 1.3) Уменьшить значение переменной right на 1.
# 2) Возвращаем преобразованую строку из массива result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "egcfe"

def makeSmallestPalindrome(s):
    left = 0
    right = len(s) - 1
    result = list(s) # ['e', 'g', 'c', 'f', 'e']

    while left < right:

        if result[left] != result[right]:
            result[left] = min(result[left], result[right])
            result[right] = result[left]

        left += 1
        right -= 1
    # ['e', 'f', 'c', 'f', 'e']
    return ''.join(result) # "efcfe"

makeSmallestPalindrome(s)

assert makeSmallestPalindrome(s="egcfe") == "efcfe"
assert makeSmallestPalindrome(s="abcd") == "abba"
assert makeSmallestPalindrome(s="seven") == "neven"