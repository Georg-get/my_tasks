### Условие задачи:
# Вам дан массив целых чисел nums. Рассмотрим следующую операцию:
# Удалим первые два элемента nums и определим оценку операции как сумму этих двух элементов.
# Эту операцию можно выполнять до тех пор, пока nums не будет содержать менее двух элементов.
# Кроме того, во всех операциях должен быть достигнут одинаковый счет.
# Верните максимальное количество операций, которые вы можете выполнить.

# Example 1:
# Input: nums = [3,2,1,4,5]
# Output: 2
# Explanation:
# We can perform the first operation with the score 3 + 2 = 5. After this operation, nums = [1,4,5].
# We can perform the second operation as its score is 4 + 1 = 5, the same as the previous operation. After this operation, nums = [5].
# As there are fewer than two elements, we can't perform more operations.

# Example 2:
# Input: nums = [1,5,3,3,4,1,3,2,2,3]
# Output: 2
# Explanation:
# We can perform the first operation with the score 1 + 5 = 6. After this operation, nums = [3,3,4,1,3,2,2,3].
# We can perform the second operation as its score is 3 + 3 = 6, the same as the previous operation. After this operation, nums = [4,1,3,2,2,3].
# We cannot perform the next operation as its score is 4 + 1 = 5, which is different from the previous scores.

# Example 3:
# Input: nums = [5,3]
# Output: 1

### Краткое условие:
# Верните максимальное количество операций, которые вы можете выполнить.

# Полное объяснение решение задачи:
# 0) Создаем переменую result со значение 1 и answer со значением 0 элемент + 1 элемент.
# 1) Проходимся циклом по идексам от 2 до длины массива nums - 1,
# 1.1) Если первый элемент + второй элемент равны answer, то увеличь result на 1.
# 1.2) Иначе, выйди из цикла.
# 2) Верни result

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [3, 2, 1, 4, 5]

def maxOperations(nums):
    result = 1
    answer = nums[0] + nums[1]  # 3+2 = 5

    for i in range(2, len(nums) - 1, 2):  # range(2, 4, 2)
        if nums[i] + nums[i + 1] == answer:
            result += 1
        else: # 4 юнитест !!!
            break

    return result  # 2

maxOperations(nums)

assert maxOperations(nums=[3, 2, 1, 4, 5]) == 2
assert maxOperations(nums=[1, 5, 3, 3, 4, 1, 3, 2, 2, 3]) == 2
assert maxOperations(nums=[5, 3]) == 1
assert maxOperations(nums=[2, 2, 3, 2, 4, 2, 3, 3, 1, 3]) == 1 # 4 юнитест !!!