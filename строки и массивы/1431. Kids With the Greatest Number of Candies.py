### Условие задачи:
# Есть n дети с конфетами. Вам дан массив целых чисел candies, где каждое число candies[i] представляет количество конфет у ребенка,
# и целое число, обозначающее количество дополнительных конфет, которые есть у вас.ithextraCandies
# Возвращает логический массив result длины n, где result[i]— true если после раздачи ребенку всех,
# у него будет наибольшее количество конфет среди всех детей, или в противном случае .ithextraCandies false
# Обратите внимание, что наибольшее количество конфет могут получить несколько детей.

# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

# Example 2:
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false]
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

# Example 3:
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]

### Краткое условие:
# Вернуть колличество чисел из массива candies которые в сумме i + extraCandies >= max(candies).

# Алгоритм решение задачи:
# 0) Создаем пустой массив result,
# 1) Проходимся циклом по массиву candies,
# 1.1) Если i + extraCandies больше или равна максивальному элементу в массиве candies, то в массив result добавь True.
# 1.1) Если i + extraCandies НЕ больше или НЕ равна максивальному элементу в массиве candies, то в массив result добавь False.
# 2) Верни массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

candies = [2, 3, 5, 1, 3]
extraCandies = 3

def kidsWithCandies(candies, extraCandies):
    result = []

    for i in candies:

        if i + extraCandies >= max(candies): # max(candies) = 5
            result.append(True)
        else:
            result.append(False)

    return result

kidsWithCandies(candies, extraCandies)

assert kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3) == [True, True, True, False, True]
assert kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1) == [True, False, False, False, False]
assert kidsWithCandies(candies=[12, 1, 12], extraCandies=10) == [True, False, True]