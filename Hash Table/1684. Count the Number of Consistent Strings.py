### Условие задачи:
# Вам дана строка allowed, состоящая из различных символов и массива строк words.
# Строка является согласованной, если все символы строки присутствуют в ней allowed.
# Возвращает количество согласованных строк в массиве words.

# Example 1:
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# Example 2:
# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.

# Example 3:
# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

                                ### Добавить в список !
### Краткое условие:
# Посчитать количество раз сколько повтаряются буквы из строки allowed в массиве words.

# Алгоритм решение задачи:
# 0) Создаем словарь hashSetAllowed в котором будет храниться уникальные ключи со значением строки allowed и переменную result=0.
# 1) Проходим по массиву words (берем элемент (слова) из массива).
# 1.1) Создаем переменную isConsistanct со значением True.
# 1.2) Проходимся по буквам слова из массива words.
# 1.2.1) Если такой буквы НЕТУ в словаре hashSetAllowed, то isConsistanct = False и пропускаем это слова.
# 1.3) Если переменная isConsistanct = True, то увеличь значение переменной result на 1.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n) (n * m)
# 2) Память O(n)

### Сложная задача !!!

allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]

def countConsistentStrings(allowed, words):
    result = 0
    hashSetAllowed = set(allowed)  # {'a', 'b'}

    for i in words:
        isConsistanct = True
        for j in i:
            if j not in hashSetAllowed:
                isConsistanct = False
                break

        if isConsistanct == True:
            result += 1
    # {'b', 'a'}
    return result # 2

countConsistentStrings(allowed, words)

assert countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]) == 2
assert countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7
assert countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == 4