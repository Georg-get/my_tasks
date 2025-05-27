### Условие задачи:
# Вам дана строка с индексом 0, s состоящая только из строчных английских букв, где каждая буква sвстречается ровно два раза .
# Вам также дан целочисленный массив длины с нулевым индексом .distance26
# Каждая буква алфавита пронумерована от 0до 25(т.е. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
# В строке с хорошим интервалом количество букв между двумя вхождениями буквы равно 0.
# Если буква не появляется , то ее можно игнорировать .ithdistance[i]ithsdistance[i]
# Верните true, если s это строка с хорошим интервалом , в противном случае верните false .

# Example 1:
# Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: true
# Explanation:
# - 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
# - 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
# - 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
# Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
# Return true because s is a well-spaced string.

# Example 2:
# Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: false
# Explanation:
# - 'a' appears at indices 0 and 1 so there are zero letters between them.
# Because distance[0] = 1, s is not a well-spaced string.

                                            ### Добавить в список !

### Краткое условие:
# Верните true, если s это строка с хорошим интервалом, в противном случае верните false.

# Алгоритм решение задачи:
# 0) Создать пустой словарь dict.
# 1) Проходимся циклом по диапазону длины строки s,
# 1.1) Если ключа i нету в словаре dict, то добавь ключ i со значением i+1
# 1.2) Если ключ i есть в словаре dict,
# 1.2.1) Если элемент из массива distance [юникод i - юникод "a"] не равен i - значение ключа i, вернуть False.
# 2) Вернуть True.

# Сложность:
# 1) Время O(n)
# 2) Память O(1) (n)

### Сложная задача !!!

s = "abaccb"
distance = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def checkDistances(s, distance):
    dict = {}

    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = i + 1
        else:
            if distance[ord(s[i]) - ord('a')] != i - dict[s[i]]: # Это условие проверяет,
                    # соответствует ли текущее расстояние до предыдущего вхождения буквы условию уникальности подстроки.
                # {'a': 1} - второй юнитест !!!
                return False # Верните false, если расстояние не совпадает
            else:
                pass
    # {'a': 1, 'b': 2, 'c': 4} - первый юнитест !!!
    return True # Возвращаем true, если все расстояния верны

checkDistances(s, distance)

assert checkDistances(s="abaccb",
                      distance=[1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
assert checkDistances(s="aa",
                      distance=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False