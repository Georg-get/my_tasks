### Условие задачи:
# Вам дана строка word. Буква называется специальной, если она написана как в нижнем, так и в верхнем регистре word.
# Возвращает количество специальных букв в формате . word

# Example 1:
# Input: word = "aaAbcBC"
# Output: 3
# Explanation:
# The special characters in word are 'a', 'b', and 'c'.

# Example 2:
# Input: word = "abc"
# Output: 0
# Explanation:
# No character in word appears in uppercase.

# Example 3:
# Input: word = "abBCab"
# Output: 1
# Explanation:
# The only special character in word is 'b'.

### Краткое условие:
# Надо вернуть колличество из одной и тойже буквы которые имеют пару из большой и маленькой буквы.

# Алгоритм решение задачи:
# 0) Создаем множество dictSet со значением строки word и пустое множество emptyDict, и переменную result со значением 0.
# 1) Проходимся циклом по множеству dictSet,
# 1.1) Делаем из i переменные lower где она будет маленькой буквой и upper где i будет большой буквой.
# 1.2) Если ключи lower и upper есть в словаре dictSet,
# 1.2.1) Если ключей lower и upper НЕТУ в словаре emptyDict, то увелись переменную result на 1 и добавь lower и upper в словарь emptyDict.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

word = "abBCab"

def numberOfSpecialChars(word):
    dictSet = set(word) # {'b', 'C', 'B', 'a'}
    emptyDict = set() # {}
    result = 0

    for i in dictSet:
        lower = i.lower() # b
        upper = i.upper() # B
        if lower in dictSet and upper in dictSet:
            if lower not in emptyDict and upper not in emptyDict:
                result += 1
                emptyDict.add(lower)
                emptyDict.add(upper)
    # emptyDict = {'B', 'b'}
    return result # 1

numberOfSpecialChars(word)

assert numberOfSpecialChars(word="aaAbcBC") == 3
assert numberOfSpecialChars(word="abc") == 0
assert numberOfSpecialChars(word="abBCab") == 1