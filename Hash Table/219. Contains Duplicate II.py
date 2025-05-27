### Условие задачи:
# Учитывая целочисленный массив nums и целое число k, возвратите, true если есть два различных индекса i и j в массиве такие,
# что nums[i] == nums[j] и abs(i - j) <= k .

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

### Краткое условие:
# Верните true, если существуют два различных индекса i и j в массиве, такие что nums[i] == nums[j] и |i - j| <= k.
# В противном случае верните false.

# Краткое объяснение решение задачи:
# 1. Создается пустой словарь dict.
# 2. Проверяем каждого элемента массива nums:
#    - Если элемент уже есть в словаре и разница между текущим индексом и индексом, хранящимся в словаре, меньше или равна k, то возвращем True.
#    - Если нет, текущий индекс элемента добавляется в словарь.
# 3. Если таких дубликатов не найдено, функция возвращает False.


# Полное объяснение решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по диапазону длины массива nums,
# 1.1) Если nums[i] есть в словаре dict и значение ключа i - i меньше либо равно k, то верни True.
# 1.2) Если nums[i] НЕТу в словаре dict и значение ключа i - i меньше либо равно k, то добавь ключ i со значением i в словарь dict.
# 2) Верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 2, 3, 1]
k = 3

def containsNearbyDuplicate(nums, k):
    dict = {}

    for i in range(len(nums)):
        if nums[i] in dict and abs(dict[nums[i]] - i) <= k:  # [1 c индексом 3]
            # abs - возрашает положилеьные числа  a = - 5  abs(a) = 5
            # {1: 0, 2: 1, 3: 2}
            return True
        else:
            dict[nums[i]] = i

    return False

containsNearbyDuplicate(nums, k)

assert containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3) == True
assert containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1) == True
assert containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2) == False
# Доп юнитесты для проверки некоторых условий:
assert containsNearbyDuplicate(nums=[1, 2, 3, 4], k=2) == False  # Нет дубликатов
assert containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1) == True  # Дубликаты вне диапазона
assert containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3],
                               k=2) == False  # Дубликаты с большим k # (дубликаты 1 и 2 находятся слишком далеко друг от друга).
assert containsNearbyDuplicate(nums=[], k=0) == False  # Пустой массив
assert containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3, 1], k=3) == True  # Проверка на больших числах