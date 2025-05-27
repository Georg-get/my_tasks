### Условие задачи:
# Вам даны два целочисленных массива nums и divisors.
# Показатель делимости — divisors[i] это количество индексов j, nums[j] делящихся на divisors[i].
# Верните целое число divisors[i] с максимальной оценкой делимости.
# Если несколько целых чисел имеют максимальную оценку, верните наименьшее из них.

# Example 1:
# Input: nums = [2,9,15,50], divisors = [5,3,7,2]
# Output: 2
# Explanation:
# The divisibility score of divisors[0] is 2 since nums[2] and nums[3] are divisible by 5.
# The divisibility score of divisors[1] is 2 since nums[1] and nums[2] are divisible by 3.
# The divisibility score of divisors[2] is 0 since none of the numbers in nums is divisible by 7.
# The divisibility score of divisors[3] is 2 since nums[0] and nums[3] are divisible by 2.
# As divisors[0], divisors[1], and divisors[3] have the same divisibility score, we return the smaller one which is divisors[3].

# Example 2:
# Input: nums = [4,7,9,3,9], divisors = [5,2,3]
# Output: 3
# Explanation:
# The divisibility score of divisors[0] is 0 since none of numbers in nums is divisible by 5.
# The divisibility score of divisors[1] is 1 since only nums[0] is divisible by 2.
# The divisibility score of divisors[2] is 3 since nums[2], nums[3] and nums[4] are divisible by 3.

# Example 3:
# Input: nums = [20,14,21,10], divisors = [10,16,20]
# Output: 10
# Explanation:
# The divisibility score of divisors[0] is 2 since nums[0] and nums[3] are divisible by 10.
# The divisibility score of divisors[1] is 0 since none of the numbers in nums is divisible by 16.
# The divisibility score of divisors[2] is 1 since nums[0] is divisible by 20.

### Краткое условие:
# Верните целое число divisors[i] с максимальной оценкой делимости.

# Алгоритм решение задачи:
# 0) Создаем пустой массив result и отсортировываем массив divisors по возрастанию.
# 1) Проходимся циклом по массиву divisors,
# 1.1) Создаем число count со значением 0,
# 1.2) Проходимся циклом по массиву nums,
# 1.2.1) Если j делится без остатка на i, то увеличь count на 1.
# 1.3) В массив result добавляем count.
# 2) Возращаем элемент из массива divisors с индексом максивальным из массива result.

# Сложность:
# 1) Время O(n*m)
# 2) Память O(n)

nums = [2, 9, 15, 50]
divisors = [5, 3, 7, 2]

def maxDivScore(nums, divisors):
    result = []
    divisors.sort() # [2, 3, 5, 7]

    for i in divisors:
        count = 0

        for j in nums:
            if j % i == 0:
                count += 1

        result.append(count)

    return divisors[result.index(max(result))] # возращаем элемент из массива divisors с индексом максивальным из массива result

maxDivScore(nums, divisors)

assert maxDivScore(nums=[2, 9, 15, 50], divisors=[5, 3, 7, 2]) == 2
assert maxDivScore(nums=[4, 7, 9, 3, 9], divisors=[5, 2, 3]) == 3
assert maxDivScore(nums=[20, 14, 21, 10], divisors=[10, 16, 20]) == 10