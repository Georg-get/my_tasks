### Условие задачи:
# Вам дан целочисленный массив с нулевым индексом nums. За одну операцию можно сделать следующее:
# Выберите два целых числа, в nums которых они равны.
# Удалите оба целых числа из nums, образуя пару.
# Операцию повторяют nums максимально возможное количество раз.
# Возвращает целочисленный массив с нулевым индексом answer размера 2 где answer[0] — количество сформированных пар и
# answer[1] — количество оставшихся целых чисел nums после выполнения операции максимально возможное количество раз.

# Example 1:
# Input: nums = [1,3,2,1,3,2,2]
# Output: [3,1]
# Explanation:
# Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
# Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
# Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
# No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.

# Example 2:
# Input: nums = [1,1]
# Output: [1,0]
# Explanation: Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [].
# No more pairs can be formed. A total of 1 pair has been formed, and there are 0 numbers leftover in nums.

# Example 3:
# Input: nums = [0]
# Output: [0,1]
# Explanation: No pairs can be formed, and there is 1 number leftover in nums.

### Краткое условие:
# Надо вернуть массив в котором будет два числа: перове число количестов одинаковых пар из массива nums,
# второе число количество чисел которое не смогло найти себе пару.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result со значением 0.
# 1) Пройтись циклом по массив nums,
# 1.1) Если i есть в словре dict, то увеличь значение переменной result на 1 и удали этот ключ со значением из словаря dict.
# 1.2) Если i НЕТу в словре dict, то добавь i как ключ со значением 1 в словарь dict.
# 2) Верни переменную result и длину словаря dict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 3, 2, 1, 3, 2, 2]

def numberOfPairs(nums):
    dict = {}
    result = 0

    for i in nums:
        if i in dict:
            result += 1
            dict.pop(i)
        else:
            dict[i] = 1
    # {2: 1}
    #         3   ,     1
    return [result, len(dict.keys())]

numberOfPairs(nums)

assert numberOfPairs(nums=[1, 3, 2, 1, 3, 2, 2]) == [3, 1]
assert numberOfPairs(nums=[1, 1]) == [1, 0]
assert numberOfPairs(nums=[0]) == [0, 1]