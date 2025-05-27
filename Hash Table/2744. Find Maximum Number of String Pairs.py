### Условие задачи:
# Вам дан массив с индексом 0,words состоящий из различных строк.
# Строка words[i]может быть соединена со строкой, words[j]если:
# Строка words[i]равна перевернутой строке words[j].
# 0 <= i < j < words.length.
# Возвращает максимальное количество пар, которые можно сформировать из массива words.
# Обратите внимание, что каждая строка может принадлежать не более чем одной паре.

# Example 1:
# Input: words = ["cd","ac","dc","ca","zz"]
# Output: 2
# Explanation: In this example, we can form 2 pair of strings in the following way:
# - We pair the 0th string with the 2nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
# - We pair the 1st string with the 3rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
# It can be proven that 2 is the maximum number of pairs that can be formed.

# Example 2:
# Input: words = ["ab","ba","cc"]
# Output: 1
# Explanation: In this example, we can form 1 pair of strings in the following way:
# - We pair the 0th string with the 1st string, as the reversed string of words[1] is "ab" and is equal to words[0].
# It can be proven that 1 is the maximum number of pairs that can be formed.

# Example 3:
# Input: words = ["aa","ab"]
# Output: 0
# Explanation: In this example, we are unable to form any pair of strings.

### Краткое условие:
# Вернуть число максимального количество пар которые могут сформироваться из элементов массива words.

# Алгоритм решение задачи:
# 0) Создать пустой словарь dict и переменную result = 0.
# 1) Пройтись циклом по массиву words
# 1.1) Создаем переменную sortedI в котором будет храниться i наоборот (cd - > dc).
# 1.2) Если ключ sortedI нету в словаре dict, то добавь ее в словарь dict с ключом sortedI значением равной 0.
# 1.3) Если ключ sortedI есть в словаре dict, то увелич значение ключа sortedI на 1 и увеличь значение переменой result на 1.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

words = ["cd", "ac", "dc", "ca", "zz"]

def maximumNumberOfStringPairs(words):
    dict = {}
    result = 0

    for i in words:
        sortedI = ''.join(sorted(i))

        if sortedI not in dict:
            dict[sortedI] = 0
        else:
            dict[sortedI] += 1
            result += 1
    # {'cd': 1, 'ac': 1, 'zz': 0}
    return result # 2

maximumNumberOfStringPairs(words)

assert maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"]) == 2
assert maximumNumberOfStringPairs(words=["ab", "ba", "cc"]) == 1
assert maximumNumberOfStringPairs(words=["aa", "ab"]) == 0