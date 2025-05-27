### Условие задачи:
# Учитывая целочисленный массив nums, возвращайте значение true, если какое-либо значение встречается в массиве хотя бы дважды
# false, и возвращайте значение, если каждый элемент различен.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

### Краткое условие:
# Если в массиве nums есть число, которое встречается дважды, то вернуть true, если все числа разные вернуть false.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по массиву nums,
# 1.1) Если ключ i есть в словаре dict, то верни True.
# 1.2) Если ключ i НЕТу в словаре dict, то добавь ключ i со значением 1 в словарь dict.
# 2) Верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

def containsDuplicate(nums):
    dict = {}

    for i in nums:
        if i in dict:
            # {1: 1}
            return True
        else:
            dict[i] = 1

    return False

containsDuplicate(nums)

assert containsDuplicate(s="egg", t="add") == True
assert containsDuplicate(s="foo", t="bar") == False
assert containsDuplicate(s="paper", t="title") == True