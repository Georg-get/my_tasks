### Условие задачи:
# Учитывая массив строк words и строку s, определите, s является ли это аббревиатурой слов.
# Строка s считается аббревиатурой, words если она может быть сформирована путем объединения первого символа каждой строки по words порядку .
# Например, "ab"может быть образовано из ["apple", "banana"], но не может быть образовано из ["bear", "aardvark"].
# Возвращает true if s — это аббревиатура от words, и false в противном случае.

# Example 1:
# Input: words = ["alice","bob","charlie"], s = "abc"
# Output: true
# Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym.

# Example 2:
# Input: words = ["an","apple"], s = "a"
# Output: false
# Explanation: The first character in the words "an" and "apple" are 'a' and 'a', respectively.
# The acronym formed by concatenating these characters is "aa".
# Hence, s = "a" is not the acronym.

# Example 3:
# Input: words = ["never","gonna","give","up","on","you"], s = "ngguoy"
# Output: true
# Explanation: By concatenating the first character of the words in the array, we get the string "ngguoy".
# Hence, s = "ngguoy" is the acronym.

### Краткое условие:
# Если первые буквы слов из массива words равны строке s, то вернуть true. Иначе false.

# Алгоритм решение задачи:
# 0) Если длина массива words не равна длине строки s, то вернуть False.
# 1) Если длина массива words РАВНА длине строки s, то создаем пустую строку result и добавляем первые буквы слов из массив words,
# 1.1) Если строка result похожа на строку s, то верни True.
# 1.2) Если строка result НЕ похожа на строку s, то верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

words = ["alice", "bob", "charlie"]
s = "abc"

def isAcronym(s, words):
    if len(words) != len(s):
        return False

    else:
        result = " "

        for i in words:
            result += i[0]  # a #b #c
            # abc = abc
        if result == s:
            return True
        else:
            return False

isAcronym(s, words)

assert isAcronym(words=["alice", "bob", "charlie"], s="abc") == True
assert isAcronym(words=["an", "apple"], s="a") == False
assert isAcronym(words=["never", "gonna", "give", "up", "on", "you"], s="ngguoy") == True