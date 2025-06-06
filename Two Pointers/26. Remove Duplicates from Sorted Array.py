### Условие задачи:
# Учитывая целочисленный массив, nums отсортированный в порядке неубывания , удалите дубликаты на месте так,
# чтобы каждый уникальный элемент появлялся только один раз . Относительный порядок элементов должен оставаться неизменным .
# Затем верните количество уникальных элементов в nums .
# Учитывая количество уникальных элементов , чтобы nums быть k принятым, вам необходимо сделать следующее:
# Измените массив nums так, чтобы первые k элементы numsсодержали уникальные элементы в том порядке,
# в котором они присутствовали numsизначально. Остальные элементы numsне важны, как и размер nums.
# Возвращаться k.
# Пользовательский судья:
# Судья проверит ваше решение с помощью следующего кода:
# int[] nums = [...]; // Входной массив
# int[] ожидаемые числа = [...]; // Ожидаемый ответ правильной длины
# int k = RemoveDuulates (nums); // Вызывает вашу реализацию
# утверждать k == ожидаемые числа.длина;
# for (int i = 0; i < k; i++) {
#     утверждать nums[i] == ожидаемыеNums[i];
# }
# Если все утверждения пройдены, ваше решение будет принято.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

### Краткое условие:
# Отправить все дубликаты чисел в конец в массиве nums и вернуть длину массива nums без дубликатов чисел.

# Алгоритм решение задачи:
# 0) Создаем переменные: left со значнием 0 и right со значнием 1.
# 1) Проходимся циклом ваилд пока left не станет меньше или ранво right и right больше длины массива nums.
# 1.1) Если число на котором установлен левый указатель равно числу на котором установлен правый указатель, то увеличь значение переменной right на 1.
# 1.2) Если число на котором установлен левый указатель НЕ равно числу на котором установлен правый указатель,
# 1.2.1) Число на котором установлен левый указатель равно числу +1 на котором установлен правый указатель, то увеличь значение переменной left на 1.
# 2) Вернуть переменную left +1.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [1, 1, 2]

def removeDuplicates(nums):
    left = 0
    right = left + 1

    while right < len(nums):
        if nums[left] != nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1] # отправляем дубликаты в конец
            left += 1
        right += 1
    # nums = [1, 2, 1] - первый кейс        # nums == [0, 1, 2, 3, 4, 0, 2, 1, 3, 1] - второй кейс
    return left + 1 # 1 + 1 - первый кейс   # 4 +1  - второй кейс

removeDuplicates(nums)

assert removeDuplicates(nums=[1, 1, 2]) == 2
assert removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5