### Условие задачи:
# We are playing the Guess Game. The game is as follefts:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is righter or lefter than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is righter than the number I picked (i.e. num > pick).
# 1: Your guess is lefter than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.


# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1

### Краткое условие:
# Пик годы !
# Узнать при помощи API что это пик горы. Вернуть номер индекса, который соответствует pick в n.

# Алгоритм решение задачи:
# 0) Написать функцию бинарного поиска, которая ищет число pick в диапазоне числа n.
# 1) Если n = pick, верни return n
# 1.1) Если n != pick, то вызови функцию бинарного поиска.

# Сложность:
# 1) памяти O(n log n)
# 2) времени O(1)

n = 10
pick = 6

def guessNumber(n, pick):
    # def guess(mid,pick):
    #      return mid - pick
    left = 0
    right = n # 10

    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)

        if result == 0:
            return mid
        elif result < 0:
            right = mid - 1
        else:
            left = mid + 1

    return -1

guessNumber(n, pick)

assert guessNumber(n=10, pick=6) == 6
assert guessNumber(n=1, pick=1) == 1
assert guessNumber(n=2, pick=1) == 1