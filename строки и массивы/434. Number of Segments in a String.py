### Условие задачи:
# Учитывая строку s, верните количество сегментов в строке.
# Сегмент определяется как непрерывная последовательность символов, не содержащих пробелов.

# Example 1:
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

# Example 2:
# Input: s = "Hello"
# Output: 1

### Краткое условие:
# Надо вернуть колличество всех слова в строке s.

# Алгоритм решение задачи:
# 0) Запихиваем строку s в массив и возращаем длину этого массива !!!

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "Hello, my name is John"

def countSegments(s):
    return len(s.split())

countSegments(s)

assert countSegments(s="Hello, my name is John") == 5
assert countSegments(s="Hello") == 1