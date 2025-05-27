### Условие задачи:
# Дан массив положительных целых чисел nums, вернуть максимально возможную сумму возрастающего подмассива в nums.
# Подмассив определяется как непрерывная последовательность чисел в массиве.
# Подмассив является возрастающим, если для всех, где.
# Обратите внимание, что подмассив размера является возрастающим .[numsl, numsl+1, ..., numsr-1, numsr]il <= i < rnumsi  < numsi+11

# Example 1:
# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

# Example 2:
# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

# Example 3:
# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

### Краткое условие:
# Дан массив положительных целых чисел nums, вернуть максимально возможную сумму возрастающего подмассива в nums.

# Алгоритм решение задачи:
# 0) Создаем переменные result и sum со значением первого элемента массива nums.
# 1) Задаем левый и правый указатель.
# 2) Проходимся циклом ваилд пока right не дайдет до конца массив nums,
# 2.1) Если число где стаит левый указатель меньше числа где стаит правый указать,
# 2.1.1) То увеличь sum на значение правого указателя, и сдвиль левый и правый указатель на 1.
# 2.2) Если число где стаит левый указатель БОЛЬШЕ числа где стаит правый указать,
# 2.2.1) То sum равна числу где стаит правый указатель, и сдвиль левый на правый указатель, а правый указатель на 1.
# 2.3) result равен максимальному числу из result или sum.
# 3) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

nums = [10, 20, 30, 5, 10, 50]

def maxAscendingSum(nums):
    result = nums[0]
    sum = nums[0]

    left = 0
    right = 1

    while right < len(nums):
        if nums[left] < nums[right]:
            sum += nums[right]
            left += 1
            right += 1

        else:
            sum = nums[right]
            left = right
            right += 1

        result = max(result, sum)

    return result

maxAscendingSum(nums)

assert maxAscendingSum(nums=[10, 20, 30, 5, 10, 50]) == 65
assert maxAscendingSum(nums=[10, 20, 30, 40, 50]) == 150
assert maxAscendingSum(nums=[12, 17, 15, 13, 10, 11, 12]) == 33