### Условие задачи:
# Вам дан целочисленный массив с индексом 0 nums, размер 3которого позволяет сформировать стороны треугольника.
# Треугольник называется равносторонним, если все его стороны имеют одинаковую длину.
# Треугольник называется равнобедренным, если у него ровно две стороны одинаковой длины.
# Треугольник называется разносторонним, если все его стороны имеют разную длину.
# Возвращает строку, представляющую тип треугольника, который может быть сформирован или, "none" если он не может
# быть сформирован, то он не может быть сформирован.

# Example 1:
# Input: nums = [3,3,3]
# Output: "equilateral"
# Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.

# Example 2:
# Input: nums = [3,4,5]
# Output: "scalene"
# Explanation:
# nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
# nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
# nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3.
# Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
# As all the sides are of different lengths, it will form a scalene triangle.

### Краткое условие:
# Возвращает строку, представляющую тип треугольника, который может быть сформирован.

# Полное объяснение решение задачи:
# 0) Создаем массив result, со строками "none", "equilateral", "isosceles", "scalene".
# 1) Сортируем массив nums.
# 2) Возврашаем элемент массива result который равен len(set(nums)) * (nums[2] < nums[0] + nums[1]).

# Сложность:
# 1) Время O(1)
# 2) Память O(1)

nums = [8, 4, 2]

def triangleType(nums):
    result = ["none", "equilateral", "isosceles", "scalene"]
    nums.sort()  # [2, 4, 8]
    #           3                 # (8   <       2 + 4 = 6) = False
    # 3 умножаем на 0 , потому что False это 0 в математике = 0
    return result[len(set(nums)) * (nums[2] < nums[0] + nums[1])]  # none

triangleType(nums)

assert triangleType(nums=[3, 3, 3]) == "equilateral"
assert triangleType(nums=[3, 4, 5]) == "scalene"
assert triangleType(nums=[8, 4, 2]) == "none"
assert triangleType(nums=[9, 4, 9]) == "isosceles"