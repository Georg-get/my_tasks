### Условие задачи:
# Вам дан строковый массив с нулевым индексом words, words[i]состоящий из строчных английских букв.
# За одну операцию выберите любой индекс, iтакой, что 0 < i < words.lengthи words[i - 1]и words[i]являются анаграммами , и удалите words[i] из words.
# Продолжайте выполнять эту операцию до тех пор, пока вам удастся выбрать индекс, удовлетворяющий условиям.
# Возврат words после выполнения всех операций.
# Можно показать, что выбор индексов для каждой операции в любом произвольном порядке приведет к одному и тому же результату.
# Анаграмма — это слово или фраза, образованная путем перестановки букв другого слова или фразы с использованием всех исходных букв ровно один раз .
# Например, "dacb"это анаграмма "abdc".

# Example 1:
# Input: words = ["abba","baba","bbaa","cd","cd"]
# Output: ["abba","cd"]
# Explanation:
# One of the ways we can obtain the resultant array is by using the following operations:
# - Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
#   Now words = ["abba","baba","cd","cd"].
# - Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
#   Now words = ["abba","cd","cd"].
# - Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
#   Now words = ["abba","cd"].
# We can no longer perform any operations, so ["abba","cd"] is the final answer.

# Example 2:
# Input: words = ["a","b","c","d","e"]
# Output: ["a","b","c","d","e"]
# Explanation:
# No two adjacent strings in words are anagrams of each other, so no operations are performed.

                                                ### Добавить в список !

### Краткое условие:
# Удалить слова анограмы и вернуть только слова, которые не повторяются.

###                         С хэшом таблицы
# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict, со значениемями по умолчанию типа int, и пустые массивы result1 и result2.
# 1) Проходим циклом по массиву words,
# 1.1) Создаем переменную val со значением строки отсортированой i.
# 1.2) Если ключа val нету в словаре dict или последний элемент массива result1 не равен val,
# то добавь val в массив result1 и добавь i в массив result2.
# 1.3) Увеличь значение ключа val на 1.
# 2) Верни массив result2.

# Сложность:
# 1) Время O(n) (n * k * log(k))
# 2) Память O(n)

### Сложная задача !!!

from collections import defaultdict

words = ["abba", "baba", "bbaa", "cd", "cd"]

def removeAnagrams(words):
    dict = defaultdict(int)  # defaultdict(<class 'int'>, {})
    result1 = []
    result2 = []

    for i in words:
        val = "".join(sorted(i))

        if val not in dict or result1[-1] != val:
            result1.append(val)
            result2.append(i)

        dict[val] += 1
    # defaultdict(<class 'int'>, {'aabb': 3, 'cd': 2})
    # result1 = ['aabb', 'cd']
    return result2  # ['abba', 'cd']

removeAnagrams(words)

assert removeAnagrams(words=["abba", "baba", "bbaa", "cd", "cd"]) == ["abba", "cd"]
assert removeAnagrams(words=["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"]

###                         Без хэша таблицы

# Алгоритм решение задачи:
# 0) Создаем переменную i со значением 0.
# 1) Проходимся бесконечным циклом ваил,
# 1.1) Если i равна длина массива words -1, то выйди из цикла.
# 1.2) Если отсортированая строка из массива words равка отсортированая строка из массива words+1, то удали i+1 и
# уменьшь значнеи i на 1.
# 1.3) Увелич значение i на 1.
# 2) Верни массив words.

# Сложность:
# 1) Время O(n^2 * k*log(k))
# 2) Память O(n^2)

# words = ["abba", "baba", "bbaa", "cd", "cd"]
#
# def removeAnagrams(words):
#     i = 0
#
#     while True:
#         if i == len(words) - 1:
#             break
#         print(''.join(sorted(words[i])))
#         if ''.join(sorted(words[i])) == ''.join(sorted(words[i + 1])):
#             words.pop(i + 1)
#             i -= 1
#         i += 1
#     return words
#
# removeAnagrams(words)