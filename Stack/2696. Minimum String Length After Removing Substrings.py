### Условие задачи:
# Вам дана строка s, состоящая только из заглавных английских букв.
# К этой строке можно применить несколько операций, где за одну операцию можно удалить любое вхождение
# одной из подстрок "AB" или "CD" из s.
# Возвращает минимально возможную длину результирующей строки, которую вы можете получить.
# Обратите внимание, что строка объединяется после удаления подстроки и может создавать новые "AB" или "CD" подстроки.

# Example 1:
# Input: s = "ABFCACDB"
# Output: 2
# Explanation: We can do the following operations:
# - Remove the substring "ABFCACDB", so s = "FCACDB".
# - Remove the substring "FCACDB", so s = "FCAB".
# - Remove the substring "FCAB", so s = "FC".

# Example 2:
# Input: s = "ACBBD"
# Output: 5

### Краткое условие:
# Надо пройтись по строке и удалить пары букв: AB и CD. Затем вывести длину строки.

# Алгоритм решение задачи:
# 0) Создать пустой массив stack
# 1) Пройтись циклом по строке s:
# 1.1) если буква в стеке и буква в строке образуют пару: AB или CD, то удалить .pop() последнию букву из стека
# 1.2) если буква в стеке и буква в строке НЕ образуют пару: AB или CD, то добовляем .append() букву из строки в стек
# 2) вернуть длину массива stack.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "ABFCACDB"

def minLength(s):
    stack = []

    for i in s:
        if len(stack) > 0 and (stack[-1] == 'A' and i == 'B' or stack[-1] == 'C' and i == 'D'):
            stack.pop()
        else:
            stack.append(i)
    # ['F', 'C']
    return len(stack) # 2

minLength(s)

assert minLength(s="ABFCACDB") == 2
assert minLength(s="ACBBD") == 5