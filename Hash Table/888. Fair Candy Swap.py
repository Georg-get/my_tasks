### Условие задачи:
# У Алисы и Боба разное общее количество конфет. Вам даны два целочисленных массива aliceSizes,
# bobSizes где aliceSizes[i]- количество конфет в коробке конфет, которая есть у Алисы,
# и количество конфет в коробке конфет, которая есть у Боба.ithbobSizes[j]jth
# Поскольку они друзья, они хотели бы обменять по одной коробке конфет каждый,
# чтобы после обмена у них обоих было одинаковое общее количество конфет.
# Общее количество конфет, имеющихся у человека, равно сумме количества конфет в каждой имеющейся у него коробке.
# Возвращает целочисленный массив n answer, где answer[0]— количество конфет в коробке, которую должна обменять Алиса,
# и answer[1]— количество конфет в коробке, которую должен обменять Боб .
# Если ответов несколько, вы можете вернуть любой из них. Гарантируется, что существует хотя бы один ответ.

# Example 1:
# Input: aliceSizes = [1,1], bobSizes = [2,2]
# Output: [1,2]

# Example 2:
# Input: aliceSizes = [1,2], bobSizes = [2,3]
# Output: [1,2]

# Example 3:
# Input: aliceSizes = [2], bobSizes = [1,3]
# Output: [2,3]

### Краткое условие:
# Вернуть массив чисел поравну, если не получется вернуть массив 0 0.

# Алгоритм решение задачи:
# 0) Создаем словарь set с aliceSizes.
# 1) Создаем переменую targetDiff со значением (сумма всех элементов массива bobSizes - сумма всех элементов массива aliceSizes)деленая на 2.
# 2) Проходимся циклом по массиву bobSizes,
# 2.1) Если i - targetDiff есть в словаре aliceSet, то вернуть массив [ i - targetDiff , i].
# 3) Вернуть массив 0,0.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

aliceSizes = [1, 1]
bobSizes = [2, 2]

def fairCandySwap(aliceSizes, bobSizes):
    aliceSet = set(aliceSizes)  # {1}
    targetDiff = (sum(bobSizes) - sum(aliceSizes)) // 2  # (4-2)/2=1

    for i in bobSizes:
        if i - targetDiff in aliceSet:  # 2 - 1 in {1}
            return [i - targetDiff, i]  # [1, 2]

    return [0, 0]

fairCandySwap(aliceSizes, bobSizes)

assert fairCandySwap(aliceSizes=[1, 1], bobSizes=[2, 2]) == [1, 2]
assert fairCandySwap(aliceSizes=[1, 2], bobSizes=[2, 3]) == [1, 2]
assert fairCandySwap(aliceSizes=[2], bobSizes=[1, 3]) == [2, 3]