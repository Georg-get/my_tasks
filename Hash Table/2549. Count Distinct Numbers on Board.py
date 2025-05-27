### Условие задачи:
# Вам дано целое положительное число n, которое изначально находится на доске.
# Каждый день, в течение нескольких дней, вы выполняете следующую процедуру:109
# Для каждого числа x, представленного на доске, найдите все 1 <= i <= n такие числа, что x % i == 1.
# Затем разместите эти числа на доске.
# Возвращает количество различных целых чисел, присутствующих на доске по истечении дней .109
# Примечание:
# Как только число будет помещено на доску, оно останется на ней до конца.
# % означает операцию по модулю. Например,  14 % 3есть 2.

# Example 1:
# Input: n = 5
# Output: 4
# Explanation: Initially, 5 is present on the board.
# The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1.
# After that day, 3 will be added to the board because 4 % 3 == 1.
# At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation:
# Since 3 % 2 == 1, 2 will be added to the board.
# After a billion days, the only two distinct numbers on the board are 2 and 3.

### Краткое условие:
# Возвращает количество различных целых чисел, присутствующих на доске по истечении дней

###                         С хэшом таблицы
# Алгоритм решение задачи:
# 0) Создаем два пустых множества board и remaining, добавляем в board переменную n, и создаем переменную day со значением 1.
# 1) Проходимся циклом по диапазону от 2 до n, добавлям i в множество remaining.
# 2) Проходимся циклом ваилд пока длина remaining не станет больше 0 и пока переменная day не станет меньше 10 в степени 9,
# 2.1) Создаем пустое множество removing.
# 2.2) Проходимся циклом по словарю remaining,
# 2.2.1) Проходимся циклом по словарю board, если k делется на j без остатка , то добавь j в board и removing, выйди из цикла.
# 2.3) Проходимся циклом по словарю removing, удаляем в словаре remaining ключ i.
# 2.4) Увеличиваем переменную day на 1.
# 3) Верни длину словаря board.

# Сложность:
# 1) Время O(n)
# 2) Память O(n^2)

n = 5

def distinctIntegers(n):
    board = set()
    remaining = set()
    board.add(n)
    day = 1

    for i in range(2, n):
        remaining.add(i)

    while len(remaining) > 0 and day < pow(10, 9):
        removing = set()

        for j in remaining:
            for k in board:
                if k % j == 1:
                    board.add(j)
                    removing.add(j)
                    break

        for num in removing:
            remaining.remove(num)
        day += 1

    return len(board)

distinctIntegers(n)

assert distinctIntegers(n=5) == 4
assert distinctIntegers(n=3) == 2

###                         Без хэша таблицы
# Алгоритм решение задачи:
# 0) Если n не равна 1, то верни n -1.
# 1) Если n равен 1, то верни 1.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

# n = 5
#
# def distinctIntegers(n):
#     if n != 1:
#         return n - 1
#     else:
#         return 1
#
# distinctIntegers(n)