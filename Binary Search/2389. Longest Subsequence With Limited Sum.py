### Условие задачи:
# Вам дан целочисленный массив nums длины n и целочисленный массив queries длины m.
# Возвращает массив answer длиной m где answer[i]— максимальный размер подпоследовательности,
# из которой можно взять nums такую, что сумма ее элементов меньше или равна queries[i].
# Подпоследовательность — это массив, который можно получить из другого массива путем удаления некоторых элементов или
# их отсутствия без изменения порядка остальных элементов.

# Example 1:
# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

# Example 2:
# Input: nums = [2,3,4,5], queries = [1]
# Output: [0]
# Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

### Краткое условие:
# Найти числа из массива nums которые будут в сумме давать число из массива queries и записать колличество чисел в массив result.
# Вернуть массив result с количеством чисел.

# Алгоритм решение задачи:
# 0) Создаем функцию бинарного поиска которая принимает массив и число, затем возращает число.
# 1) Сортируем массив nums по возрастанию.
# 2) Создаем массив firstNumberFromNumsArray со значением массива с первым элементом массива nums.
# 3) Создаем пустой массив result.
# 4) Проходимся циклом по массиву nums от 1 элемента до последнего,
# 4.1) Добавляем массив firstNumberFromNumsArray число из массива firstNumberFromNumsArray + i
# 5) Проходимся циклом по массиву queries, добавляем массиву result значение которое возрасщает функция бинарного поиска.
# 6) Вернуть массив result.

# Сложность:
# 1) памяти O(n)
# 2) времени O(n log n)

nums = [4, 5, 2, 1]
queries = [3, 10, 21]

def answerQueries(nums, queries):
    def binarySearch(firstNumberFromNumsArray, j):
        left = 0
        right = len(firstNumberFromNumsArray) - 1

        while left <= right:
            mid = (left + right) // 2

            if firstNumberFromNumsArray[mid] <= j:
                left = mid + 1
            else:
                right = mid - 1

        return left

    nums.sort()  # [1, 2, 4, 5]
    firstNumberFromNumsArray = [nums[0]]  # [1]
    result = []
    for i in nums[1:]:  # [2, 4, 5]
        firstNumberFromNumsArray.append(firstNumberFromNumsArray[-1] + i)
    # [1, 3, 7, 12]
    for j in queries:
        # 3   | 10     | 21
        result.append(binarySearch(firstNumberFromNumsArray, j))
        # [2] | [2, 3] | [2, 3, 4]
    return result  # [2, 3, 4]

answerQueries(nums, queries)

assert answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]) == [2, 3, 4]
assert answerQueries(nums=[2, 3, 4, 5], queries=[1]) == [0]