### Условие задачи:
# Вам дан массив с нулевым индексом , состоящий из неотрицательных целых чисел.nums n
# Вам необходимо применить n - 1операции к этому массиву, где в операции ( с индексом 0 )
# вы примените к элементу следующее :ithithnums
# Если nums[i] == nums[i + 1], то умножить nums[i] на 2 и установить nums[i + 1]на 0. В противном случае вы пропустите эту операцию.
# После выполнения всех операций сдвиньте все 0 символы в конец массива.
# Например, массив [1,0,2,0,0,1]после сдвига всех его 0элементов в конец имеет вид [1,2,1,0,0,0].
# Верните полученный массив .
# Обратите внимание , что операции применяются последовательно , а не все сразу.

# Example 1:
# Input: nums = [1,2,2,1,1,0]
# Output: [1,4,2,0,0,0]
# Explanation: We do the following operations:
# - i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
# - i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change nums[2] to 0. The array becomes [1,4,0,1,1,0].
# - i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
# - i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change nums[4] to 0. The array becomes [1,4,0,2,0,0].
# - i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change nums[5] to 0. The array becomes [1,4,0,2,0,0].
# After that, we shift the 0's to the right, which gives the array [1,4,2,0,0,0].

# Example 2:
# Input: nums = [0,1]
# Output: [1,0]
# Explanation: No operation can be applied, we just shift the 0 to the right.

### Краткое условие:
# После выполнения всех операций сдвиньте все 0символы в конец массива.
# Например, массив [1,0,2,0,0,1] после сдвига всех его 0элементов в конец имеет вид [1,2,1,0,0,0].
# Верните полученный массив.

# Алгоритм решение задачи:
# 0) Проходимся циклом по диапазону длины массива nums,
# 0.1) Если первое и второе число равно, то умнож первое число на 2 а второе число замени на 0.
# 1) Создаем два указателя.
# 2) Проходимся циклом ваилд пока правый указатель не дойдет до конца строки,
# 2.1) Если число на котором установлен левый указатель равно 0,
# 2.1.1) Если число на котором установлен правый указатель НЕ равно 0,
# 2.1.1.1) Поменяй местами числа где установлен левый и правый указатель, и сдвинь левый и правый указатель на 1.
# 2.1.2) Если число на котором установлен правый указатель равно 0, то сдвинь правый указатель на 1.
# 2.2) Если число на котором установлен левый указатель НЕ равно 0, сдвинь левый и правый указатель на 1.
# 3) Верни массив nums.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [1, 2, 2, 1, 1, 0]

def applyOperations(nums):

    for i in range(len(nums) - 1): # range(0, 5)
        if nums[i] == nums[i + 1]:
            nums[i] = 2 * nums[i]
            nums[i + 1] = 0
    # [1, 4, 0, 2, 0, 0]
    left = 0
    right = 1

    while right < len(nums): # пока правый указатель не дойдет до конца строки
        if nums[left] == 0:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1
        else:
            left += 1
            right += 1
                #        l  r  поменяли местами
    return nums # [1, 4, 2, 0, 0, 0]

applyOperations(nums)

assert applyOperations(nums=[1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]
assert applyOperations(nums=[0, 1]) == [1, 0]