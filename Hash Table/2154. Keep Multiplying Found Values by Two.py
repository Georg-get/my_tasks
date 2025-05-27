### Условие задачи:
# Вам дан массив целых чисел nums. Вам также дано целое число original, которое является первым числом, которое нужно искать в nums.
# Затем вы выполняете следующие шаги:
# 1) Если original найдено в nums, умножьте его на два (т. е. установите original = 2 * original).
# 2) В противном случае остановите процесс.
# 3) Повторяйте этот процесс с новым номером, пока вы продолжаете находить его.
# Вернуть окончательное значение original.

# Example 1:
# Input: nums = [5,3,6,1,12], original = 3
# Output: 24
# Explanation:
# - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
# - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
# - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
# - 24 is not found in nums. Thus, 24 is returned.

# Example 2:
# Input: nums = [2,7,9], original = 4
# Output: 4
# Explanation:
# - 4 is not found in nums. Thus, 4 is returned.

### Краткое условие:
# Если число original нету в массив nums, вернуть original. Вернуть самое большое число из массива nums,
# которое делется на original и умножить его на два.

# Алгоритм решение задачи:
# 0) Преобразовываем массив nums в словарь с set.
# 1) Проходимся циклом по словарю nums, есть ли original в множестве чисел nums, и если есть, умножает его на 2.
# 2) Верни original

# Сложность:
# 1) Время O(log n)
# 2) Память O(n)

nums = [5, 3, 6, 1, 12]
original = 3

def findFinalValue(nums, original):
    nums = set(nums)  # {1, 3, 5, 6, 12}

    while original in nums:
        original *= 2

    return original  # 24

findFinalValue(nums, original)

assert findFinalValue(nums=[5, 3, 6, 1, 12], original=3) == 24
assert findFinalValue(nums=[2, 7, 9], original=4) == 4