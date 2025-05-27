### Условие задачи:
# Учитывая целочисленный массив nums и целое число val, удалите все вхождения valin nums -place . Порядок элементов может быть изменен.
# Затем верните количество элементов, в nums которых не равны val.
# Учитывайте количество элементов, в nums которых не равны val, k чтобы их приняли, вам необходимо сделать следующее:
# Измените массив nums так, чтобы первые k элементы nums содержали элементы, не равные val. Остальные элементы numsне важны, как и размер nums.
# Возвращаться k.
# Пользовательский судья:
# Судья проверит ваше решение с помощью следующего кода:
# int[] nums = [...]; // Входной массив
# интервал вал = ...; // Значение для удаления
# int[] ожидаемые числа = [...]; // Ожидаемый ответ правильной длины.
# // Он отсортирован без значений, равных val.
# int k = RemoveElement(nums, val); // Вызывает вашу реализацию
# утверждать k == ожидаемые числа.длина;
# сортировка (числа, 0, к); // Сортируем первые k элементов числа nums
# for (int i = 0; i <actualLength; i++) {
#     утверждать nums[i] == ожидаемыеNums[i];
# }
# Если все утверждения пройдены, ваше решение будет принято.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

### Краткое условие:
# Надо удалить число val в массиве nums и вернуть его длину.

# Алгоритм решение задачи:
# 0) Создаем переменные: left со значнием 0 и right со значнием длины массива nums.
# 1) Проходимся циклома ваилд пока left не станет меньше right,
# 1.1) Если число на котором установлен левый указатель из массива nums не равно переменной val, то увеличь значение переменной left на 1.
# 1.2) Если число на котором установлен левый указатель из массива nums РАВЕН переменной val,
# 1.2.1) То число на котором установлен левый указатель из массива nums равно число на котором установлен правый указатель из массива nums -1.
# 2) Вернуть число right.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

def removeElement(nums, val):
    if len(nums) < 0 or val == 0:
        return 0

    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]  # меняем местами
            right -= 1
        else:
            left += 1
    # [0, 1, 4, 0, 3, 2, 2, 2]
    return left  # 5

removeElement(nums, val)

assert removeElement(nums=[3, 2, 2, 3], val=3) == 2
assert removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2) == 5
assert removeElement(nums=[], val=3) == 0
assert removeElement(nums=[1, 2], val=0) == 0