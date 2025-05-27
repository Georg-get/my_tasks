### Условие задачи:
# Учитывая два массива строк list1и list2, найдите общие строки с наименьшей суммой индексов .
# Общая строка — это строка, которая встречается как в файлах, так list1и в файлах list2.
# Общая строка с наименьшей суммой индексов — это такая общая строка, которая, если она появляется в ,
# list1[i] должна list2[j] иметь i + j минимальное значение среди всех других общих строк .
# Возвращает все общие строки с наименьшей суммой индексов . Верните ответ в любом порядке .

# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".

# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

# Example 3:
# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".

### Краткое условие:
# Надо найти слова, которые совпадают в двух массивах: list1 и list2, и сумма индексов, которых будет самая минимальная.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result, и массив с не повторяюшимся элементами двух массивов list1 и list2.
# 1) Проходимся циклом по массиву allList,
# добавляем ключ i со значением номера индекса из массива list1 + номера индекса из массива list2 в словарь dict.
# 2) Создаем переменную minIndex со значением минимального значения в словаре dict.
# 3) Проходимся циклом по словарю dict,
# 3.1) Если значение ключа j равно переменной minIndex, то добавь j в массив result.
# 4) Вернуть массив result.

# Сложность:
# 1) Время O(n) (m + n)
# 2) Память O(n) (m + n)

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]

def findRestaurant(list1, list2):
    dict = {}
    result = []
    allList = list(set(list1) & set(list2))  # ['Burger King', 'Shogun', 'Tapioca Express', 'KFC']

    for i in allList:
        dict[i] = list1.index(i) + list2.index(i)
    # {'Burger King': 3, 'KFC': 3, 'Tapioca Express': 3, 'Shogun': 3}
    minIndex = min(dict.values())  # 3

    for j in dict:
        if dict[j] == minIndex:
            result.append(j)

    return result  # ['Burger King', 'Tapioca Express', 'KFC', 'Shogun']

findRestaurant(list1, list2)
assert findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                      list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ["Shogun"]
assert findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                      list2=["KFC", "Shogun", "Burger King"]) == ["Shogun"]
assert findRestaurant(list1=["happy", "sad", "good"], list2=["sad", "happy", "good"]) == ["sad", "happy"]