### Условие задачи:
# Вам дана строка sentence, состоящая из слов, разделенных пробелами. Каждое слово состоит только из строчных и прописных букв.
# Мы хотели бы преобразовать предложение в «козью латынь» (вымышленный язык, похожий на свиную латынь).
# Правила козлиной латыни следующие:
# Если слово начинается с гласной ( 'a', 'e', 'i', 'o'или 'u'), добавьте ее "ma"в конец слова.
# Например, слово "apple"становится "applema".
# Если слово начинается с согласной (т. е. не с гласной), удалите первую букву и добавьте ее в конец, затем добавьте "ma".
# Например, слово "goat"становится "oatgma".
# Добавьте по одной букве 'a'в конец каждого слова по индексу его слова в предложении, начиная с 1.
# Например, первое слово добавляется "a"в конец, второе слово — "aa"в конец и так далее.
# Возвращает последнее предложение, представляющее преобразование предложения в Goat Latin .

# Example 1:
# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

# Example 2:
# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

### Краткое условие:
# Возвращает последнее предложение, представляющее преобразование предложения в Goat Latin.

# Алгоритм решение задачи:
# 0) Создаем массив arry со всеми согласными буквами англиского алфавита, и массив arrySentence где будут все слова из строки sentence.
# 1) Проходимся циклом по диапазону длины массива arrySentence,
# 1.1) Если согласная буква есть в начале слова из массива arrySentence, то добавь к этому слова "ma",
# 1.2) Если согласная буква НЕТУ есть в начале слова из массива arrySentence, то передвигаем первые букву в конец слова из массива arrySentence и добавляем "ma"
# 1.3) Добавь в конец слова столько букв "a" сколько в индексе i.
# 2) Верни преобразованый массив arrySentence в строку.

# Сложность:
# 1) Время O(n + m)
# 2) Память O(n + m)

sentence = "I speak Goat Latin"

def toGoatLatin(sentence):
    arry = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    arrySentence = sentence.split() # ['I', 'speak', 'Goat', 'Latin']

    for i in range(len(arrySentence)): # range(0, 4)
        if arrySentence[i][0] in arry:
            arrySentence[i] += 'ma'
        else:
            arrySentence[i] = arrySentence[i][1:] + arrySentence[i][0] + 'ma' # передвигаем первые букву в конец слова из массива arrySentence и добавляем "ma"

        arrySentence[i] += 'a' * (i + 1)

    return ' '.join(arrySentence)

toGoatLatin(sentence)

assert toGoatLatin(sentence="I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert toGoatLatin(
    sentence="The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"