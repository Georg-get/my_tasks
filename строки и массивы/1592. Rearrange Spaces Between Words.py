### Условие задачи:
# Вам дана строка text слов, которые размещены между некоторым количеством пробелов.
# Каждое слово состоит из одной или нескольких строчных английских букв и отделено как минимум одним пробелом.
# Гарантируется, что text содержит как минимум одно слово.
# Переставьте пробелы так, чтобы между каждой парой соседних слов было одинаковое количество пробелов, и это количество было максимальным.
# Если вы не можете перераспределить все пробелы равномерно, поместите дополнительные пробелы в конец, то есть возвращаемая строка должна быть той же длины, что и text.
# Верните строку после перестановки пробелов.

# Example 1:
# Input: text = "  this   is  a sentence "
# Output: "this   is   a   sentence"
# Explanation: There are a total of 9 spaces and 4 textArrayLen. We can evenly divide the 9 spaces between the textArrayLen: 9 / (4-1) = 3 spaces.

# Example 2:
# Input: text = " practice   makes   perfect"
# Output: "practice   makes   perfect "
# Explanation: There are a total of 7 spaces and 3 textArrayLen. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.

### Краткое условие:
# Верните строку после перестановки пробелов.

# Алгоритм решение задачи:
# 0) Создаем переменные:
# 0.1) массив textArray со значением слов из строки text,
# 0.2) textArrayLen со значением длины массива textArray,
# 0.3) numberOfSpaces со значением колличество пробелов в строке text,
# 1) Если textArrayLen больше 1, то spacesBetweenWords numberOfSpaces // (textArrayLen - 1) и r = numberOfSpaces % (textArrayLen - 1).
# 2) Иначе, spacesBetweenWords = 0 и r = numberOfSpaces.
# 3) Верни (" " * spacesBetweenWords).join(textArray) + " " * r.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

text = "  this   is  a sentence "

def reorderSpaces(text):
    textArray = text.split() # ['this', 'is', 'a', 'sentence']
    textArrayLen = len(textArray) # 4
    numberOfSpaces = text.count(" ") # 9 - колличество пробелов в строке text

    if textArrayLen > 1:
        spacesBetweenWords = numberOfSpaces // (textArrayLen - 1) # 3
        r = numberOfSpaces % (textArrayLen - 1) # 0
    else:
        spacesBetweenWords = 0
        r = numberOfSpaces

    return (" " * spacesBetweenWords).join(textArray) + " " * r

reorderSpaces(text)

assert reorderSpaces(text="  this   is  a sentence ") == "this   is   a   sentence"
assert reorderSpaces(text=" practice   makes   perfect") == "practice   makes   perfect "