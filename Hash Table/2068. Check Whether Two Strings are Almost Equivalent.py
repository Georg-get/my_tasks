### Условие задачи:
# Две строки word1 и word2 считаются почти эквивалентными,
# если разница между частотами каждой буквы от 'a'до и не превышает.'z' word1 word2 3
# Учитывая две строки word1 и word2, каждая из которых имеет длину n,
# возвращает true if word1 и почти word2 эквивалентны или false нет.
# Частота буквы — это количество раз, когда она встречается в строке.x

# Example 1:
# Input: word1 = "aaaa", word2 = "bccb"
# Output: false
# Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
# The difference is 4, which is more than the allowed 3.

# Example 2:
# Input: word1 = "abcdeef", word2 = "abaaacc"
# Output: true
# Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
# - 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
# - 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
# - 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
# - 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
# - 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
# - 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.

# Example 3:
# Input: word1 = "cccddabba", word2 = "babababab"
# Output: true
# Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
# - 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
# - 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
# - 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
# - 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.

### Краткое условие:
# Вернуть True, если колличество повторяющися букв в массивах word1 и word2 совпадают.
# Количество значений ключей двух словарей совпадает !!!

# Алгоритм решение задачи:
# 0) Создаем два пустых словаря dict1 и dict2.
# 1) Проходимся циклом по массиву word1,
# 1.1) Если ключа i НЕТу в словаре dict1, то добавь ключ i со значением 0.
# 1.2) Добавь ключ i со значением в словарь и увеличь его значение на 1.
# 2) Проходимся циклом по массиву word2,
# 2.1) Если ключа j НЕТу в словаре dict2, то добавь ключ j со значением 0.
# 2.2) Добавь ключ j со значением в словарь и увеличь его значение на 1.
# 3) Проходимся циклом по словарю dict1,
# 3.1) Если ключ key есть в словаре dict2, и если abs(dict2[key] - dict1[key])(не отрицательное число) > 3, то вернуть False.
# 3.2) Если ключ key НЕТу в словаре dict2, и если dict1[key] > 3, то вернуть False.
# 4) Проходимся циклом по словарю dict2,
# 4.1) Если ключ key есть в словаре dict1, и если abs(dict2[key] - dict1[key])(не отрицательное число) > 3, то вернуть False.
# 4.2) Если ключ key НЕТу в словаре dict1, и если dict2[key] > 3, то вернуть False.
# 5) Вернуть True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

word1 = "cccddabba"
word2 = "babababab"

def checkAlmostEquivalent(word1, word2):
    dict1 = {}
    dict2 = {}

    for i in word1:
        if i not in dict1:
            dict1[i] = 0
        dict1[i] += 1
    # {'c': 3, 'd': 2, 'a': 2, 'b': 2}
    for j in word2:
        if j not in dict2:
            dict2[j] = 0
        dict2[j] += 1
    # {'b': 5, 'a': 4}
    for key in dict1:
        if key in dict2:
            if abs(dict2[key] - dict1[key]) > 3:
                return False
        else:
            if dict1[key] > 3:
                return False
    # {'c': 3, 'd': 2, 'a': 2, 'b': 2}
    for key in dict2:
        if key in dict1:
            if abs(dict2[key] - dict1[key]) > 3:
                return False
        else:
            if dict2[key] > 3:
                return False
    # {'b': 5, 'a': 4}
    return True

checkAlmostEquivalent(word1, word2)

assert checkAlmostEquivalent(word1="aaaa", word2="bccb") == False
assert checkAlmostEquivalent(word1="abcdeef", word2="abaaacc") == True
assert checkAlmostEquivalent(word1="cccddabba", word2="babababab") == True