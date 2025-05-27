# ### Условие задачи:
# Вам дан целочисленный массив с индексом 0 nums и целевой элемент target.
# Целевой индекс i — это такой индекс , что nums[i] == target.
# Возвращает список целевых индексов nums после сортировки nums в неубывающем порядке.
# Если целевых индексов нет, верните пустой список. Возвращаемый список необходимо отсортировать по возрастанию.

# Example 1:
# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]

# Example 3:
# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]

                                ### Добавить в список !

### Краткое условие:
# Вернуть массив индексов чисел из массива nums которые соответствуют числу target.
# Если числа target нету в массиве nums, то вернуть пустой список.

###                                         С бинарым поиском
# Алгоритм решение задачи:
# 0) Сортируем массив nums по возрастанию,
# 0.1) Создаем: пустой массив result и переменную count со значением 0, и границы для бинарного поиска left+right.
# 1) Проходимся циклом ваилд пока left не станет меньше или равно right,
# 1.1) Создаем переменную mid для поиска середины.
# 1.2) Если число target меньше числа которого находится в середине массив nums, то уменьши правую границу на mid - 1.
# 1.3) Если число target БОЛЬШЕ числа которого находится в середине массив nums, то уменьши левую границу на mid + 1.
# 1.4) Если число которого находится в середине массив nums равно числу target,
# 1.4.1) то добавь индекс этого числа в массив result,
# 1.4.2) удали это число из массива nums, увеличь значение перевенной count на 1, сбрось диапазон бинарнго поиска.
# 2) Вернуть отсартированый массив result.

# Сложность:
# 1) памяти O(n log n)
# 2) времени O(n)

### Сложная задача !!!

nums = [1, 2, 5, 2, 3]
target = 3

def targetIndices(nums, target):
    nums.sort() # [1, 2, 2, 3, 5]
    result = []
    count = 0
    left = 0
    right = len(nums) - 1 # 4

    while left <= right:
        mid = (left + right) // 2

        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

        if nums[mid] == target:
            result.append(nums.index(nums[mid]) + count)
            nums.pop(mid)
            count += 1
            left = 0
            right = len(nums) - 1
    #               [3]
    return sorted(result) # [3]

targetIndices(nums, target)

assert targetIndices(nums=[1, 2, 5, 2, 3], target=2) == [1, 2]
assert targetIndices(nums=[1, 2, 5, 2, 3], target=3) == [3]
assert targetIndices(nums=[1, 2, 5, 2, 3], target=5) == [4]

###                                         Без бинарного поиска
# Алгоритм решение задачи:
# 0) Создать пустой массив стек
# 1) Отсортировать по возврастанию массив nums
# 2) Пройтись циклом по элементам массив nums
# 2.1) Если элемент массив nums совпадает с target, то добавь в массив стек номер элемента
# 2.2) Если НЕТ то, pass
# 3) Вернуть массив стек

# Сложность:
# 1) памяти O(n log n)
# 2) времени O(n)

# nums = [1,2,5,2,3]
# target = 3
#
# def targetIndices(nums,target):
#
#     stack=[]
#     nums.sort()
#
#     for i in range(len(nums)):
#         if i == target:
#             stack.appright(i)
#         else:
#             pass
#     return stack
#
# targetIndices(nums, target)