### Условие задачи:
# Слово считается действительным, если:
# Он содержит минимум 3 символа.
# Он содержит только цифры (0–9) и английские буквы (заглавные и строчные).
# Включает в себя как минимум одну гласную.
# Включает в себя как минимум одну согласную.
# Вам дана строка word.
# Верните, true если word допустимо, в противном случае верните false.
# Примечания:
# 'a', 'e', 'i', 'o', 'u', а их заглавные буквы — гласные.
# Согласная — это английская буква, не являющаяся гласной.

# Example 1:
# Input: word = "234Adas"
# Output: true
# Explanation:
# This word satisfies the conditions.

# Example 2:
# Input: word = "b3"
# Output: false
# Explanation:
# The length of this word is fewer than 3, and does not have a vowel.

# Example 3:
# Input: word = "a3$e"
# Output: false
# Explanation:
# This word contains a '$' character and does not have a consonant.

### Краткое условие:
# Верните, true если word допустимо, в противном случае верните false.

# Полное объяснение решение задачи:
# 0) Если длина строки word меньше 3, то вернуть False.
# 1) Создаем множества: где только символы из строки word, где только символы, где только глассыне буквы и где только согласные буквы.
# 2) Если длина множества dictSetWord и dictSetSymbols равны 0 и длина множества dictSetWord и dictSetVowels больше 0 и
# длина множества dictSetWord и dictSetConsonants больше 0, то верни True.
# 3) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

word = "234Adas"

def isValid(word):
    if len(word) < 3:
        return False

    dictSetWord = set(word.lower())  # {'4', 'd', 'a', 's', '2', '3'}
    dictSetSymbols = set('@#$')  # {'$', '#', '@'}
    dictSetVowels = set('aeiou')  # {'o', 'a', 'i', 'u', 'e'}
    dictSetConsonants = set(
        'bcdfghjklmnpqrstvwxyz')  # {'s', 'q', 'z', 'm', 'x', 'h', 'l', 't', 'b', 'j', 'n', 'g', 'r', 'y', 'w', 'v', 'k', 'c', 'p', 'd', 'f'}

    if len(dictSetWord & dictSetSymbols) == 0 and len(dictSetWord & dictSetVowels) > 0 and len(
            dictSetWord & dictSetConsonants) > 0:
        return True
    else:
        return False

isValid(word)

assert isValid(word="234Adas") == True
assert isValid(word="b3") == False
assert isValid(word="a3$e") == False