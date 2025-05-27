### Условие задачи:
# Учитывая два массива строк words1 и words2, верните количество строк,
# которые появляются ровно один раз в каждом из двух массивов.

# Example 1:
# Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
# Output: 2
# Explanation:
# - "leetcode" appears exactly once in each of the two arrays. We count this string.
# - "amazing" appears exactly once in each of the two arrays. We count this string.
# - "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
# - "as" appears once in words1, but does not appear in words2. We do not count this string.
# Thus, there are 2 strings that appear exactly once in each of the two arrays.

# Example 2:
# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.

# Example 3:
# Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
# Output: 1
# Explanation: The only string that appears exactly once in each of the two arrays is "ab".

### Краткое условие:
# Учитывая два массива строк words1 и words2, верните количество строк, которые появляются ровно один раз в каждом из двух массивов.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result со значением 0.
# 1) Проходимся циклом по массиву words1,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 1.2) Если ключа i НЕТу в словаре dict, то добавь ключ i в словарь со значением 1.
# 2) Проходимся циклом по массиву words2,
# 2.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 2.2) Если ключа i НЕТу в словаре dict, то добавь ключ i в словарь со значением 1.
# 3) Проходимся циклом по словарю dict,
# 3.1) Если значение ключа k ==2 и k есть в масииве words1 и k есть в масииве words2, то увеличь значение переменной result на 1.
# 4) Верни значение переменной result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

words1 = ["leetcode", "is", "amazing", "as", "is"]
words2 = ["amazing", "leetcode", "is"]


def countWords(words1, words2):
    dict = {}
    result = 0

    for i in words1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {'leetcode': 1, 'is': 2, 'amazing': 1, 'as': 1}
    for j in words2:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
    # {'leetcode': 2, 'is': 3, 'amazing': 2, 'as': 1}
    for k in dict:
        if dict[k] == 2 and k in words1 and k in words2:
            result += 1

    return result # 2

countWords(words1, words2)

assert countWords(words1=["leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"]) == 2
assert countWords(words1=["b", "bb", "bbb"], words2=["a", "aa", "aaa"]) == 0
assert countWords(words1=["a", "ab"], words2=["a", "a", "a", "ab"]) == 1