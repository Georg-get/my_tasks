### Условие задачи:
# Вам дан массив целых чисел с индексом 0 nums.
# Префикс nums[0..i] является последовательным, если для всех 1 <= j <= i, nums[j] = nums[j - 1] + 1.
# В частности, префикс, состоящий только из nums[0]is sequential.
# Возвращает наименьшее целое число, x отсутствующее в nums таком,
# которое x больше или равно сумме самого длинного последовательного префикса.

# Example 1:
# Input: nums = [1,2,3,2,5]
# Output: 6
# Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array,
# therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

# Example 2:
# Input: nums = [3,4,5,1,12,14,13]
# Output: 15
# Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not.
# Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

                                    ### Добавить в список !

### Краткое условие:
# Необходимо найти наименьшее целое число x,
# которое отсутствует в массиве и больше или равно сумме самого длинного последовательного префикса.

# Краткое объяснение решение задачи:
# 1. Создание множества: dictSet содержит уникальные элементы из nums.
# 2. Инициализация: result устанавливается на первый элемент массива, а count начинается с 1.
# 3. Суммирование последовательных чисел: В первом цикле код суммирует последовательные числа,
# начиная с первого элемента, пока они идут подряд.
# 4. Поиск отсутствующего числа: Во втором цикле код увеличивает result, пока оно присутствует в dictSet.
# 5. Возврат результата: возвращаем первое отсутствующее целое число.

# Полное объяснение решение задачи:
# 0) Создаем множество dictSet со значенеим массива nums, и переменную result со значением 1 элемента из массива nums, ё
# и переменную count со значенем до 1.
# 1) Проходимся циклом ваилд пока count не станет больше длины массива nums и nums[count] не станет равно nums[count - 1] + 1,
# 1.1) Увеличь значение переменную result на nums[count] и увеличь значение переменную count на 1.
# 2) Проходимся циклом ваилд пока result не будет в словаре dictSet, увеличь переменную result на 1.
# 3) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

                                ### Сложная задача !!!

nums = [1, 2, 3, 2, 5]

def missingInteger(nums):
    dictSet = set(nums)  # {1, 2, 3, 5}
    result = nums[0]  # 1
    count = 1

    while count < len(nums) and nums[count] == nums[count - 1] + 1:
        result += nums[count]
        count += 1
    # count = 3
    # result = 6
    while result in dictSet: # это для 2 и 3 юнитеста
        result += 1
    # 6
    return result  # 6

missingInteger(nums)

assert missingInteger(nums=[1, 2, 3, 2, 5]) == 6
assert missingInteger(nums=[3, 4, 5, 1, 12, 14, 13]) == 15
assert missingInteger(nums=[29, 30, 31, 32, 33, 34, 35, 36, 37]) == 297  # этот юнитест защищает от код нижнего !!!
# Доп юнитесты для проверки некоторых условий:
assert missingInteger(nums=[0, 0, 0, 0]) == 1 # Случай с нулями


### Не проходят все юнитесты 111 / 616 testcases passed !!!
# Сложность:
# 1) Время O(n log n)
# 2) Память O(n)

# nums = [1, 2, 3, 2, 5]
#
# def missingInteger(nums):
#     sortedNums = sorted(nums) # [1, 2, 2, 3, 5]
#     return sortedNums[-1] + 1 # 6
#
# missingInteger(nums)