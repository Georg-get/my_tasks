### Условие задачи:
# Даны два предложения, представленные в виде массивов строк sentence1 и sentence2,
# а также массив пар строк similarPairs, где каждая пара [xi, yi] указывает на то, что слова xi и yi являются похожими.
# Необходимо вернуть true, если предложения sentence1 и sentence2 являются похожими, или false, если они не похожи.

# Example 1:
# Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
# Output: true
# Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.

# Example 2:
# Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
# Output: true
# Explanation: A word is similar to itself.

# Example 3:
# Input: sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]
# Output: false
# Explanation: As they don't have the same length, we return false.

### Краткое условие:
# Необходимо вернуть true, если предложения sentence1 и sentence2 являются похожими, или false, если они не похожи.

# Алгоритм решение задачи:
# 0) Если длина массива sentence1 не равна длине массива sentence2, то верни False.
# 1) Создаем множество dictSet со значением матрицы similarPairs, где массивы стали кортеджами.
# 2) Проходимся циклом по кортеджу из массивом sentence1 и sentence2,
# 2.1) Если a равно b, или картедж из а и b есть в множестве dictSet, или картедж из b и a есть в множестве dictSet, верни True.
# 2.2) Иначе, верни False.

# Сложность:
# 1) Время O(n+m)
# 2) Память O(m) (n)

sentence1 = ["great", "acting", "skills"]
sentence2 = ["fine", "drama", "talent"]
similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]

def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False
    dictSet = set(map(tuple,
                      similarPairs))  # [["great", "fine"], ["drama", "acting"], ["skills", "talent"]] -> {('drama', 'acting'), ('great', 'fine'), ('skills', 'talent')}

    # dictSet =  {('drama', 'acting'), ('great', 'fine'), ('skills', 'talent')}
    for a, b in zip(sentence1, sentence2):  # [('great', 'fine'),('acting', 'drama'), ('skills', 'talent')]
        # a = great
        # b = fine
        if a == b or (a, b) in dictSet or (b, a) in dictSet:
            return True
        else:
            return False

areSentencesSimilar(sentence1, sentence2, similarPairs)

assert areSentencesSimilar(sentence1=["great", "acting", "skills"], sentence2=["fine", "drama", "talent"],
                           similarPairs=[["great", "fine"], ["drama", "acting"], ["skills", "talent"]]) == True
assert areSentencesSimilar(sentence1=["great"], sentence2=["great"], similarPairs=[]) == True
assert areSentencesSimilar(sentence1=["great"], sentence2=["doubleplus", "good"],
                           similarPairs=[["great", "doubleplus"]]) == False

### Оригинал решение ####

# class Solution:
#     def areSentencesSimilar(
#         self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
#     ) -> bool:
#         if len(sentence1) != len(sentence2):
#             return False
#         s = {(a, b) for a, b in similarPairs}
#         return all(
#             a == b or (a, b) in s or (b, a) in s for a, b in zip(sentence1, sentence2)
#         )