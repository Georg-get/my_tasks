### Условие задачи:
# Вам дан целочисленный массив с нулевым индексом nums. Вам также дано целое число key, которое присутствует в nums.
# Для каждого уникального целого числа target в подсчитайте количество раз, которое nums следует сразу за появлением в .
# Другими словами, подсчитайте количество индексов таких, что:target key nums i
# 0 <= i <= nums.length - 2,
# nums[i] == key и,
# nums[i + 1] == target.
# Верните с targetмаксимальным счетчиком . _ Тестовые случаи будут созданы таким образом, чтобы targetмаксимальное количество было уникальным.

# Example 1:
# Input: nums = [1,100,200,1,100], key = 1
# Output: 100
# Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
# No other integers follow an occurrence of key, so we return 100.

# Example 2:
# Input: nums = [2,2,2,2,3], key = 2
# Output: 2
# Explanation: For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key.
# For target = 3, there is only one occurrence at index 4 which follows an occurrence of key.
# target = 2 has the maximum number of occurrences following an occurrence of key, so we return 2.

                                            ### Добавить в список !

# Алгоритм решение задачи:
# 0) Создаем словарь numsDict, c ключами из чисел массива nums значениями 0.
# 1) Проходимся циклом по словарю numsDict,
# 1.1) Проходимся циклом по диапазону (от 9 до длины массива nums -1),
# 1.1.1) Если элемент массива nums i равен key и элемент массива nums i+1 равен target, то увеличь ключ target на 1.
# 2) Верни ключ с самым большим значением в словаре numsDict.

# Сложность:
# 1) Время O(n^2) (n)
# 2) Память O(n)

### Сложная задача !!!

nums = [1, 100, 200, 1, 100]
key = 1

def mostFrequent(nums, key):
    numsDict = dict.fromkeys(nums, 0)
    # {1: 0, 100: 0, 200: 0}
    for target in numsDict:
        for i in range(0, len(nums) - 1):
            if (nums[i] == key and nums[i + 1] == target):
                numsDict[target] += 1
    # {1: 0, 100: 2, 200: 0}
    return max(numsDict, key=numsDict.get)

mostFrequent(nums, key)

assert mostFrequent(nums=[1, 100, 200, 1, 100], key=1) == 100
assert mostFrequent(nums=[2, 2, 2, 2, 3], key=2) == 2