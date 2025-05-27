### Условие задачи:
# Вам дан массив строго возрастающих целых чисел с нулевым индексом и положительное целое число.
# Тройка является арифметической тройкой, если выполняются следующие условия:nums diff (i, j, k) i < j < k,
# nums[j] - nums[i] == diff, и nums[k] - nums[j] == diff. Возвращает количество уникальных арифметических троек.

# Example 1:
# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.

# Example 2:
# Input: nums = [4,5,6,7,8,9], diff = 2
# Output: 2
# Explanation:
# (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

### Краткое условие:
# Надо вернуть индексы тех чисел, которые вычитания их будет равна diff.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result = 0.
# 1) Пройтись циклом по диапазону длине массива nums (от 0 до длины массива nums).
# 1.1) Добавляем каждый элемент из массива nums в словарь dict, как ключ со значением ключ + diff.
# 2) Проходимся циклом по словарю dict.
# 2.1) Если значение совпадает с ключом в словаре dict.
# 2.1.1) Если значение + diff совпадает с каким нибудь ключом в словаре dict, то увеличь значение переменой result на 1.
# 2.1.2) Если НЕТ то pass.
# 3) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [0, 1, 4, 6, 7, 10]
diff = 3

def arithmeticTriplets(nums, diff):
    dict = {}
    result = 0

    for i in range(len(nums)):
        dict[nums[i]] = nums[i] + diff
    # {0: 3, 1: 4, 4: 7, 6: 9, 7: 10, 10: 13}

    for j in dict:
        if dict[j] in dict:  # {1:4, 4: 7, 7: 10}
            if dict[j + diff] in dict:  # 4 + 3 = 7 , { 4: 7 } = YES  #7 + 3 = 10 , { 10: 13} = YES
                result += 1
            else:  # 10 + 3 = 13 , ключа под номером 13 Нету = NO
                pass

    return result # 2

arithmeticTriplets(nums, diff)

assert arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3) == 2
assert arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2) == 2