### Условие задачи:
# Стробограмматическое число — это число, которое выглядит одинаково при повороте на 180 градусов (если смотреть на него вверх ногами).
# Напишите функцию для определения, является ли число стробограмматическим. Число представлено в виде строки.

# Example 1:
# Input:  num = "69"
# Output: true

# Example 2:
# Input:  num = "88"
# Output: true

# Example 3:
# Input:  num = "962"
# Output: false

### Краткое условие:
# Если число стробограмматическое, функция должна вернуть True, в противном случае — False.

# Алгоритм решение задачи:
# 0) Создаем словарь dict стробограмматическими числами, и задает левый и правый указатель.
# 1) Проходимся циклом ваилд пока левый указатель не пеерсечется с правым,
# 1.1) Если число где установлен правый указатель нет в словаре dict, то верни False.
# 1.2) Если число где установлен левый указатель не равно значениею ключа где установлен правый указатель, то верни False.
# 1.3) Иначе, двигаем левый и правый указатель на 1.
# 2) Вернуть True.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

num = "69"

def isStrobogrammatic(num):
    dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    left = 0
    right = len(num) - 1

    while left <= right:

        if num[right] not in dict:
            return False

        elif num[left] != dict[num[right]]:
            return False

        else:
            left += 1
            right -= 1

    return True

isStrobogrammatic(num)

assert isStrobogrammatic(num="69") == True
assert isStrobogrammatic(num="88") == True
assert isStrobogrammatic(num="962") == False


### Оригинал решение ####
#
# class Solution:
#   def isStrobogrammatic(self, num: str) -> bool:
#     rotated = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
#     l = 0
#     r = len(num) - 1
#
#     while l <= r:
#       if num[r] not in rotated:
#         return False
#       if num[l] != rotated[num[r]]:
#         return False
#       l += 1
#       r -= 1
#
#     return True