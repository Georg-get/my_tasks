### Условие задачи:
# Вам дана строка, s состоящая только из букв 'a'и 'b'. За один шаг вы можете удалить одну палиндромную подпоследовательность из s.
# Возвращает минимальное количество шагов, чтобы сделать данную строку пустой .
# Строка является подпоследовательностью данной строки, если она генерируется путем удаления некоторых символов данной строки без изменения ее порядка.
# Обратите внимание, что подпоследовательность не обязательно должна быть непрерывной.
# Строка называется палиндромом, если она читается одинаково как в прямом, так и в обратном направлении.

# Example 1:
# Input: s = "ababa"
# Output: 1
# Explanation: s is already a palindrome, so its entirety can be removed in a single step.

# Example 2:
# Input: s = "abb"
# Output: 2
# Explanation: "abb" -> "bb" -> "".
# Remove palindromic subsequence "a" then "bb".

# Example 3:
# Input: s = "baabb"
# Output: 2
# Explanation: "baabb" -> "b" -> "".
# Remove palindromic subsequence "baab" then "b".

### Краткое условие:
# Если вся строка палиндром то вернуть 1, если в строке можно удалить один символ и строка станет палиндромам то вернуть 2.

# Алгоритм решение задачи:
# 0) Создаем переменные left со значением 0 и right со значением длины строки s-1.
# 1) Проходимся циклом ваилд пока left не станет меньше чем right,
# 1.1) Если символы на которых строит указатель left и right из строки s не одинаковые, то верни 2.
# 1.2) Увеличь переменную left на 1 и уменьши переменную right на 1.
# 2) Верни 1.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "ababa"

def removePalindromeSub(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return 2
        left += 1
        right -= 1

    return 1

removePalindromeSub(s)

assert removePalindromeSub(s="ababa") == 1
assert removePalindromeSub(s="abb") == 2
assert removePalindromeSub(s="baabb") == 2