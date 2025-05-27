### Условие задачи:
# Учитывая целочисленный массив hours, представляющий время в часах, вернуть целое число,
# обозначающее количество пар i, j где i < j и hours[i] + hours[j] образуют полный день.
# Полный день определяется как продолжительность времени, кратная 24 часам.
# Например, 1 день — это 24 часа, 2 дня — это 48 часов, 3 дня — это 72 часа и т. д.

# Example 1:
# Input: hours = [12,12,30,24,24]
# Output: 2
# Explanation:
# The pairs of indices that form a complete day are (0, 1) and (3, 4).

# Example 2:
# Input: hours = [72,48,24,3]
# Output: 3
# Explanation:
# The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).

### Краткое условие:
# Надо вернуть сколько раз можно собрать полноценный день из массива hours.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict и переменную result со значением 0.
# 1) Проходимся циклом по массиву hours,
# 1.1) Создаем переменную reminder со значением i % 24,
# 1.2) Создаем переменную count со значением (24 - reminder) % 24,
# 1.3) Если ключ count есть в словаре dict, то увеличь result на значение ключа count.
# 1.4) Если ключ reminder есть в словаре dict, то увечь значение ключа reminder на 1.
# 1.5) Если ключ reminder НЕТ в словаре dict, то добавь ключ reminder со значением 1 в словарь dict.
# 2) Верни переменную result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

hours = [12, 12, 30, 24, 24]

def countCompleteDayPairs(hours):
    dict = {}
    result = 0

    for i in hours:

        reminder = i % 24
        count = (24 - reminder) % 24

        if count in dict:
            result += dict[count]

        if reminder in dict:
            dict[reminder] += 1
        else:
            dict[reminder] = 1
    # {12: 2, 6: 1, 0: 2}
    return result # 2

countCompleteDayPairs(hours)

assert countCompleteDayPairs(hours=[12, 12, 30, 24, 24]) == 2
assert countCompleteDayPairs(hours=[72, 48, 24, 3]) == 3