### Условие задачи:
# Вам дан массив строк names и массив heights, состоящий из различных положительных целых чисел.
# Оба массива имеют длину n. Для каждого индекса i и names[i] обозначаем heights[i] имя и рост человека .ith
# Возврат names отсортирован в порядке убывания роста людей.

# Example 1:
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.

# Example 2:
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

### Краткое условие:
# Надо отсортировать записать туда Имена Людей из массива names и записать к ним массив с ростом heights,
# затем вывести имена людей по убыванию.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь map и пустой массив result.
# 1) Проходимся циклом по диапазону длины массива names,
# добавляем число из массива heights как ключ, а значение берем из массива heights.
# 2) Сортируем словарь по возрастанию ключей.
# 3) Проходимся циклом по значением словаря sortMap, добавляем их в массив result.
# 4) Вернуть перевенутый массив result.

# Сложность:
# 1) Время O(n log n)
# 2) Память O(n)

names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]

def sortPeople(names, heights):
    map = {}
    result = []

    for i in range(len(names)): # range(0, 3)
        map[heights[i]] = names[i]
    # map = {155: 'Alice', 185: 'Bob', 150: 'Bob'}
    sortMap = dict(sorted(map.items()))
    # sortMap = {150: 'Bob', 155: 'Alice', 185: 'Bob'}

    for j in sortMap.values():
        result.append(j)
    # ['Bob', 'Alice', 'Bob']
    return result[::-1]  # ['Bob', 'Alice', 'Bob'] # "[::-1] " защита от первого юнитеста !!!

sortPeople(names, heights)

assert sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]) == ["Mary", "Emma", "John"] # result[::-1]
assert sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]) == ["Bob", "Alice", "Bob"]