### Условие задачи:
# Дана двоичная строка s, возвращает результат,
# true если самый длинный непрерывный сегмент 1's строго длиннее самого длинного непрерывного сегмента 0's in's,
# или возвращает false в противном случае.
# Например, в самый длинный непрерывный сегмент s имеет длину, а самый длинный непрерывный сегмент s имеет длину .
# s = "110100010"1203
# Обратите внимание, что если символов нет, то считается, что 0самый длинный непрерывный сегмент из них имеет длину.
# То же самое применимо, если нет 's.001

# Example 1:
# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.

# Example 2:
# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.

# Example 3:
# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.

### Краткое условие:
# Дана двоичная строка s, возвращает результат,
# true если самый длинный непрерывный сегмент 1's строго длиннее самого длинного непрерывного сегмента 0's in's,
# или возвращает false в противном случае.

# Алгоритм решение задачи:
# 0) Создаем пустые переменные: bestOne, bestZero, currentOne, currentZero.
# 1) Проходимся циклом по строке s,
# 1.1) Если i равно 1, то currentZero = 0 и увеличиваем currentOne на 1.
# 1.2) Если i Не равно 1, то currentOne = 0 и увеличиваем currentZero на 1.
# 2) Если bestOne больше чем bestZero, то верни True.
# 3) Если bestOne НЕ больше чем bestZero, то верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "1101"

def checkZeroOnes(s):
    # current переводится как текущий
    bestOne = 0 # 1 # 2 # 3
    bestZero = 0 # 1
    currentOne = 0
    currentZero = 0

    for i in s:
        if i == "1":
            currentZero = 0
            currentOne += 1
        else:
            currentZero += 1
            currentOne = 0

        bestOne = max(bestOne, currentOne)
        bestZero = max(bestZero, currentZero)

    if bestOne > bestZero:
        return True
    else:
        return False

checkZeroOnes(s)

assert checkZeroOnes(s="1101") == True
assert checkZeroOnes(s="111000") == False
assert checkZeroOnes(s="110100010") == False