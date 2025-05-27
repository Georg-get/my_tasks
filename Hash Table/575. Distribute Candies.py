### Условие задачи:
# У Алисы есть n конфеты, причем конфеты имеют тип . Алиса заметила, что начала прибавлять в весе, поэтому обратилась к врачу.ithcandyType[i]
# Доктор посоветовал Алисе есть только n / 2те конфеты, которые у нее есть ( n всегда ровные). Алисе очень нравятся конфеты,
# и она хочет съесть максимальное количество разных конфет, при этом следуя советам врача.
# Учитывая целочисленный массив candyTypeдлины n, верните максимальное количество различных типов конфет, которые она может съесть, если будет есть толькоn / 2 их .

# Example 1:
# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

# Example 2:
# Input: candyType = [1,1,2,3]
# Output: 2
# Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.

# Example 3:
# Input: candyType = [6,6,6,6]
# Output: 1
# Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.


### Краткое условие:
# Учитывая целочисленный массив candyType длины n, верните максимальное количество различных типов конфет,
# которые она может съесть, если будет есть только n / 2 их.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь с set(candyType).
# 1) Возвращаем минимальное занчение от длины словаря dict и длины массива candyType деленая на 2.


# Сложность:
# 1) Время O(n)
# 2) Память O(n) (k)

candyType = [1, 1, 2, 2, 3, 3]

def distributeCandies(candyType):
    dict = set(candyType)  # {1, 2, 3}
    # минимальное из 3 и 6/2=3
    return min(len(dict), len(candyType) // 2)  # 3

distributeCandies(candyType)

assert distributeCandies(candyType=[1, 1, 2, 2, 3, 3]) == 3
assert distributeCandies(candyType=[1, 1, 2, 3]) == 2
assert distributeCandies(candyType=[6, 6, 6, 6]) == 1