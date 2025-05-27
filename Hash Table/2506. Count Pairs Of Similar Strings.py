### Условие задачи:
# Вам дан строковый массив с нулевым индексом words.
# Две строки считаются похожими, если они состоят из одинаковых символов.
# Например, "abca"и "cba"похожи, поскольку оба состоят из символов 'a', 'b'и 'c'.
# Однако "abacba"и "bcfd"не похожи, поскольку состоят из разных персонажей.
# Возвращает количество пар (i, j)таких, что 0 <= i < j <= word.length - 1и две строки words[i]и words[j]похожи .


# Example 1:
# Input: words = ["aba","aabb","abcd","bac","aabc"]
# Output: 2
# Explanation: There are 2 pairs that satisfy the conditions:
# - i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
# - i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'.

# Example 2:
# Input: words = ["aabb","ab","ba"]
# Output: 3
# Explanation: There are 3 pairs that satisfy the conditions:
# - i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
# - i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
# - i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.

# Example 3:
# Input: words = ["nba","cba","dba"]
# Output: 0
# Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.

### Краткое условие:
# Надо найти количества пара в массиве words с одинаковыми буквами.

# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 0.
# 1) Проходимся циклом по диапазону длины массива words, (0 элемент массива)
# 1.1) Проходимся циклом по диапазону (i+1,длины массива words), (1 элемент массива)
# 1.1.1) Если словарь i set-ов равен словарю j set-ов, то увеличь значение переменной result на 1.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n^2)

words = ["aabb", "ab", "ba"]

def similarPairs(words):
    result = 0

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if set(words[i]) == set(words[j]): # тут мы убираем дубликаты из двух строк "aabb" => {"a","b"} и "ab" => {"a","b"}
                result += 1                     # Если они равны увеличисваем result на 1 !

    return result # 3

similarPairs(words)

assert similarPairs(words=["aba", "aabb", "abcd", "bac", "aabc"]) == 2
assert similarPairs(words=["aabb", "ab", "ba"]) == 3
assert similarPairs(words=["nba", "cba", "dba"]) == 0