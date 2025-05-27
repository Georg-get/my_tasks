### Условие задачи:
# Вам дан массив строк words и строка chars.
# Строка хороша , если она может быть составлена из символов chars(каждый символ можно использовать только один раз).
# Возвращает сумму длин всех хороших строк в словах.

# Example 1:
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

### Краткое условие:
# Вернуть длину слов из массива words, буквы которые есть в строке chars.


                                ### Без хэш таблицы
# Алгоритм решение задачи:
# 0) Создаем пустой массив result.
# 1) Проходимся циклом по массиву words,
# 1.2) Проходимся циклом по слову внутри words,
# 1.2.1) Если количество вхождений текущего символа в текущем слове больше,
# чем количество вхождений этого символа в строке chars,
# то текущее слово не может быть составлено из символов строки chars и происходит выход из цикла
# 1.3) Если нету то добавить слова в массив result.
# 2) Вернуть длину слова из массива result.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(m)

# words = ["cat", "bt", "hat", "tree"]
# chars = "atach"
#
# def countCharacters(words, chars):
#     result = []
#
#     for i in words:
#         for j in i:
#             if i.count(j) > chars.count(j):
#                 break
#         else:
#             result.append(i)
#     # ['cat', 'hat']
#     return len(''.join(result)) #6
#
# countCharacters(words, chars)

                                    ### С хэшем таблицы
# Алгоритм решение задачи:

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

words = ["cat", "bt", "hat", "tree"]
chars = "atach"

def countCharacters(words, chars):
    result = 0
    dictChars = {}

    for i in chars:
        if i in dictChars:
            dictChars[i] += 1
        else:
            dictChars[i] = 1
    # {'a': 2, 't': 1, 'c': 1, 'h': 1}
    for j in words:
        dictWords = {}
        for k in j:
            dictWords[k] = dictWords.get(k, 0) + 1
        # {'c': 1, 'a': 1, 't': 1}
        # {'b': 1, 't': 1}
        # {'h': 1, 'a': 1, 't': 1}
        # {'t': 1, 'r': 1, 'e': 2}
        for k, count in dictWords.items():
            if dictChars.get(k, 0) < count:
                break
        else:
            result += len(j)
    #       6
    return result
countCharacters(words, chars)

assert countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach") == 6
assert countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr") == 10