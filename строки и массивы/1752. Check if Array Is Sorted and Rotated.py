### Условие задачи:
# Учитывая массив nums, вернуть, true если массив был изначально отсортирован в неубывающем порядке,
# а затем повернут на некоторое количество позиций (включая ноль). В противном случае вернуть false.
# В исходном массиве могут быть дубликаты .
# Примечание: Массив, A повернутый по x позициям,
# приводит к массиву B той же длины, такой что A[i] == B[(i+x) % A.length], где %— операция по модулю.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

# Example 2:
# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.

# Example 3:
# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

### Краткое условие:
# Учитывая массив nums, вернуть, true если массив был изначально отсортирован в неубывающем порядке,
# а затем повернут на некоторое количество позиций (включая ноль).

# Алгоритм решение задачи:
# 0) Создаем переменную count со значением 0.
# 1) Проходимся циклом по диапазону от 0 до длины массива nums,
# 1.1) Если nums[i] > числа которое следуюшие деленое на длину массива, то увеличь count на 1.
# 2) Если count равно или меньше 1, то верни True.
# 2) Иначе, то верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [3, 4, 5, 1, 2]

def check(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] > nums[(i + 1) % len(nums)]:
            count += 1

    if count <= 1:
        return True
    else:
        return False

check(nums)

assert check(nums=[3, 4, 5, 1, 2]) == True
assert check(nums=[2, 1, 3, 4]) == False
assert check(nums=[1, 2, 3]) == True