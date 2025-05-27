### Условие задачи:
# Вам дан массив nums положительных целых чисел и целое число k.
# За одну операцию вы можете удалить последний элемент массива и добавить его в свою коллекцию.
# Возвращает минимальное количество операций, необходимых для сбора элементов 1, 2, ..., k .

# Example 1:
# Input: nums = [3,1,5,4,2], k = 2
# Output: 4
# Explanation: After 4 operations, we collect elements 2, 4, 5, and 1, in this order. Our collection contains elements 1 and 2. Hence, the answer is 4.

# Example 2:
# Input: nums = [3,1,5,4,2], k = 5
# Output: 5
# Explanation: After 5 operations, we collect elements 2, 4, 5, 1, and 3, in this order. Our collection contains elements 1 through 5. Hence, the answer is 5.

# Example 3:
# Input: nums = [3,2,5,3,1], k = 3
# Output: 4
# Explanation: After 4 operations, we collect elements 1, 3, 5, and 2, in this order. Our collection contains elements 1 through 3. Hence, the answer is 4.

                                                ### Добавить в список !

### Краткое условие:
# Возвращает минимальное количество операций, необходимых для сбора элементов 1, 2, ..., k .

# Алгоритм решение задачи:
# 0) Создаем словарь dict со значением set(диапазон от 1 до k+1) и переменную result со значением 0.
# 1) Проходимся циклом по словарю dict, создаем переменную number со зачением последненго числа из массива nums.
# 1.1) Если number есть в словаре dict, то удали number из словаря dict.
# 2) Увеличь значение переменной result на 1.
# 3) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

### Сложная задача !!!

nums = [3, 1, 5, 4, 2]
k = 2

def minOperations(nums, k):
    dict = set(range(1, k + 1))  # {1, 2}
    result = 0

    while dict:
        number = nums.pop()
        # {1, 2}
        if number in dict:
            dict.remove(number)
        result += 1

    return result # 4

minOperations(nums, k)

assert minOperations(nums=[3, 1, 5, 4, 2], k=2) == 4
assert minOperations(nums=[3, 1, 5, 4, 2], k=5) == 5
assert minOperations(nums=[3, 2, 5, 3, 1], k=3) == 4