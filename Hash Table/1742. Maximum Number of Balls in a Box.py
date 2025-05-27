### Условие задачи:
# Вы работаете на фабрике по производству шаров, где у вас есть n шары с номерами от low Limit до high Limit включительно (т. е. n == highLimit - lowLimit + 1)
# и бесконечное количество коробок с номерами от 1 до infinity.
# Ваша задача на этой фабрике — поместить каждый шарик в коробку с номером, равным сумме цифр номера шарика.
# Например, номер шара 321 будет указан в номере коробки 3 + 2 + 1 = 6, а номер шара 10 будет указан в номере коробки 1 + 0 = 1.
# Учитывая два целых числа low Limit и highLimit, верните количество шаров в ящике с наибольшим количеством шаров.

# Example 1:
# Input: lowLimit = 1, highLimit = 10
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
# Box 1 has the most number of balls with 2 balls.

# Example 2:
# Input: lowLimit = 5, highLimit = 15
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
# Boxes 5 and 6 have the most number of balls with 2 balls in each.

# Example 3:
# Input: lowLimit = 19, highLimit = 28
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
# Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
# Box 10 has the most number of balls with 2 balls.

                                    ### Добавить в список !
### Краткое условие:
# Учитывая два целых числа lowLimit и highLimit, верните количество шаров в ящике с наибольшим количеством шаров.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по диапазону (lowLimit, highLimit + 1),
# 1.1) Создаем переменную sum,
# 1.2) Проходимся циклом while, если i > или = 1, то выходим из циклом while,
# 1.2.1) Увеличиваем переменную sum на i деленная на 10,
# 1.2.2) Присваеваем i значение i делем на 10.
# 1.3) Если ключа sum НЕТу в словаре dict, то добавь ключ sum со значением 1.
# 1.4) Если ключ sum есть в словаре dict, то увеличь его значение на 1.
# 2) Верни максимальный значение из словаря dict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n) (1)

### Сложная задача !!!

lowLimit = 1
highLimit = 10

def countBalls(lowLimit, highLimit):
    dict = {}

    for i in range(lowLimit, highLimit + 1): # range(1, 11)
        sum = 0

        while i >= 1:
            sum += i % 10
            i //= 10

        if sum not in dict:
            dict[sum] = 1
        else:
            dict[sum] += 1
    # {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    return max(dict.values())  # 2

countBalls(lowLimit, highLimit)

assert countBalls(lowLimit=1, highLimit=10) == 2
assert countBalls(lowLimit=5, highLimit=15) == 2
assert countBalls(lowLimit=19, highLimit=28) == 2