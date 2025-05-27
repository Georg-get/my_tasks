### Условие задачи:
# Учитывая двумерный целочисленный массив nums, где nums[i] является непустым массивом различных положительных целых чисел,
# верните список целых чисел, которые присутствуют в каждом массиве, nums отсортированном в порядке возрастания.

# Example 1:
# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation:
# The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

# Example 2:
# Input: nums = [[1,2,3],[4,5,6]]
# Output: []
# Explanation:
# There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

### Краткое условие:
# Надо вернуть массив в котором будут числа которые больше всего повторяються из матрицы nums.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и пустой массив result.
# 1) Если длина матрицы равна 1, то отсортируй 0 элемент матрицы и верни 0 элемент.
# 2) Если длина матрицы НЕ РАВНА 1,
# 2.1) Создай: пустой словарь dict и пустой массив result, и переменную bigVale со значением 0,
# 2.2) Проходимся циклом по матрице nums,
# 2.2.1) Проходимся циклом по элементам массива из матрицы nums,
# 2.2.1.1) Если ключ j есть в словаре dict, то увеличь значение ключа j на 1.
# 2.2.1.2) Если ключ j НЕТу в словаре dict, то добавь ключ j со значением 1.
# 2.2.2) Проходимя циклом по словарю dict и ищем там самое большое значение,
# если мы находим самое большое значение то добавляеи его в переменную bigVale.
# 2.2.3) Если bigVale == 1 , то вернуть массив result.
# 2.2.4) Если bigVale НЕ РАВНО 1,
# 2.2.4.1) Пройтись циклом по словарю dict и добавить только те ключи у которых значение равно bigVale.
# 2.2.4.2) Вернуть отсортированый массив result.

# Сложность:
# 1) Время O(n^2)
# 2) Память O(n)

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]

def intersection(nums):
    if len(nums) == 1:
        nums[0].sort()

        return nums[0]
    else:
        dict = {}
        result = []
        bigVale = 0

        for i in nums:
            for j in i:
                if j in dict:
                    dict[j] += 1
                else:
                    dict[j] = 1
        # {3: 3, 1: 2, 2: 2, 4: 3, 5: 2, 6: 1}
        for value in dict.values():
            if value > bigVale:
                bigVale = value
        # 3
        if bigVale == 1:
            return result
        else:
            for key, value in dict.items():
                if value == bigVale:
                    result.append(key)
            # [3,4]
            return sorted(result) # [3,4]

intersection(nums)