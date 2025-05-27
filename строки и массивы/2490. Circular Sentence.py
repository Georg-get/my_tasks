### Условие задачи:
# Предложение представляет собой список слов, разделенных одним пробелом, без начальных и конечных пробелов.
# Например, "Hello World", "HELLO", "hello world hello world"— это все предложения.
# Слова состоят только из заглавных и строчных английских букв. Прописные и строчные английские буквы считаются разными.
# Предложение является кольцевым, если:
# Последний символ слова равен первому символу следующего слова.
# Последний символ последнего слова равен первому символу первого слова.
# Например, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" все являются круговыми предложениями.
# Однако , "Leetcode is cool", "happy Leetcode" и "Leetcode" не "I like Leetcode" являются круговыми предложениями.
# Дана строка sentence, вернуть, true если она циклическая. В противном случае вернуть false.

# Example 1:
# Input: sentence = "leetcode exercises sound delightful"
# Output: true
# Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
# - leetcode's last character is equal to exercises's first character.
# - exercises's last character is equal to sound's first character.
# - sound's last character is equal to delightful's first character.
# - delightful's last character is equal to leetcode's first character.
# The sentence is circular.

# Example 2:
# Input: sentence = "eetcode"
# Output: true
# Explanation: The words in sentence are ["eetcode"].
# - eetcode's last character is equal to eetcode's first character.
# The sentence is circular.

# Example 3:
# Input: sentence = "Leetcode is cool"
# Output: false
# Explanation: The words in sentence are ["Leetcode", "is", "cool"].
# - Leetcode's last character is not equal to is's first character.
# The sentence is not circular.

### Краткое условие:
# Дана строка sentence, вернуть, true если она циклическая. В противном случае вернуть false.

# Алгоритм решение задачи:
# 0) Создаем массив sentenceList со значением строки sentence и строку firstWords со значением первого слова.
# 1) Проходимся циклом по массиву sentenceList с второго слова до конца,
# 1.1) Если первая буква в слове i не совпадает с последней буквой слова firstWords, то верни False.
# 1.2) Запиши в переменную firstWords слова i.
# 2) Если первое и последнее слова в строке sentence совпадают, то верни True.
# 3) Если первое и последнее слова в строке sentence НЕ совпадают, то верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

sentence = "leetcode exercises sound delightful"

def isCircularSentence(sentence):
    sentenceList = sentence.split(' ') # ['leetcode', 'exercises', 'sound', 'delightful']
    firstWords = sentenceList[0] # leetcode

    for i in sentenceList[1:]: # сравниваем первую букву слова i с первой буквой следующего слова
                            #          |    |
                            # ['leetcode', 'exercises', 'sound', 'delightful']
                            #
                            #                       |    |
                            # ['leetcode', 'exercises', 'sound', 'delightful']
                            #
                            #                                |    |
                            # ['leetcode', 'exercises', 'sound', 'delightful']
        if i[0] != firstWords[-1]:
            return False

        firstWords = i # exercises # sound # delightful

    if sentence[0] == sentence[-1]:
        return True
    else:
        return False

isCircularSentence(sentence)

assert isCircularSentence(sentence="leetcode exercises sound delightful") == True
assert isCircularSentence(sentence="eetcode") == True
assert isCircularSentence(sentence="Leetcode is cool") == False