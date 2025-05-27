### Условие задачи:
# Вам дана строка, s состоящая только из символов '0'и '1'. За одну операцию можно изменить любую '0'на '1'или наоборот.
# Строка называется чередующейся, если никакие два соседних символа не равны.
# Например, строка "010"является чередующейся, а строка "0100"— нет.
# Верните минимальное количество операций, необходимых для создания s чередующихся.

# Example 1:
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.

# Example 2:
# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.

# Example 3:
# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".

### Краткое условие:
# Верните минимальное количество операций, необходимых для создания s чередующихся.

# Алгоритм решение задачи:
# 0) Создаем переменные lenSringS со значением длины строки s и firstSymbol со значением первого символа из строки s,
# и count со значением 0.
# 1) Проходимся циклом по диапазону от 0 до lenSringS,
# 1.1) Если индекс i % 2 равно 0 и элемени i не равен firstSymbol, или индекс i % 2 равно 1 и элемени i равен firstSymbol,
# 1.1.1) Увеличиваем count на 1.
# 2) Вернуть минимальное число из count или lenSringS - count.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "0100"

def minOperations(s):
    lenSringS = len(s) # 4
    firstSymbol = s[0] # 0
    count = 0

    for i in range(lenSringS):
        if i % 2 == 0 and s[i] != firstSymbol or i % 2 == 1 and s[i] == firstSymbol:
            count += 1

    return min(count, lenSringS - count)

minOperations(s)

assert minOperations(s="0100") == 1
assert minOperations(s="10") == 0
assert minOperations(s="1111") == 2