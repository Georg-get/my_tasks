### Условие задачи:
# Вам дан массив строк с нулевым индексом words, два целых числа left и right.
# Строка называется строкой гласных, если она начинается с символа гласной и заканчивается символом гласной,
# где символы гласных — 'a', 'e', 'i', 'o'и 'u'.
# Возвращает количество строк гласных words[i], i принадлежащих включающему диапазону[left, right]

# Example 1:
# Input: words = ["are","amy","u"], left = 0, right = 2
# Output: 2
# Explanation:
# - "are" is a vowel string because it starts with 'a' and ends with 'e'.
# - "amy" is not a vowel string because it does not end with a vowel.
# - "u" is a vowel string because it starts with 'u' and ends with 'u'.
# The number of vowel strings in the mentioned range is 2.

# Example 2:
# Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
# Output: 3
# Explanation:
# - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
# - "mu" is not a vowel string because it does not start with a vowel.
# - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
# - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
# The number of vowel strings in the mentioned range is 3.

### Краткое условие:
# Надо вернуть колличество слов, которые начинаются с гласной буквы из диапазона left = 0, right = 2 массива words.

# Алгоритм решение задачи:
# 0) Создаем переменую result со значением 0 и обрезаем массив words по его диапазону left и right и создаем мапу dict с гласными буквами.
# 1) Проходимся циклом по массиву words, если слова в массиве words начинается и заканчивается на букву из мапы dict,
# 1.1) То увеличиваем переменную result на 1.
# 2) Вернуть result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

words = ["are", "amy", "u"]
left = 0
right = 2

def vowelStrings(words, left, right):
    result = 0
    words = words[left:right + 1]
    dict = {'a', 'e', 'i', 'o', 'u'}

    for i in words:
        if i[0] in dict and i[-1] in dict:
            result += 1

    return result

vowelStrings(words, left, right)

assert vowelStrings(words=["are", "amy", "u"], left=0, right=2) == 2
assert vowelStrings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4) == 3