### Условие задачи:
# У вас есть длинная клумба, в которой некоторые участки засажены, а некоторые нет.
# Однако цветы нельзя сажать на соседних участках.
# Дан целочисленный массив, flowerbed содержащий 0' и 1', где 0означает пустой, а 1 означает непустой,
# и целое число n, вернуть, можно true ли n посадить новые цветы в, flowerbed не нарушая правила отсутствия смежных цветов,
# и false в противном случае.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

### Краткое условие:
# вернуть, можно true ли n посадить новые цветы в, flowerbed не нарушая правила отсутствия смежных цветов,
# и false в противном случае.

# Полное объяснение решение задачи:
# 0) Задаем левый и правый указатель.
# 1) Проходимся циклом ваилд пока n больше 0 и right меньше длины массива flowerbed,
# 1.1) Если число где стаит правый указатель равно 1,
# 1.1.1) То n уменьши на (right - left - 2) // 2 и left равно right.
# 1.2) Двигаем right на 1.
# 2) Если равно 0 и right равна длине flowerbed,
# 2.1) То n уменьши на (right - left - 1) // 2.
# 3) Если n меньше или равно 0, то верни True.
# 4) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

flowerbed = [1, 0, 0, 0, 1]
n = 1

def canPlaceFlowers(flowerbed, n):
    left = -2
    right = 0

    while n > 0 and right < len(flowerbed):

        if flowerbed[right] == 1:
            n -= (right - left - 2) // 2
            left = right

        right += 1

    if flowerbed[-1] == 0 and right == len(flowerbed):
        n -= (right - left - 1) // 2

    if n <= 0:
        return True
    else:
        return False

canPlaceFlowers(flowerbed, n)

assert canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1) == True
assert canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2) == False