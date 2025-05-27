### Условие задачи:
# Строку можно сократить, заменив любое количество несмежных, непустых подстрок их длинами.
# Длины не должны иметь начальных нулей.
# Например, строка, такая как "substitution", может быть сокращена как (но не ограничивается):
# • "slOn" ("s ubstitutio n" )
# • "sub4u4" ("sub stit u tion" )
# • "12" ("substitution" )
# • "suiluZon" ("su bst i t u ti on" )
# • "substitution" (подстроки не заменены)
# Следующие сокращения не являются допустимыми:
# • "s55n" ("s ubsti tutio n", замененные подстроки являются смежными)
# • "s010n" (имеет начальные нули)
# • "substitution" (заменяет пустую подстроку)
# Для заданной строки word и сокращения abbr, вернуть, соответствует ли строка заданному сокращению.
# Подстрока — это непрерывная непустая последовательность символов в строке.

# Example 1:
# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

# Example 2:
# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".


### Краткое условие:
# Вернуть true если строка word сокращается до строки abbr. Иначе false.

# Алгоритм решение задачи:
# 0) Задаем левый и правый указатель.
# 1) Проходимся циклом ваилд пока левый указатель не дойдет до конца строи word и пока правый указатель не дойдет до конца строи abbr,
# 1.1) Если левый и правый указатель равны, то увелись левый и правый указатели на 1 и пропусти итерацию.
# 1.2) Если правый указатель установлен на цифре или установлен на 0, то верни False.
# 1.3) num = 0.
# 1.4) Проходимся циклом ваилд пока правый указатель не дойдет до конца строки abbr и не остановиться на цифре,
# 1.4.1) num = num * 10 + int(abbr[right])
# 1.4.2) Увеличиваем правый указатель на 1.
# 1.5) Увеличиваем левый указатель на num.
# 2) Если левый указатель дошел до конца строки word и правый указатель дошел до конца строки abbr, верни True.
# 3) Иначе, верни False.

# Сложность:
# 1) Время O(n + m)
# 2) Память O(1)

word = "internationalization"
abbr = "i12iz4n"

def validWordAbbreviation(word, abbr):
    left = 0
    right = 0

    while left < len(word) and right < len(abbr):
        if word[left] == abbr[right]:
            left += 1
            right += 1
            continue # пропусти итерацию и иди к слюдующим элементом.

        if not abbr[right].isdigit() or abbr[right] == '0':
            return False
        num = 0

        while right < len(abbr) and abbr[right].isdigit():
            num = num * 10 + int(abbr[right])
            right += 1

        left += num

    if left == len(word) and right == len(abbr):
        return True
    else:
        return False

validWordAbbreviation(word, abbr)

assert validWordAbbreviation(word="internationalization", abbr="i12iz4n") == True
assert validWordAbbreviation(word="apple", abbr="a2e") == False

### Оригинал решение ####
#
# class Solution:
#   def validWordAbbreviation(self, word: str, abbr: str) -> bool:
#     i = 0  # word's index
#     j = 0  # abbr's index
#
#     while i < len(word) and j < len(abbr):
#       if word[i] == abbr[j]:
#         i += 1
#         j += 1
#         continue
#       if not abbr[j].isdigit() or abbr[j] == '0':
#         return False
#       num = 0
#       while j < len(abbr) and abbr[j].isdigit():
#         num = num * 10 + int(abbr[j])
#         j += 1
#       i += num
#
#     return i == len(word) and j == len(abbr)