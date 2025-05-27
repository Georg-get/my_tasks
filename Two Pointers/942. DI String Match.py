### Условие задачи:
# Перестановку целых perm чисел n + 1всех целых чисел в диапазоне [0, n]можно представить в виде строки s длины n, где:
# s[i] == 'I'если perm[i] < perm[i + 1]и
# s[i] == 'D'если perm[i] > perm[i + 1].
# Учитывая строку s, восстановите перестановку perm и верните ее.
# Если существует несколько допустимых перестановок, верните любую из них.

# Example 1:
# Input: s = "IDID"
# Output: [0,4,1,3,2]

# Example 2:
# Input: s = "III"
# Output: [0,1,2,3]

# Example 3:
# Input: s = "DDI"
# Output: [3,2,0,1]

### Краткое условие:
# Учитывая строку s, восстановите перестановку perm и верните ее.

# Алгоритм решение задачи:
# 0) Создаем переменные: left со значением 0 и right со значением длины строки s, и пустой массив result.
# 1) Проходимся циклом по строке s,
# 1.1) Если i равна I, то добавь в массив result значнеие left и увеличь значение left на 1.
# 1.2) Если i НЕ равна I, то добавь в массив result значнеие right и уменьши значение right на 1.
# 2) Верни массив result + массива left.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "IDID"

def diStringMatch(s):
    left = 0
    right = len(s)
    result = []

    for i in s:
        if i == "I":
            result.append(left)
            left += 1
        else:
            result.append(right)
            right -= 1
    # [0, 4, 1, 3] + [2]
    return result + [left]

diStringMatch(s)

assert diStringMatch(s="IDID") == [0, 4, 1, 3, 2]
assert diStringMatch(s="III") == [0, 1, 2, 3]
assert diStringMatch(s="DDI") == [3, 2, 0, 1]