### Условие задачи:
# Вам даны две строки s, t в которых каждый символ встречается не более одного раза s и t является перестановкой s.
# Разница перестановок между s и t определяется как сумма абсолютной разницы между индексом вхождения каждого символа в s
# и индексом вхождения того же символа в t.
# Возвращает разницу перестановок между s и t.

# Example 1:
# Input: s = "abc", t = "bac"
# Output: 2
# Explanation:
# For s = "abc" and t = "bac", the permutation difference of s and t is equal to the sum of:
# The absolute difference between the index of the occurrence of "a" in s and the index of the occurrence of "a" in t.
# The absolute difference between the index of the occurrence of "b" in s and the index of the occurrence of "b" in t.
# The absolute difference between the index of the occurrence of "c" in s and the index of the occurrence of "c" in t.
# That is, the permutation difference between s and t is equal to |0 - 1| + |2 - 2| + |1 - 0| = 2.

# Example 2:
# Input: s = "abcde", t = "edbac"
# Output: 12
# Explanation: The permutation difference between s and t is equal to |0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12.


### Краткое условие:
# Вернуть число которое показывает сколько раз надо поменять буквы в строках s и t, чтобы они стали равны между собой.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result со значением 0.
# 1) Проходимся циклом по диапазону от 0 до длины строки t,
# 1.1) Добавляем в словарь dict ключ букву из строки t со значением ее индекса в строке t.
# 2) Проходимсяц циклом по диапазону от 0 до длины строки s,
# 2.1) Увеличиваем переменную result на положительный результат j-значение ключа j.
# 3) Вернуть result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "abc"
t = "bac"

def findPermutationDifference(s, t):
    dict = {} # 0
    result = 0

    for i in range(len(t)):
        dict[t[i]] = i
    # {'b': 0, 'a': 1, 'c': 2} # цифры это индексы букв !!!
    for j in range(len(s)):
        result += abs(j - dict[s[j]]) # abs - метод который возращаент положительное число если число отрицательное
    # {'b': 0, 'a': 1, 'c': 2}
    return result # 2

findPermutationDifference(s, t)

assert findPermutationDifference(s="abc", t="bac") == 2
assert findPermutationDifference(s="abcde", t="edbac") == 12