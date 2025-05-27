### Условие задачи:
# Вам даны 2 целочисленных массива nums1 и nums2 длины n и m соответственно. Вам также дано положительное целое число k.
# Пара (i, j) называется хорошей , если nums1[i] делится на nums2[j] * k( 0 <= i <= n - 1, 0 <= j <= m - 1).
# Верните общее количество хороших пар.

# Example 1:
# Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1
# Output: 5
# Explanation:
# The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).

# Example 2:
# Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3
# Output: 2
# Explanation:
# The 2 good pairs are (3, 0) and (3, 1).

### Краткое условие:
# Верните общее количество хороших пар.

                                        ### Без хэша таблицы ###
# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 0.
# 1) Проходим циклом по массиву nums1,
# 1.1) Проходим циклом по массиву nums2,
# 1.1.1) Если i % (j * k) без остатка, то увеличь result на 1.
# 2) Верни result.

# Сложность:
# 1) Время O(n*m)
# 2) Память O(1)

nums1 = [1, 3, 4]
nums2 = [1, 3, 4]
k = 1

def numberOfPairs(nums1, nums2, k):
    result = 0

    for i in nums1:
        for j in nums2:
            if i % (j * k) == 0:
                result += 1

    return result

numberOfPairs(nums1, nums2, k)

assert numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1) == 5
assert numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3) == 2