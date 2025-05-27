### Условие задачи:
# Подстрока — это непрерывная (непустая) последовательность символов внутри строки.
# Подстрока гласных — это подстрока, состоящая только из гласных ( 'a', 'e', 'i', 'o'и 'u') и
# в которой присутствуют все пять гласных.
# Дана строка word, возвращает количество подстрок гласных в ней word.

# Example 1:
# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"

# Example 2:
# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.

# Example 3:
# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"

                                        ### Добавить в список !

### Краткое условие:
# Возвращает количество подстрок гласных в ней word.

###                         С хэшом таблицы (хэш сет)
# Алгоритм решение задачи:
# 0) Создаем: словарь dictVowel с гласными буквами англиского алфавита, и переменную count со значением 0.
# 1) Проходимся циклом по диапазону от 0 до длины строки word,
# 1.1) Создаем пустое множество setDict.
# 1.2) Если ключ i элемент из строки word есть в словаре dictVowel,
# 1.2.1) То проходимся циклом по диапазону от i до длины строки word,
# 1.2.1.1) Если ключ j элемент из строки word есть в словаре dictVowel,
# 1.2.1.1.1) То добавь в словарь setDict j элемент из строки word.
# 1.2.1.1.2) Если словарь setDict равен dictVowel, то увеличь значение перемной count на 1.
# 1.2.1.2) Иначе, выйди из цикла.
# 2) Верни число count.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(1)

### Сложная задача !!!

word = "cuaieuouac"

def countVowelSubstrings(word):
    dictVowel = set("aeiou")  # {'u', 'a', 'e', 'o', 'i'}
    count = 0

    for i in range(len(word)):
        setDict = set()

        if word[i] in dictVowel:
            for j in range(i, len(word)):
                if word[j] in dictVowel:
                    setDict.add(word[j])

                    if setDict == dictVowel:
                        count += 1
                else:
                    break

    return count

countVowelSubstrings(word)

assert countVowelSubstrings(word="aeiouu") == 2
assert countVowelSubstrings(word="unicornarihan") == 0
assert countVowelSubstrings(word="cuaieuouac") == 7

###                         Без хэша таблицы
# Алгоритм решение задачи:
# 0) Создаем пустую переменную result.
# 1) Проходимся циклом по диапазону длине строки,
# 1.1) Проходимся циклом по диапазону(i+1, длине строки+1),
# 1.1.1) Если есть ключси "aeiou" в строке word и длина словаря без повторений равна 5, то увеличь значение переменной result на 1.
# 2) Вернуть переменную result

# Сложность:
# 1) Время O(n^3)
# 2) Память O(1)

# word = "cuaieuouac"
#
# def countdictVowelSubstrings(word):
#     result = 0
#
#     for i in range(len(word)):
#         for j in range(i + 1, len(word) + 1):
#             if set(word[i:j]).issubset('aeiou') and len(set(word[i:j])) == 5:
#                 result += 1
#     return result
#
# countdictVowelSubstrings(word)