### Условие задачи:
# Учитывая два целочисленных массива arr1 и arr2 и целое число d, верните значение расстояния между двумя массивами .
# Значение расстояния определяется как количество элементов, arr1[i] в которых нет ни одного элемента,
# arr2[j] где |arr1[i]-arr2[j]| <= d.

# Example 1:
# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation:
# For arr1[0]=4 we have:
# |4-10|=6 > d=2
# |4-9|=5 > d=2
# |4-1|=3 > d=2
# |4-8|=4 > d=2
# For arr1[1]=5 we have:
# |5-10|=5 > d=2
# |5-9|=4 > d=2
# |5-1|=4 > d=2
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2

# Example 2:
# Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# Output: 2

# Example 3:
# Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1

### Краткое условие:
# Верните значение расстояния между двумя массивами arr1 и arr2.

# Алгоритм решение задачи:
# 0) Сортируем массив arr2 по возрастанию и создаем переменную distance со значением длины массива arr1.
# 1) Проходимся циклом по массиву arr1,
# 1.1) Создаем переменную left со значением 0,
# 1.2) Создаем переменную right со значением длины массива arr2-1,
# 1.3) Проходимся циклом ваилд пока left не станет меньше или равна right,
# 1.3.1) Находим mid (середину),
# 1.3.2) Если абсолютное (без знако значение) значение (i - arr2[mid]) больше или равно d, то уменьши переменную distance на 1 и выйди из цикла.
# 1.3.3) Если arr2[mid] больше чем i, то присвой переменной right значяение mid - 1.
# 1.3.4) Если arr2[mid] меньше чем i, то присвой переменной left значяение mid + 1.
# 2) Верни переменную distance.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2

def findTheDistanceValue(arr1, arr2, d):
    arr2.sort() # [1, 8, 9, 10]
    distance = len(arr1) # 3

    for i in arr1:
        
        left = 0
        right = len(arr2) - 1 # 3

        while left <= right:
            mid = (left + right) // 2

            if abs(i - arr2[mid]) <= d:
                distance -= 1
                break
            elif arr2[mid] > i:
                right = mid - 1
            elif arr2[mid] < i:
                left = mid + 1
    #       2
    return distance

findTheDistanceValue(arr1, arr2, d)

assert findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2) == 2
assert findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3) == 2
assert findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6) == 1