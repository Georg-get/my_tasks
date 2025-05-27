### Условие задачи:
# Дана строка s, состоящая из слов и пробелов, верните длину последнего слова в строке.
# Слово – это максимум подстрока состоящий только из символов, не являющихся пробелами.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

### Краткое условие:
# Надо вернуть длину последнего слова в строке s.

# Алгоритм решение задачи:
# 0) Создаем переменную listS со значением массива с словами из строки s.
# 1) Верни длину последнего элемента массива listS.


# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "Hello World"

def lengthOfLastWord(s):

    listS = s.split() # ['Hello', 'World']
                # 5
    return len(listS[-1]) # return len(s.split()[-1])

lengthOfLastWord(s)

assert lengthOfLastWord(s="Hello World") == 5
assert lengthOfLastWord(s="   fly me   to   the moon  ") == 4
assert lengthOfLastWord(s="luffy is still joyboy") == 6