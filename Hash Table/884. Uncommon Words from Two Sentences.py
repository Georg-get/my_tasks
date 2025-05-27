### Условие задачи:
# Предложение представляет собой строку слов, разделенных одним пробелом, где каждое слово состоит только из строчных букв .
# Слово считается необычным , если оно встречается ровно один раз в одном из предложений и не встречается в другом предложении.
# Учитывая два предложения s1 и s2, верните список всех необычных слов. Вы можете вернуть ответ в любом порядке.

# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]

# Example 2:
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]

### Краткое условие:
# Вывести те слова, которые не повторяются в двух строках s1 и s2.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result, и помешаем строку s1 в массив masS1 и
# помешаем строку s2 в массив masS2.
# 1) Проходимся циклом по массиву masS1,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа на 1.
# 1.2) Если ключ i НЕТу в словаре dict, то добавь ключ i со значением 1 в словарь dict.
# 2) Проходимся циклом по массиву masS2,
# 2.1) Если ключ j есть в словаре dict, то увеличь значение ключа на 1.
# 2.2) Если ключ j НЕТу в словаре dict, то добавь ключ i со значением 1 в словарь dict.
# 3) Проходимся циклом по словарю dict,
# 3.1) Если значение ключа k равно 1, то добавь ключ k в массив result.
# 4) Вернуть массив result.

# Сложность:
# 1) Время O(n) (m+n)
# 2) Память O(n) (m+n)

s1 = "this apple is sweet"
s2 = "this apple is sour"

def uncommonFromSentences(s1, s2):
    dict = {}
    masS1 = s1.split(" ") # ['this', 'apple', 'is', 'sweet']
    masS2 = s2.split(" ") # ['this', 'apple', 'is', 'sour']
    result = []

    for i in masS1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {'this': 1, 'apple': 1, 'is': 1, 'sweet': 1}

    for j in masS2:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
    # {'this': 2, 'apple': 2, 'is': 2, 'sweet': 1, 'sour': 1}

    for k in dict:
        if dict[k] == 1:
            result.append(k)

    # ['sweet', 'sour']
    return result

uncommonFromSentences(s1, s2)

assert uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour") == ["sweet", "sour"]
assert uncommonFromSentences(s1="apple apple", s2="banana") == ["banana"]