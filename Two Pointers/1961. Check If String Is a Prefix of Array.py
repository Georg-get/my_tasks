### Условие задачи:
# Учитывая строку sи массив строк words, определите, s является ли строка префиксомwords.
# Строка s — это префиксная строка if words, s которую можно создать путем объединения первых
# k строк wordsдля некоторого положительного значения k , не превышающего words.length.
# Возвращает true if s — префиксную строку words или false иначе.

# Example 1:
# Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
# Output: true
# Explanation:
# s can be made by concatenating "i", "love", and "leetcode" together.

# Example 2:
# Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
# Output: false
# Explanation:
# It is impossible to make s using a prefix of arr.

                                    ### Добавить в список !


### Краткое условие:
# Надо проверить можно ли собрать из массива words строку s и вернуть true если получилось, иначе false.

# Алгоритм решение задачи:
# 0) Создаем переменную left со значением 0.
# 1) Проходимся циклом по массиву words,
# 1.1) Создаем переменную right со значением 0,
# 1.2) Проходимся циклом ваилд пока left не станет больше длина строки s и right больше длина строки i и левый указатель в строке s равен строке i правому указателю,
# 1.2.1) Увеличь переменную left на 1 и уменьше переменную right на 1.
# 1.3) Если left равен длине строки s и right равно длине строки, то верни True.
# 1.4) Если right не равно длине строки, то верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

s = "iloveleetcode"
words = ["i", "love", "leetcode", "apples"]

def isPrefixString(s, words):
    left = 0

    for i in words:
        right = 0

        while left < len(s) and right < len(i) and s[left] == i[right]:
            left += 1
            right += 1

        if left == len(s) and right == len(i):
            return True

        if right != len(i): # Нужно для второго юнитеста !!!
            return False

isPrefixString(s, words)

assert isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"]) == True
assert isPrefixString(s="iloveleetcode", words=["apples", "i", "love", "leetcode"]) == False # Он !!!