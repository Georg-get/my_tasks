### Условие задачи:
# Учитывая целое число x, верните true if x палиндром, и false иначе.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

### Краткое условие:
# Надо проверить число на палиндром, если число палиндром то вернуть true.
# Если число не палиндром или число отрицательное, то вернуть false.

# Алгоритм решение задачи:
# 0) Если число х меньше 0, то верни False.
# 1) Переобразуем число х в строку.
# 2) Задаем левый и правый указатель.
# 3) Проходимся циклом ваилд пока left не станет меньше right,
# 3.1) Если число где стаит левый указатель не равен числу где стаит правый указатель, то верни False.
# 3.2) Увеличиваем значение left на 1 и уменьшаем значение right на 1.
# 4) Вернуть True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

x = 121

def isPalindrome(x):
    if x < 0:
        return False

    x = str(x)
    left = 0
    right = len(x) - 1

    while left < right:
        if x[left] != x[right]: # если числа где установлены левый и правый указатель не равны верни False
            return False
        left += 1
        right -= 1

    return True

isPalindrome(x)

assert isPalindrome(x=121) == True
assert isPalindrome(x=-121) == False
assert isPalindrome(x=10) == False
assert isPalindrome(x=0) == False