### Условие задачи:
# Учитывая массив строк words, верните первую палиндромную строку в массиве.
# Если такой строки нет, верните пустую строку "".
# Строка является палиндромной, если она читается одинаково и вперед, и назад.

# Example 1:
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

# Example 2:
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.

### Краткое условие:
# Надо вернуть первое слова палиндром из массива words.

# Алгоритм решение задачи:
# 0) Проходимся циклом по массиву words,
# 0.1) Создаем переменные left со значением 0 и right со значением длины слова -1.
# 0.2) Проходимся циклом ваил пока left не станет меньше right,
# 0.2.1) Если i[left] не равно i[right], то выйди из цикла.
# 0.2.2) Увеличь left на 1 и уменьши right на 1.
# 0.3) Верни i.
# 1) Верни пустую строку.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

words = ["abc", "car", "ada", "racecar", "cool"]

def firstPalindrome(words):
    for i in words:
        left = 0
        right = len(i) - 1

        while left < right:
            if i[left] != i[right]:
                break

            left += 1
            right -= 1
        else:
            return i  # "ada"

    return ""

firstPalindrome(words)

assert firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"]) == "ada"
assert firstPalindrome(words=["notapalindrome", "racecar"]) == "racecar"
assert firstPalindrome(words=["def", "ghi"]) == ""