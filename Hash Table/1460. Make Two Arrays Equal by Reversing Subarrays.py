### Условие задачи:
# Вам даны два целочисленных массива одинаковой длины target и arr.
# За один шаг вы можете выбрать любой непустой подмассив и arr перевернуть его. Разрешено делать любое количество шагов.
# Верните true, если можете сделать arr равным target или false иначе.

# Example 1:
# Input: target = [1,2,3,4], arr = [2,4,1,3]
# Output: true
# Explanation: You can follow the next steps to convert arr to target:
# 1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
# 2- Reverse subarray [4,2], arr becomes [1,2,4,3]
# 3- Reverse subarray [4,3], arr becomes [1,2,3,4]
# There are multiple ways to convert arr to target, this is not the only way to do so.

# Example 2:
# Input: target = [7], arr = [7]
# Output: true
# Explanation: arr is equal to target without any reverses.

# Example 3:
# Input: target = [3,7,9], arr = [3,7,11]
# Output: false
# Explanation: arr does not have value 9 and it can never be converted to target.

### Краткое условие:
# Вернуть true если все элементы двух массивов target и arr совпадают.
# Если есть элемент, который не совпадает вернуть false.

# Алгоритм решение задачи:
# 0) Создаем два пустых словаря targetDict и arrDict.
# 1) Проходимся циклом по массиву target,
# 1.1) Если ключ i есть в словаре targetDict, то увеличь значение ключа на 1.
# 1.2) Если ключ i НЕТу в словаре targetDict, то добавь ключ i со значением 1 в словарь targetDict.
# 2) Проходимся циклом по массиву arr,
# 2.1) Если ключ j есть в словаре arrDict, то увеличь значение ключа на 1.
# 2.2) Если ключ j НЕТу в словаре arrDict, то добавь ключ j со значением 1 в словарь arrDict.
# 3) Верни targetDict == arrDict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]

def canBeEqual(target, arr):
    targetDict = {}
    arrDict = {}

    for i in target:
        if i in targetDict:
            targetDict[i] += 1
        else:
            targetDict[i] = 1
    # {1: 1, 2: 1, 3: 1, 4: 1}
    for j in arr:
        if j in arrDict:
            arrDict[j] += 1
        else:
            arrDict[j] = 1
    # {2: 1, 4: 1, 1: 1, 3: 1}
    if targetDict == arrDict:
        return True
    else:
        return False
    # return targetDict == arrDict

canBeEqual(target, arr)

assert canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]) == True
assert canBeEqual(target=[7], arr=[7]) == True
assert canBeEqual(target=[3, 7, 9], arr=[3, 7, 11]) == False