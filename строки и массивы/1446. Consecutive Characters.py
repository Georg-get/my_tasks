### Условие задачи:
# Мощность строки — это максимальная длина непустой подстроки, содержащей только один уникальный символ.
# Для заданной строки s верните степень числа s.

# Example 1:
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

# Example 2:
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

### Краткое условие:
# Надо вернуть длину подстроки повторяюшимя букв.

# Алгоритм решение задачи:
# 0) Создаем: левый и правый указатель, и переменные count и result со значением 0.
# 1) Проходимся циклом ваилд пока правый указатель не дойдет до конца строки s,
# 1.1) Если буква где установлен левый указатель не равна букве где установлен правый указатель,
# то left = right и увеличь right на 1 и count = 0.
# 1.2) Если буква где установлен левый указатель РАВНА букве где установлен правый указатель, то увеличь count и right на 1.
# 1.3) Если count больше result, то result = count.
# 2) Верни result + 1.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "leetcode"

def maxPower(s):
    left = 0
    right = 1
    count = 0
    result = 0

    while right < len(s):
        if s[left] != s[right]:
            left = right
            right += 1
            count = 0
        else:
            count += 1
            right += 1

        if count > result:
            result = count

    return result + 1

maxPower(s)

assert maxPower(s="leetcode") == 2
assert maxPower(s="abbcccddddeeeeedcba") == 5