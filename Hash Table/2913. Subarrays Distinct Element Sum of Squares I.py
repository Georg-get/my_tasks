### Условие задачи:
# Вам дан целочисленный массив с нулевым индексом nums.
# Количество различных подмассивов nums определяется как:
# Позвольте nums[i..j]быть подмассивом, nums состоящим из всех индексов от i до j такого, что 0 <= i <= j < nums.length.
# Тогда количество различных значений в nums[i..j]называется числом различных значений nums[i..j].
# Возвращает сумму квадратов различных значений всех подмассивов nums.
# Подмассив — это непрерывная непустая последовательность элементов массива.

# Example 1:
# Input: nums = [1,2,1]
# Output: 15
# Explanation: Six possible subarrays are:
# [1]: 1 distinct value
# [2]: 1 distinct value
# [1]: 1 distinct value
# [1,2]: 2 distinct values
# [2,1]: 2 distinct values
# [1,2,1]: 2 distinct values
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

# Example 2:
# Input: nums = [1,1]
# Output: 3
# Explanation: Three possible subarrays are:
# [1]: 1 distinct value
# [1]: 1 distinct value
# [1,1]: 1 distinct value
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.

                                            ### Добавить в список !

### Краткое условие:
# Надо разбить массив nums на подмассивы и взять значение этих подмассивов возвести в квадрат
# и сложить (= Сумма квадратов чисел различных чисел во всех подмассивах).
# Вернуть сумму квадратов чисел различных чисел во всех подмассивах

# Алгоритм решение задачи:
# 0) Создать переменные: lengthArryNums = длина массива nums и result = 0 для подсчета суммы.
# 1) Пройтись циклом по диапазону размера массива nums (от 0 до 3).
# 1.1) Создать словарь setDict со значением set-ом, для убирание дублей.
# 1.2) Пройтись циклом по диапазону от i до размера массива nums (от i до 3).
# 1.2.1) Добавить в словарь setDict ключ со значением j
# 1.2.2) Увеличиваем значение переменной result на длину словаря setDict в квадраете.
# 2) Возвращаем значение переменной result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

nums = [1, 2, 1]

def sumCounts(nums):
    lengthArryNums = len(nums)
    result = 0

    for i in range(lengthArryNums):
        setDict = set()

        for j in range(i, lengthArryNums):
            setDict.add(nums[j])
            result += len(setDict) ** 2

    return result

sumCounts(nums)

assert sumCounts(nums=[1, 2, 1]) == 15
assert sumCounts(nums=[1, 1]) == 3