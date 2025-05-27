### Условие задачи:
# Предложение состоит только из строчных букв ( 'a'to 'z'), цифр ( '0'to '9'), дефисов ( '-'), знаков препинания ( '!', '.', и ',') и пробелов ( ' ').
# Каждое предложение может быть разбито на один или несколько токенов, разделенных одним или несколькими пробелами ' '.
# Токен является допустимым словом, если выполняются все три из следующих условий:
# Он содержит только строчные буквы, дефисы и/или знаки препинания ( без цифр).
# Максимально допустим один дефис '-'. Если он присутствует, он должен быть окружен строчными символами ( "a-b"допустимо, но "-ab"и "ab-"недопустимы).
# Максимум один знак препинания. Если он есть, он должен быть в конце токена ( "ab,", "cd!", и "."являются допустимыми, но "a!b"и "c.,"не являются допустимыми).
# Примерами допустимых слов являются "a-b.", "afad", "ba-c", "a!", и "!".
# Для заданной строки sentence вернуть количество допустимых слов в ней sentence .

# Example 1:
# Input: sentence = "cat and  dog"
# Output: 3
# Explanation: The valid words in the sentence are "cat", "and", and "dog".

# Example 2:
# Input: sentence = "!this  1-s b8d!"
# Output: 0
# Explanation: There are no valid words in the sentence.
# "!this" is invalid because it starts with a punctuation mark.
# "1-s" and "b8d" are invalid because they contain digits.

# Example 3:
# Input: sentence = "alice and  bob are playing stone-game10"
# Output: 5
# Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
# "stone-game10" is invalid because it contains digits.

### Краткое условие:
# Надо вернуть колличество слов которые будут без цифр и символов из строки sentence.

# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 0 и pattern c нашей регуляркой, и массив sentenceList со значением слов из строки sentence.
# 1) Проходимся циклом по массиву sentenceList,
# 1.1) Если слова i проходит регулярку pattern, то увеличь result на 1.
# 2) Верни result.

# Сложность:
# 1) Время O(n*m)
# 2) Память O(n)

import re

sentence = "cat and  dog"

def countValidWords(sentence):
    result = 0
    pattern = "^([a-z]+(-?[a-z]+)?)?(!|\.|,)?$"
    sentenceList = sentence.split() # ['cat', 'and', 'dog']

    for i in sentenceList:

        if re.match(pattern, i):
            result += 1

    return result

countValidWords(sentence)

assert countValidWords(sentence="cat and  dog") == 3
assert countValidWords(sentence="!this  1-s b8d!") == 0
assert countValidWords(sentence="alice and  bob are playing stone-game10") == 5
assert countValidWords(sentence="he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.") == 6 # этот юнитест не пропускает решение через стек !!!

### Не проходят юнитесты 89 / 244 testcases passed
# sentence = "cat and  dog"
#
# def countValidWords(sentence):
#     digitsDict = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
#     symbolsDict = {"!", ".", ",", "-"}
#     stack = []
#
#     for word in sentence.split():
#        Если слова i нету элемента который есть в словаре digitsDict или в словаре symbolsDict.
#         if not any(char in digitsDict or char in symbolsDict for char in word):
#             stack.append(word)
#
#     return len(stack)
#
# countValidWords(sentence)
